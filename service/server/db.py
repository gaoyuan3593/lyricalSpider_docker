#! /usr/bin/python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from service.db.model.m_db import DataSource
from service.utils.yaml_tool import get_by_name_yaml

conf = get_by_name_yaml('mysql')
engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
    conf['user'],
    conf['password'],
    conf['host'],
    conf['port'],
    conf['database']), convert_unicode=True, pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         bind=engine))
