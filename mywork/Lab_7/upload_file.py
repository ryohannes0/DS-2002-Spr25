import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'my-first-bucket-aur8dm'
local_file = 'victory_logo.jpg'

with open(local_file, 'rb') as data:
    s3.put_object(Body=data, Bucket=bucket, Key='victory_logo.jpg')
print(f"File {local_file} uploaded successfully to bucket}.")
