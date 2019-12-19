from random import random
from _datetime import datetime
from datetime import timedelta
import deviceConfiguration
from random import randint


def generate_random_meal():

    return {
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'source_type': "active",
        'data_type': "meal",
        'start_time': str(datetime.now() - timedelta(minutes=randint(0, 60))),
        'stop_time': str(datetime.now()),
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version
    }


def generate_random_gyro_details(xgyro_min, x_range, ygyro_min, y_range, zgyro_min, z_range):
    """Generate values between 0 and 1 ."""
    return {
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'measurement_time': str(datetime.today()),
        'source_type': "raw",
        'data_type': "gyro",
        'xgyro': xgyro_min + random()*x_range,
        'ygyro': ygyro_min + random()*y_range,
        'zgyro': zgyro_min + random()*z_range,
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
        'added_to_health': str(datetime.today()),
        'data_sync_time': str(datetime.today() + timedelta(seconds=randint(0, 100))),
        'source_type': "health",
        'data_type': "heart_rate",
        'heart_beat_count': 70 + random()*50,
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version
    }


def generate_random_accelerometer_details():

    return{
        'device_model': deviceConfiguration.device_model,
        'system_name': deviceConfiguration.system_name,
        'system_version': deviceConfiguration.system_version,
        'measurement_time': str(datetime.today()),
        'source_type': "raw",
        'data_type': "accelerometer",
        'x_acceleration': -2 + random()*4,
        'y_acceleration': -2 + random()*4,
        'z_acceleration': -2 + random()*4,
        'study_type': "meal_study",
        'subject_id': deviceConfiguration.subject_id,
        'phone_unique_id': deviceConfiguration.phone_unique_id,
        'watch_unique_id': deviceConfiguration.watch_unique_id,
        'app_version': deviceConfiguration.app_version

    }


