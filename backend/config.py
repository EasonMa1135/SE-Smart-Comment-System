import datetime
# 配置类基类
class BaseConfig(object):
    JWT_SECRET_KEY = "5682"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=60)

    # 数据库配置
    DIALCT = "mysql"
    DRITVER = "pymysql"
    HOST = 'localhost'
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "ufo-62418676" # TODO
    DBNAME = 'sc' # TODO

    SQLALCHEMY_DATABASE_URI = f"{DIALCT}+{DRITVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

# 生产环境配置类
class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

# 开发模式配置类
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False