import boto3

iamclient = boto3.client('iam')
iamresource = boto3.resource('iam')
user = iamresource.User('demouser')
group = iamresource.Group('demogroup')
user.create()
user.create_login_profile(Password='India@12345')

iamclient.attach_user_policy(UserName='demouser',PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')

group.create()
group.add_user(UserName='demouser')
