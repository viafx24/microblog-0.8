import os
basedir = os.path.abspath(os.path.dirname(__file__))

#another way to get the reference to the postgresql db:
#POSTGRES = {
#    'user': 'postgres',
#    'pw': 'cardinal',
#    'db': 'test-load-heroku-backup',
#    'host': 'localhost',
#    'port': '5432',
#}

#Local_PostgreSQL='postgresql://%(user)s:\
#%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

#print(Local_PostgreSQL) 
#then add Local_PostgreSQL in place of the line 26
#test-load-heroku-backupS

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '#5fbd9d}QE|c*i[Ysh8kCsjgf(jtIe'
    #previous variable for sqlite:
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:cardinal@localhost:5432/local-database-dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
