from datetime import datetime, timezone
from untested_helpers import from_datetime_to_string

def datetime_to_eventbrite_format(datetime_string):   
    dt = datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%SZ")
    # convert from current timezone to utc
    dt_utc = dt.astimezone(timezone.utc)
    return from_datetime_to_string(dt_utc)