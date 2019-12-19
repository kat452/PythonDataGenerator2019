from random import random


def generate_random_gyro_details(today):
    """Generate values between 0 and 1 ."""
    return {
        'device_model': "Apple watch",
        'system_name': "watchOS",
        'system_version': "6.1.1",
        'measurement_time': today,
        'source_type': "raw",
        'data_type': "gyro",
        'xgyro': random(),
        'ygyro': random(),
        'zgyro': random(),
        'study_type': "meal_study",
        'subject_id': "7ba82a44-7c79-4d6f-94cf-5bfd678db34b",
        'phone_unique_id': "678328B8-E1A4-4DF4-B0FB-38673C77B70F",
        'watch_unique_id': "37C6FA39-C85B-4018-9D03-0B012BE67828",
        'app_version': "1.0.3"
    }


