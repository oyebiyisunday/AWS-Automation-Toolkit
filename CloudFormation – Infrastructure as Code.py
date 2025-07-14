import boto3

cf = boto3.client('cloudformation')

try:
    with open('network.json') as f:
        cf.create_stack(
            StackName='ProdNetwork',
            TemplateBody=f.read(),
            Capabilities=['CAPABILITY_IAM']
        )
except cf.exceptions.ClientError as e:
    print(f"Template error: {e.response['Error']['Message']}")