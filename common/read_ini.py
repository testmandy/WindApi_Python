# coding=utf-8
# @Time    : 2019/12/19 16:21
# @Author  : Mandy
import configparser
import json

import conftest


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = conftest.env_dir
        else:
            self.file_path = file_path
        self.conf = self.read_ini()

    def read_ini(self):
        """调用读取配置模块中的类"""
        conf = configparser.ConfigParser()
        conf.read(self.file_path, encoding="utf-8")
        return conf

    def get_value(self, key, section=None):
        if section is None:
            value = self.conf.get('Common', key)
        else:
            value = self.conf.get(section, key)
        return value

    def modify_value(self, section, key, value):
        self.conf.set(section, key, value)

    def modify_value_json(self, section, key):
        new_json = json.loads(self.get_value(section, key))
        new_json.set


if __name__ == '__main__':
    ini = ReadIni()
    data = ini.get_value('header')
    data = json.loads(data)
    print(type(data))
    print(data)

