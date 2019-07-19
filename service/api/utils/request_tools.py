#! /usr/bin/python3
# -*- coding: utf-8 -*-


def get_request_data(request):
    data = request.args.to_dict()
    if not data:
        data = request.json or request.form.to_dict()
    return data
