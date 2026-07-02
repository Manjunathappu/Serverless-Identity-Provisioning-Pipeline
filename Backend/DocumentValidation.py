import json
import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

table = dynamodb.Table('Employee-s2mb')

# 🔔 Replace with your SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:619336173896:hrms-notification-s2mb"


def lambda_handler(event, context):

    try:
        # Get S3 event details
        record = event['Records'][0]
        key = record['s3']['object']['key']

        print("Uploaded file:", key)

        # Extract employee_id from path
        # Format: employee-documents/{employee_id}/file.pdf
        parts = key.split("/")
        employee_id = parts[1]

        print("Employee ID:", employee_id)

        # ✅ Update DynamoDB
        table.update_item(
            Key={"employee_id": employee_id},
            UpdateExpression="SET documents_uploaded = :val, #st = :stage",
            ExpressionAttributeValues={
                ":val": True,
                ":stage": "HR_REVIEW"
            },
            ExpressionAttributeNames={
                "#st": "stage"
            }
        )

        # 🔔 Send SNS Notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="📄 Documents Uploaded - HR Action Required",
            Message=f"""
Employee ID: {employee_id}

Documents have been uploaded successfully.

👉 Please review and approve in HR Dashboard.
"""
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Validation completed + HR notified")
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }