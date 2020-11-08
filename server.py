import yaml
import boto3
import time 

stream = open("config.yaml",'r')

data = yaml.load(stream, Loader=yaml.FullLoader)

### create instance
s = boto3.Session(region_name="us-west-2")
ec2 = s.resource('ec2')

instance = ec2.create_instances(ImageId='ami-0528a5175983e7f28',
                                KeyName='infra-master-key',
                                InstanceType=data["server"]["instance_type"],
                                SubnetId='subnet-04879e65a37dc5864',
                                MaxCount=1,
                                MinCount=1,
                                BlockDeviceMappings=[{
                                    'DeviceName':data["server"]["volumes"][0]["device"],
                                    'Ebs':{
                                        'VolumeSize':data["server"]["volumes"][0]["size_gb"],
                                        'VolumeType':data["server"]["volumes"][0]["type"]
                                    }
                                }]) 
#print(data["server"]["volumes"][0]["device"])
print("instance created")
