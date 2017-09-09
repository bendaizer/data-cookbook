import requests

URL = 'http://127.0.0.1:5000/'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def test_server_is_running():
    response = requests.get(URL, headers=HEADERS)
    assert response.status_code == 200