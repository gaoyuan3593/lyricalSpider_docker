#! /usr/bin/python3
# -*- coding: utf-8 -*-
from config import ENABLE_DEBUG_MODE

__version__ = '0.0.1'

import sys
import logbook

level = 'debug'
error_level = 'warning'
filename = '/home/gaoyuan/log/p.log'
error_filename = '/home/pandora/log/p_error.log'
format_string = '[{record.time:%Y-%m-%d %H:%M:%S.%f%z}][{record.level_name}]' \
                '[pid:{record.process}][{record.filename}:{record.lineno}]' \
                '[seq_no:{record.extra[seq_no]}]:{record.message}'
if ENABLE_DEBUG_MODE:
    handler = logbook.StreamHandler(sys.stdout, format_string=format_string, level=level.upper(), bubble=True)
    handler.push_application()
else:
    error_handler = logbook.RotatingFileHandler(error_filename, max_size=512 * 1024 * 1024, backup_count=7, bubble=True,
                                                format_string=format_string, level=error_level.upper())
    error_handler.push_application()
    handler = logbook.RotatingFileHandler(filename, max_size=512 * 1024 * 1024, backup_count=7, bubble=True,
                                          format_string=format_string, level=level.upper())
    handler.push_application()
logbook.set_datetime_format('local')
logger = logbook.Logger('nut')
