import json
import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employee-s2mb')

ses = boto3.client('ses', region_name='ap-south-1')

def generate_temp_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def lambda_handler(event, context):

    try:
        print("EVENT:", event)

        body = event.get('body')

        if isinstance(body, str):
            body = json.loads(body)

        employee_id = body.get('employee_id')
        status = body.get('status')

        print("Employee ID:", employee_id)
        print("Status:", status)

        if not employee_id or not status:
            return {
                "statusCode": 400,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": "Missing employee_id or status"})
            }

        # ✅ GET EMPLOYEE DETAILS
        response = table.get_item(
            Key={"employee_id": employee_id}
        )

        item = response.get('Item')

        if not item:
            raise Exception("Employee not found")

        email = item.get('email')
        name = item.get('name')

        print("Email:", email)
        print("Name:", name)

        # ✅ UPDATE STATUS
        table.update_item(
            Key={"employee_id": employee_id},
            UpdateExpression="SET #s = :s",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":s": status}
        )

        # ✅ EMAIL CONTENT
        subject = ""
        message = ""

        if status == "APPROVED":

            temp_password = generate_temp_password()

            subject = "🎉 Welcome to the Company!"

            message = f"""

Hello {name},

Congratulations! 🎉 Your onboarding has been APPROVED.

Welcome to the company!

🔐 Your Login Credentials:

Employee ID: {employee_id}
Temporary Password: {temp_password}

🌐 Login here:
https://hrms-onboarding-portal.s3.ap-south-1.amazonaws.com/index.html

⚠️ Please login and change your password immediately after first login.

We’re excited to have you onboard 🚀

Best Regards,  
HR Team
"""

        elif status == "REJECTED":

            subject = "Onboarding Status Update"

            message = f"""
Hello {name},

We regret to inform you that your onboarding request has been REJECTED.

For more details, please contact HR.

Best Regards,  
HR Team
"""

        # ✅ SEND EMAIL (SES)
        ses.send_email(
            Source='supritha.p92003@gmail.com',  # MUST be verified
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': message}}
            }
        )

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": f"Employee {status} and email sent"
            })
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "error": str(e)
            })
        }