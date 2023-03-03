from marshmallow import Schema, fields

from data_base import db


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


class PostSchema(Schema):
    pk = fields.Int(dump_only=True)
    poster_name = fields.Str()
    poster_avatar = fields.Str()
    pic = fields.Str()
    content = fields.Str()
    views_count = fields.Int()
    likes_count = fields.Int()
    commtnt_count = fields.Int()


class Comment(db.Model):
    __tablename__ = "comment"

    post_id = db.Column(db.Integer, db.ForeignKey("post.pk"))
    post = db.relationship("Post")
    commenter_name = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(256))
    pk = db.Column(db.Integer, primary_key=True)


class CommentSchema(Schema):
    post_id = fields.Int()
    commenter_name = fields.Str()
    comment = fields.Str()
    pk = fields.Int(dump_only=True)
