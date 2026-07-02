import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employee-s2mb')

def lambda_handler(event, context):
    
    print("EVENT:", event)   # 🔥 Debug line

    employee_id = event.get('employee_id')
    
    if not employee_id:
        return {
            'statusCode': 400,
            'body': json.dumps('employee_id is missing')
        }
    
    table.update_item(
        Key={'employee_id': employee_id},
        UpdateExpression="SET it_provisioned = :val, #st = :stage",
        ExpressionAttributeNames={
            "#st": "stage"
        },
        ExpressionAttributeValues={
            ":val": True,
            ":stage": "IT_PROVISIONING"
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('IT Provisioning Done')
    }