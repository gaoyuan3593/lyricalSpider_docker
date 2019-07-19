#! /usr/bin/python3
# -*- coding: utf-8 -*-
from service.server.main import application as app


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)