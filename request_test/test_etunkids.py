import requests
import json


def test_baidu_request():

    http_get = requests.get('https://sports.sina.com.cn/g/pl/2023-08-15/doc-imzhftsi5431460.shtml')
    print('/n http_response_test: ', http_get.text)
    response_code = http_get.status_code
    print('code = ', response_code)
    assert response_code ==200