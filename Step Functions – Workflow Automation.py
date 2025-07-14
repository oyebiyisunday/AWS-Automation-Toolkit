import boto3, json

sf = boto3.client('stepfunctions')
sf.start_execution(
    stateMachineArn='arn:aws:states:us-east-1:123456789012:stateMachine:OrderFlow',
    name='Order_789',
    input=json.dumps({"items": 3, "total": 149.99})
)