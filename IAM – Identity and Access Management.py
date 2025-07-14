import boto3, json

iam = boto3.client('iam')
role = iam.create_role(
    RoleName='LambdaRole',
    AssumeRolePolicyDocument=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    })
)
iam.attach_role_policy(
    RoleName='LambdaRole',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
)
print(role['Role']['Arn'])