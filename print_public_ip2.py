import yaml
import boto3

stream = open("config.yaml",'r')

data = yaml.load(stream, Loader=yaml.FullLoader)
s = boto3.Session(region_name="us-west-2")
ec2 = s.resource('ec2')

for instance in ec2.instances.all():
    if instance.tags[0]["Value"] == data["server"]["users"][1]["login"]:
        print('Here is the second instance public ip:\n'+ str(instance.public_ip_address))