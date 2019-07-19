#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def get_module_obj_by_name(module_name, sub_module_name):
    parts = sub_module_name.split('.')
    sub_module_name = '%s.%s' % (module_name, parts[-1])
    try:
        module_obj = sys.modules[sub_module_name]
    except KeyError:
        __import__(sub_module_name)
        module_obj = sys.modules[sub_module_name]

    return module_obj


def get_module_from_service(service_type, handler):
    from service.config import SERVICE_MODULE_PACKAGE

    return get_module_obj_by_name('{}.{}'.format(SERVICE_MODULE_PACKAGE, service_type), handler)
