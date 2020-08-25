from apps import create_app
from flask_script import Manager

app = create_app('product')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
