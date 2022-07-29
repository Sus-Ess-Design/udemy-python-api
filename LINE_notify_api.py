import json
with open('line.json') as f:
    line_json = json.load(f)
import requests

def notify_message(message):
    LINE_NOTIFY_TOKEN = line_json['LINE_NOTIFY_TOKEN']
    # Defined in line.json as following:
    #    {
    #        "LINE_NOTIFY_TOKEN": "YOUR_LINE_NOTIFY_TOKEN"
    #    }

    url = 'https://notify-api.line.me/api/notify'


    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }

    data = {
        'message': message
    }

    requests.post(
        url,
        headers=headers,
        data=data
    )

message = 'This is test message'
notify_message(message)
