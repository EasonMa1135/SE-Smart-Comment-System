from apps import db
from datetime import datetime


class Course(db.Model):
    __tablename__ = 'Course'
    c_id = db.Column(db.Integer, primary_key=True, nullable=False)
    t_name = db.Column(db.String(255), nullable=False)
    c_code = db.Column(db.String(255), nullable=False)
    c_name = db.Column(db.String(255), nullable=False)
    c_credits = db.Column(db.Numeric(3, 1), nullable=False)
    c_category = db.Column(db.String(255), nullable=False)
    c_department = db.Column(db.String(255), nullable=False)
    

class Comment(db.Model):
    __tablename__ = 'Comment'
    com_id = db.Column(db.Integer, primary_key=True, nullable=False)
    c_id = db.Column(db.Integer, db.ForeignKey('Course.c_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    course = db.relationship('Course', backref='comments')
    
    
class TeacherComment(db.Model):
    __tablename__ = 'TeacherComment'
    tc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    