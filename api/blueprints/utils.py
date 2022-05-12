from datetime import datetime
import pytz


# TODO: Convert this to use a locale for user
def localise_tz(type_, obj):
    tz = pytz.timezone("UTC")

    if type_ == "environment":
        tz_time = tz.localize(obj.created)
        obj.created = tz_time.astimezone(tz=pytz.timezone("Europe/London"))
    elif type_ == "reading":
        tz_time = tz.localize(obj.time)
        obj.time = tz_time.astimezone(tz=pytz.timezone("Europe/London"))
    return obj
