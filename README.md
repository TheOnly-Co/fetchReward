# fetchReward

## Technology Used 

  - Python 
  - Boto3
  - Amazon Web Services

## How to 
  1. Preparation/Setup 
     - Make sure you are logged into AWS in the terminal 😄
     - Use a Linux or MacOs system, otherwise use [Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) instruction
  2. Make sure you have ```pip``` installed
  3. Then, ```pip install pyyaml```
  4. Then, ```pip install boto3```
  5. Run ```python server.py```
  6. Wait 1 minute for the instance to be created
  7. Email me for the private key and make a file and store as ```~/.ssh/fetchrewrads.pem```
  8. Run ```python print_public_ip1.py``` to get public IP output for the first instance and ssh into it by using ```ssh -i ~/.ssh/fetchrewards.pem ec2-user@11.XXX.XXX.XXX```
  9. Run ```python print_public_ip2.py``` to get public IP output for the second instance and ssh into it by using ```ssh -i ~/.ssh/fetchrewards.pem ec2-user@22.XXX.XXX.XXX```
