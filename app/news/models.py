from marshmallow_jsonapi import Schema, fields
from marshmallow import validate, pre_dump
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, nullable=False)
    news_id = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    news_type = db.Column(db.Text, nullable=False)
    site = db.Column(db.Text, nullable=False)
    lang = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text, nullable=False)
    news_category = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    body_markdown = db.Column(db.Text, nullable=False)

    def __init__(self, status, news_id, timestamp_creation, timestamp_publish, title, news_type,
                 site, lang, excerpt, news_category, url, image_url, body, body_markdown, ):

        self.status = status
        self.news_id = news_id
        self.timestamp_creation = timestamp_creation
        self.timestamp_publish = timestamp_publish
        self.title = title
        self.news_type = news_type
        self.site = site
        self.lang = lang
        self.excerpt = excerpt
        self.news_category = news_category
        self.url = url
        self.image_url = image_url
        self.body = body
        self.body_markdown = body_markdown


class NewsSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    # add validate=not_blank in required fields
    id = fields.UUID(attribute="uuid")
    title = fields.String(validate=not_blank)
    body_markdown = fields.String(validate=not_blank)
    excerpt = fields.String(validate=not_blank)
    timestamp_publish = fields.DateTime("%Y-%m-%dT%H:%M:%S+00:00")
    url = fields.Url(validate=not_blank)
    image_url = fields.String(validate=not_blank)
    lang = fields.String(validate=not_blank)

    # status = fields.Integer(required=True)
    # news_id = fields.String(validate=not_blank)
    # news_type = fields.String(validate=not_blank)
    # site = fields.String(validate=not_blank)
    # news_category = fields.String(validate=not_blank)
    # body = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/news/"
        else:
            self_link = "/news/{}".format(data['id'])
        return {'self': self_link}

    @pre_dump
    def empty_image_url_to_none(self, data):
        if not data.image_url:
            data.image_url = None
        return data

    class Meta:
        type_ = 'news'
        strict = True
