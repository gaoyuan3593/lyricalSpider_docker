#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os


def get_absolute_cur_path(f):
    return os.path.split(os.path.realpath(f))[0]


def get_absolute_parent_path(cur_file_or_path):
    if not os.path.isdir(cur_file_or_path):
        return get_absolute_cur_path(cur_file_or_path)

    return os.path.dirname(cur_file_or_path)


def get_js_cur_path():
    return os.path.split(os.path.realpath(__file__))[0]
