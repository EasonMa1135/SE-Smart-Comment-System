from datetime import datetime, timedelta
from flask import Blueprint
from flask import request, make_response
from apps import db
from apps.orm import *
from flask_jwt_extended import jwt_required, get_jwt_identity

other_blue = Blueprint('others', __name__, url_prefix='/other')
# TODO