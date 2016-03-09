from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, nullable=False)
    video_id = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    site = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    thumbnail_url = db.Column(db.Text, nullable=False)
    description_snippet = db.Column(db.Text, nullable=False)

    def __init__(self, status, video_id, url, site, title, description, thumbnail_url,
                 timestamp_creation, timestamp_publish, description_snippet, ):

        self.status = status
        self.video_id = video_id
        self.url = url
        self.site = site
        self.title = title
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.timestamp_creation = timestamp_creation
        self.timestamp_publish = timestamp_publish
        self.description_snippet = description_snippet


class VideosSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    # add validate=not_blank in required fields
    id = fields.UUID(attribute="uuid")

    status = fields.Integer(required=True)
    video_id = fields.String(validate=not_blank)
    url = fields.Url(validate=not_blank)
    site = fields.String(validate=not_blank)
    title = fields.String(validate=not_blank)
    description = fields.String(validate=not_blank)
    thumbnail_url = fields.Url(validate=not_blank)
    description_snippet = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/videos/"
        else:
            self_link = "/videos/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'videos'
        strict = True
