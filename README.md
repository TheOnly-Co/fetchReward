# fetchReward

## Technology Used 

  - Python 
  - Boto3
  - Amazon Web Services

## How to 

  - Make sure you have ```pip``` installed
  - Then, ```pip install pyyaml```
  - Then, ```pip install boto3```
  - Run ```python server.py```
  - Wait 1 minute for the instance to be created
  - Run ```python print_public_ip1.py``` to get public IP output for the first instance and ssh into it by using ```ssh -i fetchreward.pem ec2-user@11.XXX.XXX.XXX```
  - Run ```python print_public_ip2.py``` to get public IP output for the second instance and ssh into it by using ```ssh -i fetchreward.pem ec2-user@22.XXX.XXX.XXX```
