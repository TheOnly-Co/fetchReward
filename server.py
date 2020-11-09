import yaml
import boto3
import time 

stream = open("config.yaml",'r')

data = yaml.load(stream, Loader=yaml.FullLoader)

### create instance
s = boto3.Session(region_name="us-west-2")
ec2 = s.resource('ec2')
user_data_script = "#!/bin/bash\nadduser %s\nmkdir -p /home/%s/.ssh\n echo\"%s\" >> /home/%s/.ssh/authorized_keys \nchown -R %s:%s /home/%s" % (data["server"]["users"][0]["login"],
    data["server"]["users"][0]["login"],
    data["server"]["users"][0]["ssh_key"],
    data["server"]["users"][0]["login"],
    data["server"]["users"][0]["login"],
    data["server"]["users"][0]["login"],
    data["server"]["users"][0]["login"])
def create_instance():
    instance = ec2.create_instances(ImageId='ami-0528a5175983e7f28',
                                    KeyName=data["server"]["keyName"],
                                    InstanceType=data["server"]["instance_type"],
                                    SubnetId='subnet-04879e65a37dc5864',
                                    MaxCount=1,
                                    MinCount=1,
                                    UserData=user_data_script,
                                    BlockDeviceMappings=[{
                                        'DeviceName':data["server"]["volumes"][0]["device"],
                                        'Ebs':{
                                            'VolumeSize':data["server"]["volumes"][0]["size_gb"],
                                            'VolumeType':data["server"]["volumes"][0]["type"]
                                        }
                                    }],
                                    TagSpecifications=[
                                        {
                                            'ResourceType': 'instance',
                                            'Tags': [
                                                {
                                                    'Key': 'Name',
                                                    'Value': data["server"]["users"][0]["login"]
                                                },
                                            ]
                                        },
                                    ])

def create_second_instance():
    instance = ec2.create_instances(ImageId='ami-0528a5175983e7f28',
                                    KeyName=data["server"]["keyName"],
                                    InstanceType=data["server"]["instance_type"],
                                    SubnetId='subnet-04879e65a37dc5864',
                                    MaxCount=1,
                                    MinCount=1,
                                    UserData=user_data_script,
                                    BlockDeviceMappings=[{
                                        'DeviceName':data["server"]["volumes"][1]["device"],
                                        'Ebs':{
                                            'VolumeSize':data["server"]["volumes"][1]["size_gb"],
                                            'VolumeType':data["server"]["volumes"][1]["type"]
                                        }
                                    }],
                                    TagSpecifications=[
                                        {
                                            'ResourceType': 'instance',
                                            'Tags': [
                                                {
                                                    'Key': 'Name',
                                                    'Value': data["server"]["users"][1]["login"]
                                                },
                                            ]
                                        },
                                    ])



create_instance()
create_second_instance()
print("instance created")
