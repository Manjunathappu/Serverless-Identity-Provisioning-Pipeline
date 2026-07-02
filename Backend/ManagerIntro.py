import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employee-s2mb')

def lambda_handler(event, context):
    
    employee_id = event.get('employee_id')
    
    if not employee_id:
        return {
            'statusCode': 400,
            'body': json.dumps('employee_id is required')
        }
    
    table.update_item(
        Key={'employee_id': employee_id},
        UpdateExpression="SET manager_intro_done = :val, #st = :stage, #status = :s",
        ExpressionAttributeNames={
            "#st": "stage",
            "#status": "status"
        },
        ExpressionAttributeValues={
            ":val": True,
            ":stage": "COMPLETED",
            ":s": "ACTIVE"
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Onboarding Completed Successfully')
    }