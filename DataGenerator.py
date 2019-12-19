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
    """#Ok define attributes of this class"""
    def __init__(self):
        self.xgyro_min = -2
        self.xgyro_max = +2
        self.ygyro_min = -2
        self.ygyro_max = +2
        self.zgyro_min = -2
        self.zgyro_max = +2

    def get_gyro_records(self, n, current_time):
        return [self.get_gyro_record(current_time)for _ in range(n)]

    def get_accelerometer_records(self, n, current_time):
        return [self.get_accelerometer_record(current_time)for _ in range(n)]

    def get_heart_records(self, n, current_time):
        return [self.get_heart_record(current_time)for _ in range(n)]

    def get_accelerometer_record(self, current_time):
        accelerometer = jsonDictonaries.generate_random_accelerometer_details(current_time)
        data = json.dumps(accelerometer)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}
        """return data"""

    def get_gyro_record(self, current_time):
        gyro = jsonDictonaries.generate_random_gyro_details(self.xgyro_min, self.xgyro_max, self.ygyro_min,
                                                            self.ygyro_max, self.zgyro_min, self.zgyro_min,
                                                            current_time)
        data = json.dumps(gyro)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}
        """return data"""

    def get_heart_record(self, current_time):
        heart = jsonDictonaries.generate_random_heart_rate(current_time)
        data = json.dumps(heart)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}
        """return data"""

    def get_meal_record(self):
        meal = jsonDictonaries.generate_random_meal()
        data = json.dumps(meal)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}


def main():
    kinesis = boto3.client('kinesis', aws_access_key_id=accessKeyId, aws_secret_access_key=secretAccessKey)
    generator = RecordGenerator()
    batch_size = 1
    '#This was changed because of request for batch size of 100'
    count = 0
    while True:
        "# records = generator.get_records(batch_size)"
        current_time = datetime.datetime.now()
        """records = generator.get_passive_records(batch_size)"""
        records = generator.get_gyro_records(batch_size, current_time)
        print(records)
        records = generator.get_heart_records(batch_size, current_time)
        print(records)
        records = generator.get_accelerometer_records(batch_size, current_time)
        print(records)
        '# kinesis.put_records(StreamName="test", Records=records)    # TODO change to kinesis stream name'

        count= count+1

        if (count % 1000) == 1:
            records = generator.get_meal_record()
            print(records)

        '#in seconds'
        time.sleep(0.1)
        '#TODO the combination of time.sleep and batch size will determine how many in a minute, '
        '#and how they are spaced out'


if __name__ == "__main__":
    main()

    """
        def get_record(self):

            record = jsonDictonaries.generate_random_gyro_details(self.xgyro_min, self.xgyro_max, self.ygyro_min,
                                                                  self.ygyro_max, self.zgyro_min, self.zgyro_max)
            data = json.dumps(record)
            record1 = jsonDictonaries.generate_random_meal()
            data1 = json.dumps(record1)
            record = jsonDictonaries.generate_random_accelerometer_details()
            # return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}
            return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}

        def get_records(self, n):
            return [self.get_record() for _ in range(n)]
    """
    """   def get_passive_records(self, n):
            return [self.get_passive_record() for _ in range(n)]"""
    """def get_passive_record(self):
        current_time = datetime.datetime.now()
        acc = self.get_accelerometer_record(current_time)
        gyro = self.get_gyro_record(current_time)
        heart = self.get_gyro_record(current_time)
        return acc, gyro, heart"""

