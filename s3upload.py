import boto3

s3 = boto3.client('s3')

s3.upload_file('/root/boto/index.html','testrnjkfadklbucketcloudformation','index.html')
