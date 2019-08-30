#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service import logger
#from service.server.main import cache


#@cache.memoize()
def get_data_source():
    from service.db.model.m_db import DataSource
    from service.server.db import db_session
    result = db_session.query(DataSource).all()
    return [item.json() for item in result]


def get_data_source_with_service(s):
    from service.server.db import db_session
    from service.db.model.m_db import DataSource
    k = db_session.query(DataSource).filter(DataSource.service == s).first()
    return k


def get_news_source_with_service(s):
    from service.server.db import db_session
    from service.db.model.m_db import NewsSource
    k = db_session.query(NewsSource).filter(NewsSource.website == s).first()
    return k


def add_data_source(data):
    from service.db.model.m_db import DataSource
    from service.server.db import db_session
    try:
        ds = DataSource(id=data.get('id', None),
                        name=data.get('name', None),
                        service=data.get('service', None),
                        handler=data.get('handler', None),
                        enabled=data.get('enabled', 1),
                        description=data.get('description', None)
                        )
        db_session.add(ds)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise IntoDbError()

    k = db_session.query(DataSource).filter(DataSource.id == int(data.get('id', None))).first().json()
    return k