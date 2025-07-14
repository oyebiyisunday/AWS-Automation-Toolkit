import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

table.put_item(Item={'UserID': '101', 'Name': 'John', 'Email': 'john@example.com'})
print(table.get_item(Key={'UserID': '101'}).get('Item'))
print(table.query(KeyConditionExpression=Key('UserID').eq('101'))['Items'])