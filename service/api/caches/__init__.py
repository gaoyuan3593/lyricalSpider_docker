#! /usr/bin/python3
# -*- coding: utf-8 -*-


def delete_caches():
    from service.server.main import application as app
    from service import logger
    with app.app_context():
        from service.server.main import cache
        cache.clear()
        logger.info('clear all the cache!')
