import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app: Flask = Flask(__name__)
config = Config()
app.config.from_object(config)
app.url_map.strict_slashes = False
app.app_context().push()
db = SQLAlchemy()
db.init_app(app)


class Post(db.Model):
    __tablename__ = "post"

    pk = db.Column(db.Integer, primary_key=True)
    poster_name = db.Column(db.String(100), nullable=False)
    poster_avatar = db.Column(db.String(256))
    pic = db.Column(db.String(256))
    content = db.Column(db.Text)
    views_count = db.Column(db.Integer)
    likes_count = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)


with open('data/posts.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

list_post = []
for dict_ in data:
    list_post.append(Post(**dict_))


class Comment(db.Model):
    __tablename__ = "comment"

    post_id = db.Column(db.Integer)
    commenter_name = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(256))
    pk = db.Column(db.Integer, primary_key=True)



with open('data/comments.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

list_comment = []
for dict_ in data:
    list_comment.append(Comment(**dict_))


db.drop_all()
db.create_all()

with db.session.begin():
    db.session.add_all(list_comment)
    db.session.commit()

data_post = list_post
for item in data_post:
    item.comment_count = len(db.session.query(Comment).filter(Comment.post_id == item.pk).all())

db.session.add_all(list_post)
db.session.commit()
