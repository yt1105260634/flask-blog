# 导入类库

from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


# 实例化对象

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


# 封装函数  完成初始化

def config_extensions(app):
    bootstrap.init_app(app=app)
    mail.init_app(app=app)
    db.init_app(app=app)