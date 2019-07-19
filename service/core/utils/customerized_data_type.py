#! /usr/bin/python3
# -*- coding: utf-8 -*-


def enum(**named_values):
    return type('Enum', (), named_values)



