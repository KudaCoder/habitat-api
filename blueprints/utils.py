from dotenv import load_dotenv
from datetime import datetime
import requests
import json
import pytz


# TODO: Convert this to use a locale for user
def localise_tz(data):
    if isinstance(data, list):
        for data_point in data:
            data_point = perform_localise(data_point)
    else:
        data = perform_localise(data)
    
    return data

def perform_localise(data):
    for k, v in data.items():
        if isinstance(v, str):
            try:
                tz = pytz.timezone("UTC")
                utc_time = datetime.fromisoformat(v)
                tz_time = tz.localize(utc_time)
                data[k] = tz_time.astimezone(tz=pytz.timezone("Europe/London")).isoformat()
            except Exception:
                # Not an isoformat, just move on
                pass
    return data
