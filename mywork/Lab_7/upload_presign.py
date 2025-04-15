import requests
import boto3

url = 'https://media.tenor.com/PGerqATnNL8AAAAM/thumbs-up.gif'
file_name = 'thumbs-up.gif'

response = requests.get(url)
with open(file_name, 'wb') as file:
    file.write(response.content)

print("File saved success")

bucket_name = 'my-first-bucket-aur8dm'
object_name = file_name
expires_in = 604800


s3 = boto3.client('s3', region_name='us-east-1')
s3.upload_file(file_name, bucket_name, object_name)
print(f"File {file_name} uploaded to bucket {bucket_name}.")

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print(f"Presigned URL: {response}")
