import json
import boto3
import base64
import uuid
from datetime import datetime

# AWS Clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Resources
table = dynamodb.Table('Employee-s2mb')
BUCKET_NAME = 'hrms-documents-s2mb'


# ✅ FILE VALIDATION FUNCTION
def validate_file(file_content, max_size_mb=2):

    if not file_content:
        return False, "File missing"

    try:
        file_bytes = base64.b64decode(file_content)
    except Exception:
        return False, "Invalid file encoding"

    # ✅ Check size
    size_mb = len(file_bytes) / (1024 * 1024)

    if size_mb > max_size_mb:
        return False, f"File too large (>{max_size_mb}MB)"

    # ✅ Check PDF signature
    if not file_bytes.startswith(b'%PDF'):
        return False, "Only PDF files allowed"

    return True, file_bytes


# ✅ UPLOAD FUNCTION
def upload_file(file_bytes, employee_id, filename):

    key = f"employee-documents/{employee_id}/{filename}"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=file_bytes,
        ContentType='application/pdf'
    )

    return key


# ✅ MAIN HANDLER
def lambda_handler(event, context):

    try:
        body = json.loads(event['body'])

        # Generate employee ID
        employee_id = str(uuid.uuid4())

        # 🔍 VALIDATE FILES
        id_valid, id_result = validate_file(body.get("id_proof"))
        degree_valid, degree_result = validate_file(body.get("degree_certificate"))
        offer_valid, offer_result = validate_file(body.get("offer_letter"))

        if not id_valid:
            raise Exception(f"ID Proof Error: {id_result}")

        if not degree_valid:
            raise Exception(f"Degree Certificate Error: {degree_result}")

        if not offer_valid:
            raise Exception(f"Offer Letter Error: {offer_result}")

        # 📦 UPLOAD FILES
        id_key = upload_file(id_result, employee_id, "id_proof.pdf")
        degree_key = upload_file(degree_result, employee_id, "degree_certificate.pdf")
        offer_key = upload_file(offer_result, employee_id, "offer_letter.pdf")

        # 📊 SAVE TO DYNAMODB
        table.put_item(
            Item={
                "employee_id": employee_id,
                "name": body.get("name"),
                "email": body.get("email"),
                "department": body.get("department"),
                "role": body.get("role"),
                "manager": body.get("manager"),
                "joining_date": body.get("joining_date"),

                "status": "PENDING",
                "stage": "DOCUMENT_COLLECTION",

                "documents_uploaded": True,
                "it_provisioned": False,
                "policy_signed": False,
                "manager_intro_done": False,

                "created_at": datetime.utcnow().isoformat()
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Employee created successfully",
                "employee_id": employee_id
            })
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }