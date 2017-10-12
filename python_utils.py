# python 通过requests请求api
import requests

def get_api_result(url, filter_params):
        return requests.get(url, params=filter_params).json()
