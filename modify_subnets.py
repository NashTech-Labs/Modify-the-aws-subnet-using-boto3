# MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION: ")

# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client_for_subnet = boto3.client("ec2", region_name=REGION)


def modify_subnet(subnet_id, public_ip):

    try:
        res = client_for_subnet.modify_subnet_attribute(
            MapPublicIpOnLaunch={'Value': public_ip},
            SubnetId=subnet_id)
# This modify_subnet_attribute() will not return any type of output when it is done successful.


    except ClientError:
        logger_for.exception('This can not be modify.')
        raise
    else:
        return res


if __name__ == '__main__':
    ID = input("Enter the subnet id")
    MAP_PUBLIC_IP = True #input("Enter your answer in True or Flase: ")
    subnet_attribute = modify_subnet(ID,MAP_PUBLIC_IP)
    logger_for.info(
        f'Your Subnet has been modified and new value: {MAP_PUBLIC_IP}'
    )
