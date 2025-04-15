import boto3

s3 = boto3.client('s3', region_name='us-east-1')

# Define the bucket and file to upload
bucket = 'ds2002-aur8dm'  # Replace with your actual bucket name
local_file = 'path/to/your/file.jpg'  # Replace with the local file path

# Upload the file to S3
with open(local_file, 'rb') as data:
    s3.put_object(Body=data, Bucket=bucket, Key='victory_logo.jpg')  # Change the Key if needed

print(f"File {local_file} uploaded successfully to {bucket}.")
