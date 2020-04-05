import requests
import json
from constants import const


async def post_data(people_count, device_type, zone_id):
    data = {"deviceId": device_type, "placeId": zone_id, "count": people_count}
    data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    requests.post(url=const.recreation_server_endpoint, headers=headers, data=data)
