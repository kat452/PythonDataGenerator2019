import boto3
import json
import time
#modified from tutorial at https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-hotspots-prepare.html
from random import random

# Modify this section to reflect your AWS configuration.
awsRegion = ""  # The AWS region where your Kinesis Analytics application is configured.
accessKeyId = ""  # Your AWS Access Key ID
secretAccessKey = ""  # Your AWS Secret Access Key
inputStream = "ExampleInputStream"  # The name of the stream being used as input into the Kinesis Analytics hotspots application

# Variables that control properties of the generated data.
xRange = [0, 10]  # The range of values taken by the x-coordinate
yRange = [0, 10]  # The range of values taken by the y-coordinate
hotspotSideLength = 1  # The side length of the hotspot
hotspotWeight = 0.2  # The fraction ofpoints that are draw from the hotspots
device_model = "Apple watch"
system_name = "watchOS"
system_version = "6.1.1"
#measurementTime changes
source_type = "raw"
data_type = "gyro"


#xyz are randomized
x_gyroRange = [0, 1]
y_gyroRange = [0, 1]
z_gyroRange = [0, 1]

study_type = "meal_study"
subject_id = "7ba82a44-7c79-4d6f-94cf-5bfd678db34b"
subject

def generate_point_in_rectangle(x_min, width, y_min, height):
    """Generate points uniformly in the given rectangle."""
    return {
        'x': x_min + random() * width,
        'y': y_min + random() * height
    }


class RecordGenerator(object):
    """A class used to generate points used as input to the hotspot detection algorithm. With probability hotspotWeight,
    a point is drawn from a hotspot, otherwise it is drawn from the base distribution. The location of the hotspot
    changes after every 1000 points generated."""

    def __init__(self):
        self.x_min = xRange[0]
        self.width = xRange[1] - xRange[0]
        self.y_min = yRange[0]
        self.height = yRange[1] - yRange[0]
        self.points_generated = 0
        self.hotspot_x_min = None
        self.hotspot_y_min = None

    def get_record(self):
        if self.points_generated % 1000 == 0:
            self.update_hotspot()

        if random() < hotspotWeight:
            record = generate_point_in_rectangle(self.hotspot_x_min, hotspotSideLength, self.hotspot_y_min,
                                                 hotspotSideLength)
            record['is_hot'] = 'Y'
        else:
            record = generate_point_in_rectangle(self.x_min, self.width, self.y_min, self.height)
            record['is_hot'] = 'N'

        self.points_generated += 1
        data = json.dumps(record)
        return {'Data': bytes(data, 'utf-8'), 'PartitionKey': 'partition_key'}

    def get_records(self, n):
        return [self.get_record() for _ in range(n)]

    def update_hotspot(self):
        self.hotspot_x_min = self.x_min + random() * (self.width - hotspotSideLength)
        self.hotspot_y_min = self.y_min + random() * (self.height - hotspotSideLength)


def main():
    kinesis = boto3.client('kinesis')

    generator = RecordGenerator()
    batch_size = 10

    while True:
        records = generator.get_records(batch_size)
        print(records)
        kinesis.put_records(StreamName="ExampleInputStream", Records=records)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
