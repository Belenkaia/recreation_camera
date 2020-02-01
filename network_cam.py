import requests
import json


def post_data(people_count, device_type, zone_id):
    data = {"deviceId": device_type, "placeId": zone_id, "count": people_count}
    data = json.dumps(data)
    addr = "http://192.168.1.64:8080/recreation/api/data"
    headers = {'content-type': 'application/json'}
    r = requests.post(url=addr, headers=headers, data=data)
