#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os

import yaml

from service.config import CONF_FILE_NAME
from service.config import CONF_PATH
from service.utils.file_sys import get_absolute_cur_path

FULL_PATH_CONF_FILE = '%s/%s' % (CONF_PATH, CONF_FILE_NAME)


def load_conf(fp=FULL_PATH_CONF_FILE):
    try:
        stream = open(fp, 'r')
    except Exception as e:
        default_yaml_file = get_absolute_cur_path(__file__) + os.sep + CONF_FILE_NAME
        stream = open(default_yaml_file, 'r')

    conf = yaml.load(stream)

    return conf


def get_by_name_yaml(name):
    conf = load_conf()
    return conf.get(name, None)


if __name__ == '__main__':
    load_conf()
    print(get_by_name_yaml('redis'))
