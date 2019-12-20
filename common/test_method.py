# coding=utf-8
# @Time    : 2019/12/11 17:00
# @Author  : Mandy
import json

import requests


class Method:
    def get_method(self, url, header=None):
        res = requests.get(url=url, headers=header).json()
        return json.dumps(res, indent=2)

    def post_method(self, url, data, header=None):
        res = requests.post(url=url, data=data, headers=header).json()
        return json.dumps(res, indent=2)

    def run_main(self, method, url, data, header):
        if method == 'get':
            res = self.get_method(url, header)
        else:
            res = self.post_method(url, data, header)
        return res
