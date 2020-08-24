# 通用配置
class Config(object):
    # 使用本地的静态文件bootstrap
    BOOTSTRAP_SERVE_LOCAL = True


# 开发环境
class DevelopmentConfig(Config):
    pass


# 开发环境
class TestingConfig(Config):
    pass


# 开发环境
class ProductionConfig(Config):
    pass


config = {
    'default': DevelopmentConfig,
    'product': ProductionConfig,
    'test': TestingConfig,
}
