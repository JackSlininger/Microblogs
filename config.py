WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-cannot-and-will-not-know'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
