import requests
from django.conf import settings


def get_port_one_token():
    url = "https://api.iamport.kr/users/getToken"
    headers = {"Content-Type": "application/json"}
    data = {
        "imp_key": settings.PORT_ONE_API_KEY,
        "imp_secret": settings.PORT_ONE_SECRET_KEY,
    }
    response = requests.post(url, json=data)
    result = response.json()

    if response.status_code == 200:
        return result["response"]["access_token"]
    else:
        raise Exception("Failed to get PortOne token: " + result.get("message"))
