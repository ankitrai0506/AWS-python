import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(Filters=[
    {
        'Name':'availability-zone',
        'Values': ['us-east-1d']
    }

]):
    print('Instance id {} Instance Type {}'.format(instance.instance_id,instance.instance_type))
