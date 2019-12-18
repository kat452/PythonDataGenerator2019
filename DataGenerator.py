import boto3
import json
import time
import datetime

'#modified from tutorial at https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-prepare.html'
from random import random

# TODO need to configure these securely

awsRegion = ""  # The AWS region where your Kinesis Analytics application is configured.
accessKeyId = ""  # Your AWS Access Key ID
secretAccessKey = ""  # Your AWS Secret Access Key
inputStream = "ExampleInputStream"

'# The name of the stream being used as input into the Kinesis Analytics hotspots application'

'# Variables that control properties of the generated data.'
'#xRange = [0, 10]  # The range of values taken by the x-coordinate'
'#yRange = [0, 10]  # The range of values taken by the y-coordinate'
'#hotspotSideLength = 1  # The side length of the hotspot'
'#hotspotWeight = 0.2  # The fraction ofpoints that are draw from the hotspots'

'measurementTime = str(datetime.now())'

'#xyz are randomized'
'#This needs to be randomized'
'#xgyro_Range = [0, 1]'
'#this needs to be randomized'
'#ygyro_Range = [0, 1]'
'#this needs to be randomized'
'#zgyro_Range = [0, 1]'


def generate_random_gyro_details(xgyro_min, xgryo_max, ygyro_min, ygyro_max, zgyro_min, zgyro_max):
    """Generate values between 0 and 1 ."""
    return {
        'device_model': "Apple watch",
        'system_name': "watchOS",
        'system_version': "6.1.1",
        'measurement_time': str(datetime.datetime.today()),
        'source_type': "raw",
        'data_type': "gyro",
        'xgyro': xgyro_min + random(),
        'ygyro': ygyro_min + random(),
        'zgyro': zgyro_min + random(),
        'study_type': "meal_study",
        'subject_id': "7ba82a44-7c79-4d6f-94cf-5bfd678db34b",
        'phone_unique_id': "678328B8-E1A4-4DF4-B0FB-38673C77B70F",
        'watch_unique_id': "37C6FA39-C85B-4018-9D03-0B012BE67828",
        'app_version': "1.0.3"
    }


class RecordGenerator(object):
    """A class used to generate points used as input to the hotspot detection algorithm. With probability hotspotWeight,
    a point is drawn from a hotspot, otherwise it is drawn from the base distribution. The location of the hotspot
    changes after every 1000 points generated."""

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
        """"in the original code this had to do with changing starting info on position every so many "points"""
        """if self.points_generated % 1000 == 0:
            self.update_hotspot()"""
        record = generate_random_gyro_details(
            self.xgyro_min, self.xgyro_max, self.ygyro_min, self.ygyro_max, self.zgyro_min, self.zgyro_max)
        """if random() < hotspotWeight:
            record = generate_point_in_rectangle(self.hotspot_x_min, hotspotSideLength, self.hotspot_y_min,
                                                 hotspotSideLength)
            record['is_hot'] = 'Y'
        else:
            record = generate_point_in_rectangle(self.x_min, self.width, self.y_min, self.height)
            record['is_hot'] = 'N' 
        #self.points_generated += 1"""
        data = json.dumps(record)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}

    def get_records(self, n):
        return [self.get_record() for _ in range(n)]


""" def update_hotspot(self):
        self.hotspot_x_min = self.x_min + random() * (self.width - hotspotSideLength)
        self.hotspot_y_min = self.y_min + random() * (self.height - hotspotSideLength) """


def main():
    kinesis = boto3.client('kinesis')

    generator = RecordGenerator()
    batch_size = 1
    '#This was changed because of request for batch size of 100'

    while True:
        records = generator.get_records(batch_size)
        print(records)
        kinesis.put_records(StreamName="ExampleInputStream", Records=records)
        # TODO change to kinesis stream name

        '#in seconds'
        time.sleep(0.1)

        '#TODO the combination of time.sleep and batch size will determine how many in a minute, '
        '#and how they are spaced out'


if __name__ == "__main__":
    main()
