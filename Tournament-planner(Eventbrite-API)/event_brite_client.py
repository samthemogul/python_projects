from urllib import request
import json
import os
from datetime import datetime, timezone
from untested_helpers import from_datetime_to_string

class EventBriteAPIHelper:
    
    def __init__(self):
        self.token = get_api_key()
        print(self.token)

    
    def get_organization_id(self):
        
        url = f'https://www.eventbriteapi.com/v3/users/me/organizations/?token={self.token}'

        request_object = request.Request(url, method="GET")
        request_object.add_header('Content-Type', 'application/json')

        opened_request = request.urlopen(request_object, data=None)
        result = opened_request.read().decode('utf-8')
        parsed = json.loads(result)
       
        print(f"{parsed['organizations'][0]['id']=}")
        return parsed['organizations'][0]['id']


    def create_event(self, title, description, start_time, end_time):
        organization_id = self.get_organization_id()
        
       
        data = {
            "event": {
                "currency": "USD",
                "name": {
                    "html": title
                },
                "description": {
                    "html": description
                },
                "start": {
                    "timezone": "UTC",
                    "utc": datetime_to_eventbrite_format(start_time)
                },
                "end": {
                    "timezone": "UTC",
                    "utc": datetime_to_eventbrite_format(end_time)
                },
            }
        }

        
        data = json.dumps(data)
        data = data.encode()
        
        
        url = f'https://www.eventbriteapi.com/v3/organizations/{organization_id}/events/?token={self.token}'

        
        req = request.Request(url, method="POST")
        req.add_header('Content-Type', 'application/json')
        
       
        opened_request = request.urlopen(req, data=data)

        
        content = opened_request.read().decode('utf-8')
        parsed = json.loads(content)

        # Returns the ID of the event created
        return parsed.get('id')

    
    def update_event(self, event_id, title, description, start_time, end_time):
        
        data = {
            "event": {
                "currency": "USD",
                "name": {
                    "html": title,
                    "text": title
                },
                "description": {
                    "html": description
                },
                "start": {
                    "timezone": "UTC",
                    "utc": datetime_to_eventbrite_format(start_time)
                },
                "end": {
                    "timezone": "UTC",
                    "utc": datetime_to_eventbrite_format(end_time)
                },
            }
        }

        data = json.dumps(data)
        data = data.encode()

        url = f'https://www.eventbriteapi.com/v3/events/{event_id}'

        req = request.Request(url, method="POST")
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', f'Bearer {self.token}')
        
        
        response = request.urlopen(req, data=data)
        content = response.read().decode('utf-8')
        parsed = json.loads(content)

        # Returns the ID of the event created
        return parsed.get('name')

    ########### HELPERS ###############

def get_api_key():
    '''Read the api key from the apikey.txt file'''
    if not os.path.exists('apikey.txt'):
        raise Exception("Please create a file named apikey.txt and paste the Private Token there")
   
    with open('apikey.txt') as f:
        return f.read().strip()


def datetime_to_eventbrite_format(datetime_string):   
    dt = datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%SZ")
    # convert from current timezone to utc
    dt_utc = dt.astimezone(timezone.utc)
    return from_datetime_to_string(dt_utc)

if __name__ == '__main__':
    client = EventBriteAPIHelper()
    result = client.update_event("778625418587", "Test Event changed", "something", "2024-05-12T02:00:00Z", "2024-05-12T04:00:00Z" )

    print(result)

    