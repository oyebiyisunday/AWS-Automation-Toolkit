import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
bucket_name = 'my-unique-bucket-2025'

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
    )
    s3.upload_file(
        'report.pdf', 
        bucket_name, 
        '2025/report.pdf',
        ExtraArgs={'ACL': 'public-read'}
    )
    print([b['Name'] for b in s3.list_buckets()['Buckets']])
except ClientError as e:
    if e.response['Error']['Code'] == 'BucketAlreadyExists':
        print("Error: Bucket name already taken")