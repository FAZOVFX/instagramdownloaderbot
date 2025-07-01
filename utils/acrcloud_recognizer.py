import os
import requests
import hashlib
import hmac
import base64
import time

def recognize_audio(filepath):
    host = os.getenv("ACR_HOST")
    access_key = os.getenv("ACR_KEY")
    access_secret = os.getenv("ACR_SECRET")

    http_method = "POST"
    http_uri = "/v1/identify"
    data_type = "audio"
    signature_version = "1"
    timestamp = str(int(time.time()))

    string_to_sign = f"{http_method}\n{http_uri}\n{access_key}\n{data_type}\n{signature_version}\n{timestamp}"
    sign = base64.b64encode(hmac.new(access_secret.encode(), string_to_sign.encode(), hashlib.sha1).digest()).decode()

    files = {'sample': open(filepath, 'rb')}
    data = {
        'access_key': access_key,
        'data_type': data_type,
        'signature_version': signature_version,
        'signature': sign,
        'timestamp': timestamp,
    }

    response = requests.post(f"http://{host}/v1/identify", files=files, data=data)
    try:
        result = response.json()
        if 'metadata' in result and 'music' in result['metadata']:
            return result['metadata']['music'][:3]
        else:
            return None
    except:
        return None
