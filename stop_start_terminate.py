import boto3

client = boto3.client('ec2')

#To Start the Instance
client.start_instances(InstanceIds=['i-01234543cd34'])

#To Stop the Instance
client.stop_instances(InstanceIds=['i-01234543cd34'])

#To Terminate the Instance
resp = client.terminate_instances(InstanceIds=['i-01234543cd34'])
for instance in resp['TerminatingInstances']:
    print("The instance {} Terminated".format(instance['InstanceId']))
