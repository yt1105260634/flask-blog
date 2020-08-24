from .mains import mains
from .users import _users
from .posts import _posts

# 蓝本的配置
DEFAULT_BLUEPRINT = (
    (mains, ''),
    (_users, '/users'),
    (_posts, '/posts'),
)


# 封装函数 完成蓝本的注册
def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=url_prefix)

