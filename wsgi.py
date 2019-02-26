from gevent import monkey
monkey.patch_all()

from app import api
from gunicorn.app.base import Application


class MyApplication(Application):
    def load_config(self):
        self.load_config_from_module_name_or_filename("gunicorn_conf.py")


    def load(self):
        return api.app

if __name__ == '__main__':
    MyApplication().run()
