import boto3

sqs = boto3.client('sqs')
queue_url = sqs.get_queue_url(QueueName='orders')['QueueUrl']

sqs.send_message(QueueUrl=queue_url, MessageBody='Order_789')
messages = sqs.receive_message(
    QueueUrl=queue_url, 
    MaxNumberOfMessages=5,
    WaitTimeSeconds=10
).get('Messages', [])

for msg in messages:
    print(msg['Body'])
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])