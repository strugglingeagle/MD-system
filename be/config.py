import redis


class Config(object):
    """配置信息"""
    SECRET_KEY = "asdfghjkl;"

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root1234@127.0.0.1:3306/maleware"
    SQLALCHEMY_TRACK_MODIFICATION = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session 配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True   # 对 cookie 中的 session_id 进行隐藏
    PERMANENT_SESSION_LIFETIME = 86400  # 有效期，单位是秒
    # WTF_CSRF_CHECK_DEFAULT = False


class devConfig(Config):
    """开发模式配置信息"""
    DEBUG = True
    pass


class prodConfig(Config):
    """线上模式配置信息"""
    pass


config_map = {
    "develop": devConfig,
    "product": prodConfig
}
