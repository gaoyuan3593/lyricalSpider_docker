#! /usr/bin/python3
# -*- coding: utf-8 -*-

from sqlalchemy import BigInteger
from sqlalchemy import Column, DateTime, String
from sqlalchemy import Index
from sqlalchemy import SmallInteger
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DataSource(Base):
    __tablename__ = 'data_source'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    service = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    handler = Column(String(50), nullable=True)
    enabled = Column(SmallInteger, nullable=False, server_default=text('1'))
    description = Column(String(200), nullable=True, server_default=text('description'))

    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"))

    __table_args__ = (Index('ix_data_source', 'name', 'service', 'handler', 'enabled'),)

    def short_json(self):
        return dict(
            id=self.id,
            name=self.name
        )

    def json(self):
        return dict(
            id=self.id,
            service=self.service,
            handler=self.handler,
            name=self.name,
            description=self.description,
            enabled=self.enabled,
            create_time=self.create_time,
            update_time=self.update_time
        )
