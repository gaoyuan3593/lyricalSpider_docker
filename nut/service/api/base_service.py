#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import request, jsonify

from service.api.utils import resp_ok, resp_404
from service.api.utils.ds_utils import get_data_source_with_service
from service.server.main import application as app
from service.utils import get_module_from_service
from service.api.utils.request_tools import get_request_data


@app.errorhandler(404)
def not_found(error):
    return resp_404()


@app.route('/lyrical/<service_type>', methods=['GET'])
def get_result(service_type):
    ds = get_data_source_with_service(service_type)
    handler = get_module_from_service(service_type, ds.handler)
    data = get_request_data(request)
    obj = handler.get_handler(data)
    result = obj.query()
    return resp_ok(result)