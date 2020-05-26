#! /usr/bin/python3
# -*- coding: utf-8 -*-


def generate_seq_no():
    import hashlib
    import uuid
    import os
    seq_no = hashlib.md5(('%s-%s' % (os.getpid(), str(uuid.uuid1()))).encode('utf-8')).hexdigest()
    return seq_no
