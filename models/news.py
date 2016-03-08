from __future__ import generators
import psycopg2
import psycopg2.extras
import yaml
import model
from marshmallow import pre_dump
from marshmallow_jsonapi import Schema, fields


class NewsProvider (model.Provider):
    table_name = "news"

    def exists(self, uuid):
        """ Returns True if record with uuid exists """
        return self.read(uuid) is not None

    def exists_by_news_id(self, news_id):
        """ Returns True if record with news_id exists """
        return self.read_by_news_id(news_id) is not None

    def exists_by_title_news_type(self, title, news_type):
        """ Returns True if record with title and news_type exists """
        return self.read_by_title_news_type(title, news_type) is not None

    def make_model(self, props):
        return News(props)

    def get_all(self):
        with self.get_db_cursor() as cur:
            cur.execute("SELECT * FROM news ORDER BY timestamp_publish DESC")
            res = cur.fetchall()
            returns = []
            for record in res:
                if record is not None:
                    returns.append(News(record))
            return returns

    def get_all_languages(self):
        with self.get_db_cursor() as cur:
            cur.execute("SELECT DISTINCT lang FROM news", ())
            return map(lambda x: x['lang'], cur)

    def get_all_sites(self):
        with self.get_db_cursor() as cur:
            cur.execute("SELECT DISTINCT site FROM news", ())
            return map(lambda x: x['site'], cur)

    def read(self, uuid):
        with self.get_db_cursor() as cur:
            cur.execute("SELECT * FROM news WHERE uuid = (%s)", (uuid,))
            res = cur.fetchone()

            if res is not None:
                return News(res)
            else:
                return None

    def read_by_news_id(self, news_id):
        with self.get_db_cursor() as cur:
            cur.execute("SELECT * FROM news WHERE news_id = (%s)", (news_id,))
            res = cur.fetchone()

            if res is not None:
                return News(res)
            else:
                return None

    def read_by_title_news_type(self, title, news_type):
        with self.get_db_cursor() as cur:
            cur.execute("SELECT * FROM news WHERE title = (%s) AND news_type = (%s)", (title, news_type))
            res = cur.fetchone()

            if res is not None:
                return News(res)
            else:
                return None


class News (model.Model):
    object_type = 'news'


class NewsSchema(Schema):
    id = fields.UUID(attribute="uuid")
    title = fields.Str()
    body_markdown = fields.Str()
    excerpt = fields.Str()
    timestamp_publish = fields.DateTime("%Y-%m-%dT%H:%M:%S+00:00")
    url = fields.Url()
    image_url = fields.Url(allow_none=True)
    lang = fields.Str()

    @pre_dump
    def empty_image_url_to_none(self, data):
        if not data.image_url:
            data.image_url = None
        return data

    class Meta:
        type_ = "news"
        strict = True
