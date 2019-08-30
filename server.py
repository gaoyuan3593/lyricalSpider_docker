#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service.server.main import application as app

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host='127.0.0.1', port=8002)
