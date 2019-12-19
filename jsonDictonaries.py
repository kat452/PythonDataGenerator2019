from random import random
import datetime
import deviceConfiguration


def generate_random_meal():

    return {
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'source_type': "active",
        'data_type': "meal",
        'start_time': "2019-12-02T13:43:41+0000", # TODO
        'stop_time': "2019-12-02T13:43:42+0000",  #TODO
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version
    }


def generate_random_gyro_details(xgyro_min, xgryo_max, ygyro_min, ygyro_max, zgyro_min, zgyro_max):
    """Generate values between 0 and 1 ."""
    return {
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'measurement_time': str(datetime.datetime.today()),
        'source_type': "raw",
        'data_type': "gyro",
        'xgyro': xgyro_min + random()*4,
        'ygyro': ygyro_min + random()*4,
        'zgyro': zgyro_min + random()*4,
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version
    }


def generate_random_heart_rate():

    return {
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'added_to_health': str(datetime.datetime.today()),
        'source_type': "health",
        'data_type': "heart_rate",
        'heart_beat_count': 70 + random()*50,
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version
    }


def generate_random_accelerometer_details(xgyro_min, xgryo_max, ygyro_min, ygyro_max, zgyro_min, zgyro_max):

    return{
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'measurement_time': str(datetime.datetime.today()),
        'source_type': "raw",
        'data_type': "accelerometer",
        'xgyro': xgyro_min + random()*4,
        'ygyro': ygyro_min + random()*4,
        'zgyro': zgyro_min + random()*4,
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version

    }


