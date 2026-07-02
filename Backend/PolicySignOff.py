import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employee-s2mb')

def lambda_handler(event, context):
    
    # get employee_id from request
    employee_id = event.get('employee_id')
    
    if not employee_id:
        return {
            'statusCode': 400,
            'body': json.dumps('employee_id is required')
        }
    
    # update DynamoDB
    table.update_item(
        Key={'employee_id': employee_id},
        UpdateExpression="SET policy_signed = :val, #st = :stage",
        ExpressionAttributeNames={"#st": "stage"},
        ExpressionAttributeValues={
            ":val": True,
            ":stage": "POLICY_SIGN"
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Policy Signed Successfully')
    }