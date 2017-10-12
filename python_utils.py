========================================================================
# python 通过requests请求api
import requests

def get_api_result(url, filter_params):
        return requests.get(url, params=filter_params).json()

========================================================================
#python 保存数据为csv文件

import csv

headers = ['xxx', 'xxx']
with open('csv_name.csv','wb') as f:
        f_csv = csv.DictWriter(f, headers)
        f.write(','.join(headers))
        f.write('\n')
        f_csv.writerows(info_list)

=========================================================================
#python json转dict

import json

d = json.loads(param)
