#! /usr/bin/python3
# -*- coding: utf-8 -*-


def generate_sig(endpoint, params=None, secret=None):
    import hmac
    from hashlib import sha256
    sig = endpoint
    if params:
        for key in sorted(params.keys()):
            sig += '|{}={}'.format(key, params[key])
    return hmac.new(secret.encode('utf-8'), sig.encode('utf-8'), sha256).hexdigest()


if __name__ == '__main__':
    endpoint = "/pandora/bank_card?no=6217731401216680"
    secret = "0703c93d739bf141a9906400da627f9f"
    sign = generate_sig(endpoint=endpoint, secret=secret)
    print(sign)
