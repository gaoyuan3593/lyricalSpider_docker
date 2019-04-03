#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service.server.main import cache


def ds_cache_delete():
    from service.api.utils.ds_utils import get_data_source
    cache.delete_memoized(get_data_source)