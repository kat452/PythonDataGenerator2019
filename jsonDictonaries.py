from random import random
import datetime


def generate_random_meal_heartrate():

    return {
        'device_model': "Apple watch",
        'system_name': "watchOS",
        'system_version': "6.1.1",
        'source_type': "active",
        'data_type': "meal",
        'start_time': "2019-12-02T13:43:41+0000",
        'stop_time': "2019-12-02T13:43:42+0000",
        'study_type': "meal_study",
        'subject_id' : "yashtech",
        'phone_unique_id': "678328B8-E1A4-4DF4-B0FB-38673C77B70F",
        'watch_unique_id': "37C6FA39-C85B-4018-9D03-0B012BE67828",
        'app_version': "1.0"
    }


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


def generate_random_heart_rate():

    return {
        'device_model': "Apple watch",
        'system_name': "watchOS",
        'system_version': "6.1.1",
        'added_to_health': str(datetime.datetime.today()),
        'source_type': "health",
        'data_type': "heart_rate",
        'heart_beat_count': 70 + random()*50,
        'study_type': "meal_study",
        'subject_id': "7ba82a44-7c79-4d6f-94cf-5bfd678db34b",
        'phone_unique_id': "678328B8-E1A4-4DF4-B0FB-38673C77B70F",
        'watch_unique_id': "37C6FA39-C85B-4018-9D03-0B012BE67828",
        'app_version': "1.0.3"
    }


def generate_random_accelerometer_details(xgyro_min, xgryo_max, ygyro_min, ygyro_max, zgyro_min, zgyro_max):

    return{
        'device_model': "Apple watch",
        'system_name': "watchOS",
        'system_version': "6.1.1",
        'measurement_time': str(datetime.datetime.today()),
        'source_type': "raw",
        'data_type': "accelerometer",
        'xgyro': xgyro_min + random(),
        'ygyro': ygyro_min + random(),
        'zgyro': zgyro_min + random(),
        'study_type': "meal_study",
        'subject_id': "7ba82a44-7c79-4d6f-94cf-5bfd678db34b",
        'phone_unique_id': "678328B8-E1A4-4DF4-B0FB-38673C77B70F",
        'watch_unique_id': "37C6FA39-C85B-4018-9D03-0B012BE67828",
        'app_version': "1.0.3"

    }


