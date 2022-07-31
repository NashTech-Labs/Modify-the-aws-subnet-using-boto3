# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def modify_subnet(subnet_id, map_public_ip_on_launch):

    try:
        response = vpc_client.modify_subnet(
            MapPublicIpOnLaunch={'Value': map_public_ip_on_launch},
            SubnetId=subnet_id)

    except ClientError:
        logger.exception('This can not be modify.')
        raise
    else:
        return response


if __name__ == '__main__':
    # SUBNET_ID = 'subnet-071923fde0da8166e'
    SUBNET_ID = input("Enter the subnet id")
    MAP_PUBLIC_IP_ON_LAUNCH = True
    subnet_attribute = modify_subnet(SUBNET_ID,MAP_PUBLIC_IP_ON_LAUNCH)
    logger.info(
        f'Your Subnet has been modified and new value: {MAP_PUBLIC_IP_ON_LAUNCH}'
    )