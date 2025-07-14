import boto3, time, json

kinesis = boto3.client('kinesis')
try:
    kinesis.put_record(
        StreamName='clickstream',
        Data=json.dumps({'user': 'u_789', 'action': 'purchase'}).encode(),
        PartitionKey='u_789'
    )
except kinesis.exceptions.ProvisionedThroughputExceededException:
    time.sleep(2)  # Retry with backoff