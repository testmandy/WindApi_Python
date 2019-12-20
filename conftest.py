# coding=utf-8
# @Time    : 2019/12/19 16:23
# @Author  : Mandy
import logging
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(project_dir, 'logs\\')

env_dir = os.path.join(project_dir, 'data\\env.ini')

config_dir = os.path.join(project_dir, 'config')

case_dir = os.path.join(project_dir, 'testcases\\article.py')

IdColNum = 0
ModelNameColNum = 1
ApiNameColNum = 2
UrlColNum = 3
MethodColNum = 4
IsRunColNum = 5
DependentIdColNum = 6
DependentKeyColNum = 7
ResponseKeyColNum = 8
RequestDataColNum = 9
ExpectDataColNum = 10
ActualDataColNum = 11

header = {
    "x-sign": "Linshen100",
    "x-token": "anonymous_token",
    "content-type": "application/json"
}


def get_logger():
    CONF_LOG = "../config/logging.ini"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()

