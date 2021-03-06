#! /usr/bin/python3
# -*- coding: utf-8 -*-
from flask import request, jsonify

from service.api.utils import resp_ok, resp_404
from service.api.utils.ds_utils import get_data_source_with_service, search_news_result
from service.server.main import application as app
from service.utils import get_module_from_service
from service.api.utils.request_tools import get_request_data


@app.errorhandler(404)
def not_found(error):
    return resp_404()


@app.route('/lyrical/<service_type>', methods=['GET', 'POST'])
def get_result(service_type):
    ds = get_data_source_with_service(service_type)
    handler = get_module_from_service(service_type, ds.handler)
    data = get_request_data(request)
    obj = handler.get_handler(data)
    result = obj.query()
    return resp_ok(result)


@app.route('/lyrical/monitor/search_news', methods=['GET'])
def get_monitor_news():
    data = get_request_data(request)
    result_list = search_news_result(data)
    if result_list:
        result = dict(
            status=200,
            msg="success",
            result=[dict(news_name=data.news_name,
                         website=data.website) for data in result_list]
        )
        return resp_ok(result)
    else:
        return resp_ok(dict(
            status=200,
            msg="未查询到结果"))


@app.route('/lyrical/monitor/paper', methods=['GET'])
def get_monitor_paper(service_type):
    ds = get_data_source_with_service(service_type)
    handler = get_module_from_service(service_type, ds.handler)
    data = get_request_data(request)
    obj = handler.get_handler(data)
    result = obj.query()
    return resp_ok(result)
