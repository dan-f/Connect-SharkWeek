from flask import Blueprint
from app.articles.models import Articles, ArticlesSchema
from flask_restful import Api, Resource

articles = Blueprint('articles', __name__)
# http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
# https://github.com/marshmallow-code/marshmallow-jsonapi
schema = ArticlesSchema(strict=True)
api = Api(articles)


# Articles
class ListArticles(Resource):

    def get(self):
        articles_query = Articles.query.all()
        results = schema.dump(articles_query, many=True).data
        return results


class GetArticle(Resource):

    def get(self, id):
        article_query = Articles.query.get_or_404(id)
        result = schema.dump(article_query).data
        return result


api.add_resource(ListArticles, '.json')
api.add_resource(GetArticle, '/<int:id>.json')
