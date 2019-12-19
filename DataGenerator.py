import boto3
import json
import time
import datetime
import config
import jsonDictonaries
'#modified from tutorial at https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-prepare.html'
from random import random

# Modify this section to reflect your AWS configuration.
awsRegion = "us-east-1"  # The AWS region where your Kinesis Analytics application is configured.
accessKeyId = config.accessKeyId  # Your AWS Access Key ID
secretAccessKey = config.secretAccessKey  # Your AWS Secret Access Key
inputStream = "test"


class RecordGenerator(object):


    '#Ok define attributes of this class'
    def __init__(self):
        self.xgyro_min = 0
        self.xgyro_max = 1
        self.ygyro_min = 0
        self.ygyro_max = 1 
        self.zgyro_min = 0
        self.zgyro_max = 1
        """self.x_min = xRange[0]
        self.width = xRange[1] - xRange[0]
        self.y_min = yRange[0]
        self.height = yRange[1] - yRange[0]
        self.points_generated = 0
        self.hotspot_x_min = None
        self.hotspot_y_min = None"""

    def get_record(self):

        record = jsonDictonaries.generate_random_gyro_details(self.xgyro_min, self.xgyro_max, self.ygyro_min,
                                                              self.ygyro_max, self.zgyro_min, self.zgyro_max)
        data = json.dumps(record)
        record1 = jsonDictonaries.generate_random_meal()
        data1 = json.dumps(record1)
        record = jsonDictonaries.generate_random_accelerometer_details(self.xgyro_min, self.xgyro_max, self.ygyro_min,
                                                              self.ygyro_max, self.zgyro_min, self.zgyro_max)
        #return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}

    def get_records(self, n):
        return [self.get_record() for _ in range(n)]


def main():
    kinesis = boto3.client('kinesis', aws_access_key_id=accessKeyId, aws_secret_access_key=secretAccessKey)
    generator = RecordGenerator()
    batch_size = 1
    '#This was changed because of request for batch size of 100'

    while True:
        records = generator.get_records(batch_size)
        print(records)
        '# kinesis.put_records(StreamName="test", Records=records)    # TODO change to kinesis stream name'

        '#in seconds'
        time.sleep(0.1)
        '#TODO the combination of time.sleep and batch size will determine how many in a minute, '
        '#and how they are spaced out'


if __name__ == "__main__":
    main()
