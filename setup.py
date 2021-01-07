#! /usr/bin/python3
# -*- coding: utf-8 -*-
import glob

from setuptools import setup, find_packages

setup(
    name='lyrcal-spider',
    version='1.0.0',
    license="BSD",
    description='nut spider micro service',
    author='#',
    author_email='#',
    url='#',
    include_package_data=True,
    package_data={'service': ['utils\js_data\*.js']},
    packages=find_packages("."),
    zip_safe=False,
    install_requires=[
        "beautifulsoup4==4.6.0",
        "elasticsearch>=6.0.0",
        "elasticsearch-dsl>=6.3.1",
        "APScheduler==3.6.0",
        "bs4==0.0.1",
        "fake-useragent==0.1.10",
        "Flask==0.12.4",
        "Flask-Bcrypt==0.7.1",
        "Flask-Cache==0.13.1",
        "flask-restplus==0.10.1",
        "Flask-SQLAlchemy==2.3.2",
        "gunicorn==19.7.1",
        "Jinja2==2.10",
        "Logbook==1.3.3",
        "lxml==4.6.2",
        "PyYAML==3.12",
        "redis==2.10.6",
        "requests==2.18.4",
        "crypto==1.4.1",
        "urllib3==1.22",
        "celery==4.3.0",
        "pymongo==3.7.2",
        "pandas==0.24.2",
        "pillow==6.0.0",
        "rsa==4.0",
        "jieba==0.39",
    ],
    data_files=[
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ]

)
