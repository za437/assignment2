import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.urandom(32) or "zack-Ali"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'zack.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
