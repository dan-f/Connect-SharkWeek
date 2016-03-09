from flask import Blueprint
from app.news.models import News, NewsSchema
from flask_restful import Api, Resource


news = Blueprint('news', __name__)
# http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
# https://github.com/marshmallow-code/marshmallow-jsonapi
schema = NewsSchema(strict=True)
api = Api(news)


# News
class ListNews(Resource):

    def get(self):
        news_query = News.query.all()
        results = schema.dump(news_query, many=True).data
        return results


class GetNews(Resource):

    def get(self, id):
        news_query = News.query.get_or_404(id)
        result = schema.dump(news_query).data
        return result


api.add_resource(ListNews, '.json')
api.add_resource(GetNews, '/<int:id>.json')
