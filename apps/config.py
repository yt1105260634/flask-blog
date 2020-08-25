import os

base_dir = os.path.abspath(os.path.dirname(__file__))
# 通用配置
class Config(object):

    SECRET_KEY = 'XXXXXXX'
    # 使用本地的静态文件bootstrap
    BOOTSTRAP_SERVE_LOCAL = True

    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'yt1105260634@163.com'
    MAIL_PASSWORD = 'BBCRDQSCLXAOYHPA'


# 开发环境
class DevelopmentConfig(Config):
    # 数据库的配置变量
    HOSTNAME = '49.235.198.160'
    PORT = '3306'
    DATABASE = 'flask0820'
    USERNAME = 'root'
    PASSWORD = 'Yt7336046.'

    DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(username=USERNAME,
                                                                                               password=PASSWORD,
                                                                                               host=HOSTNAME, port=PORT,
                                                                                               db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'testing.sqlite')


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'product.sqlite')


config = {
    'default': DevelopmentConfig,
    'product': ProductionConfig,
    'test': TestingConfig,
}


