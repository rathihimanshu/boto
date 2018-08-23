import boto3

ec2 = boto3.resource('ec2')
instance = ec2.Instance('ec2')

ec2.create_instances(ImageId='ami-0cf31d971a3ca20d6',InstanceType='t2.micro',KeyName='prac',MaxCount=1,MinCount=1)
