#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
