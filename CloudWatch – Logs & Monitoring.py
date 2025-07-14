import boto3
from datetime import datetime

cw = boto3.client('cloudwatch')
cw.put_metric_data(
    Namespace='ECommerce',
    MetricData=[{
        'MetricName': 'CheckoutErrors',
        'Value': 1,
        'Unit': 'Count',
        'Dimensions': [
            {'Name': 'Page', 'Value': 'Payment'},
            {'Name': 'Browser', 'Value': 'Safari'}
        ],
        'Timestamp': datetime.utcnow()
    }]
)