import boto3
import json

lambda_client = boto3.client('lambda')

try:
    response = lambda_client.invoke(
        FunctionName='data-processor',
        InvocationType='RequestResponse',
        Payload=json.dumps({'filename': 'data.csv'}).encode()
    )
    print(json.loads(response['Payload'].read().decode()))
except lambda_client.exceptions.ResourceNotFoundException:
    print("Error: Function not found")