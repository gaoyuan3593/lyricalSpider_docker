#! /usr/bin/python3
# -*- coding: utf-8 -*-


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d