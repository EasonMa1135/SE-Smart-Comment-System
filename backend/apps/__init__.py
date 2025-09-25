from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig, ProductionConfig

db = SQLAlchemy()
jwt = JWTManager()

from .views import user_blue, other_blue

def create_app():
    # 构建 app
    my_app = Flask(__name__)
    # app 加载配置
    my_app.config.from_object(ProductionConfig)
    # app 创建数据库
    db.init_app(my_app)
    # app 创建 jwt
    jwt.init_app(my_app)
    # 注册蓝图
    my_app.register_blueprint(user_blue)
    my_app.register_blueprint(other_blue)
    # TODO
    
    return my_app
