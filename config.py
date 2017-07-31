# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.urandom(24)
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'charts.db')
    JSON_AS_ASCII = False

class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
