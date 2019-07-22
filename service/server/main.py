#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask
#from flask_cache import Cache
from service import ENABLE_DEBUG_MODE


application = Flask(__name__)
application.secret_key = 'XPXu04w-(exW5lm`JT3c'
application.debug = ENABLE_DEBUG_MODE

#cache = Cache(application)


from service.api import base_service , error_handler
