import boto3

# Create a client for S3
s3 = boto3.client('s3')

# List buckets
resp = s3.list_buckets()
for bucket in resp['Buckets']:
    print(bucket['Name'])

# Upload a file
s3.upload_file('local_file.txt', 'my-bucket', 'remote_name.txt')