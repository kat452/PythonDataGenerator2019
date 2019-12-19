from random import random


def generate_random_meal_heartrate():

    return {
        'device_model': "Apple watch",
        'system_name': "watchOS",
        'system_version': "6.1.1",

        'source_type': "health",
        'data_type': "heart_rate",
        'heart_beat_count': 70 + random()*50,
        'study_type': "meal_study",
        'subject_id': "7ba82a44-7c79-4d6f-94cf-5bfd678db34b",
        'phone_unique_id': "678328B8-E1A4-4DF4-B0FB-38673C77B70F",
        'watch_unique_id': "37C6FA39-C85B-4018-9D03-0B012BE67828",
        'app_version': "1.0.3"
    }




