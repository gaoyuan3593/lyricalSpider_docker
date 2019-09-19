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
    conf['database']), convert_unicode=True, pool_pre_ping=True, isolation_level='AUTOCOMMIT')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

if __name__ == '__main__':
    k = db_session.query(DataSource).filter(DataSource.service == "sina").first()
    print(k.handler)
