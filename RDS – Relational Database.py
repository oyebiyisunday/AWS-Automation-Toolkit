import boto3

rds = boto3.client('rds')
for db in rds.describe_db_instances()['DBInstances']:
    print(f"{db['DBInstanceIdentifier']}: {db['DBInstanceStatus']} ({db['Engine']} {db['EngineVersion']})")