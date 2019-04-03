# ! /usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import

__author__ = 'duwenbin'

from service import logger

from celery import Task, Celery
from service.utils.yaml_tool import get_by_name_yaml

conf = get_by_name_yaml('redis')

CELERY_BROKER_URL = 'redis://:%s@%s:%s/5' % (conf['password'], conf['host'], conf['port'])
CELERY_BACKEND_URL = 'redis://:%s@%s:%s/6' % (conf['password'], conf['host'], conf['port'])

app = Celery('PandoraTasks',
             broker=CELERY_BROKER_URL,
             backend=CELERY_BACKEND_URL,
             changes=dict(CELERY_ENABLE_UTC=True,
                          CELERY_ACKS_LATE=True,
                          CELERY_CREATE_MISSING_QUEUES=True,
                          CELERY_DEFAULT_QUEUE='pandora.service.tasks',
                          CELERYD_PREFETCH_MULTIPLIER=10,
                          BROKER_TRANSPORT_OPTIONS={
                              'visibility_timeout': 36000}),
             include=[
                 'service.celery.tasks'
             ])

app.config_from_object({
    'CELERYBEAT_SCHEDULE': {},
    'CELERY_TASK_RESULT_EXPIRES': 15,
    'CELERY_TIMEZONE': 'Asia/Shanghai',
    'CELERY_SERIALIZER': 'json',
    'CELERY_ACCEPT_CONTENT': ['json'],
    'CELERY_RESULT_SERIALIZER': 'json',
    'CELERYD_MAX_TASKS_PER_CHILD': 5,
})


class BaseTask(Task):
    _db_session = None

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        _args = dict(status=status, retval=retval, task_id=task_id)
        logger.info("Entering into after_return callback  {args: %s}" % _args)
        if self._db_session is not None:
            self._db_session.remove()
        if einfo:
            logger.exception(einfo)

    def on_success(self, retval, *args, **kwargs):
        logger.info("Entering into callback on_success...")
        super(BaseTask, self).on_success(retval, *args, **kwargs)
        logger.info("Return value %s" % retval)
        if retval:
            for token, reason in retval.failed.items():
                code, errmsg = reason
                logger.info('Device failed: %s, reason: %s', token, errmsg)

            for code, errmsg in retval.errors:
                logger.info('Error: %r', errmsg)

            if retval.needs_retry():
                self.retry()

    def on_failure(self, exc, task_id, *args, **kwargs):
        logger.info("Entering into callback on_failure..., and retry. {task_id: %s}" % task_id)
        logger.exception(exc)
        self.retry(countdown=60, exc=exc, max_retries=2)
