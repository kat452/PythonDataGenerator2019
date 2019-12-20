import boto3
import json
import time
import datetime
import config
import jsonDictonaries

'#modified from tutorial at https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-prepare.html'
from random import random
from random import randint

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
        return [self.get_gyro_record(current_time) for _ in range(n)]

    def get_accelerometer_records(self, n, current_time):
        return [self.get_accelerometer_record(current_time) for _ in range(n)]

    def get_heart_records(self, n, current_time):
        return [self.get_heart_record(current_time) for _ in range(n)]

    def get_accelerometer_record(self, current_time):
        accelerometer = jsonDictonaries.generate_random_accelerometer_details(current_time)
        data = json.dumps(accelerometer)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}

    def get_gyro_record(self, current_time):
        gyro = jsonDictonaries.generate_random_gyro_details(self.xgyro_min, self.xgyro_max, self.ygyro_min,
                                                            self.ygyro_max, self.zgyro_min, self.zgyro_min,
                                                            current_time)
        data = json.dumps(gyro)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}
        # return data

    def get_heart_record(self, current_time):
        heart = jsonDictonaries.generate_random_heart_rate(current_time)
        data = json.dumps(heart)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}

    def get_meal_record(self):
        meal = jsonDictonaries.generate_random_meal_details()
        data = json.dumps(meal)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}


def main():
    kinesis = boto3.client('kinesis', aws_access_key_id=accessKeyId, aws_secret_access_key=secretAccessKey)
    generator = RecordGenerator()
    batch_size = randint(1, 60)  # TODO get minimum and maximum batch size
    heart_batch_size = 3
    '#This was changed because of request for batch size of 100'
    count = 0
    total = 0
    generation_per_second = .05
    heart_count = 0
   # heart_random_rate = randint(0, 5)
    prev_time_batch_rate =datetime.datetime.now();
    prev_time_heart = datetime.datetime.now();
    while True:
        current_time = datetime.datetime.now()
        records = generator.get_gyro_records(batch_size, current_time)
        print(records)
        # kinesis.put_records(StreamName=inputStream, Records=records)    # TODO change to kinesis stream name'
        records = generator.get_accelerometer_records(batch_size, current_time)
       # print(records)
        # kinesis.put_records(StreamName=inputStream, Records=records)    # TODO change to kinesis stream name'
        total = total + batch_size
        # print(total)

        if prev_time_heart + datetime.timedelta(minutes=1) < datetime.datetime.now():
            prev_time_heart = datetime.datetime.now()
            print(".......... HEART RATE.............")
            records = generator.get_heart_records(batch_size, current_time)
            print(records)
            prev_time_heart = datetime.datetime.now()

        if (count % 1000) == 1:
            # for meal record
             records = generator.get_meal_record()
            # print("................. MEAL RECORD.......................")
            # print(records)
            # kinesis.put_records(StreamName=inputStream, Records=records)    # TODO change to kinesis stream name'
            # for heart record
             print(".......... HEART RATE.............")
            # records = generator.get_heart_records(batch_size, current_time)
             print(records)
            # kinesis.put_records(StreamName=inputStream, Records=records)    # TODO change to kinesis stream name'
        '#in seconds'
        '#if (int(count / (1 / generation_per_second)) % heart_random_rate) == 0:'
        # print(" ")
        # print(count / (1 / generation_per_second))
        # print(" ")
        if (prev_time_batch_rate + datetime.timedelta(seconds=1)) < datetime.datetime.now():
            # if (count / (1 / generation_per_second)) == 1:
            prev_time_batch_rate = datetime.datetime.now()
            batch_size = randint(1, 5)
            timex = datetime.datetime.now()
            print("batch size is  " + str(batch_size) + " at time " + str(timex))

        count = count + 1

        time.sleep(generation_per_second)
        # TODO per second send 60 records

        '#TODO the combination of time.sleep and batch size will determine how many in a minute, '
        '#and how they are spaced out'


if __name__ == "__main__":
    main()
