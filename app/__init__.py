from flask import Flask, jsonify, abort, make_response
from flask.ext.sqlalchemy import SQLAlchemy


# http://flask.pocoo.org/docs/0.10/patterns/appfactories/
def create_app(config_filename):
    app = Flask(__name__, static_folder='templates/static')
    app.config.from_object(config_filename)

    # Init Flask-SQLAlchemy
    db = SQLAlchemy()
    db.init_app(app)

    # Blueprints
    from app.articles.views import articles
    app.register_blueprint(articles, url_prefix='/api/v1/articles')
    from app.news.views import news
    app.register_blueprint(news, url_prefix='/api/v1/news')
    from app.videos.views import videos
    app.register_blueprint(videos, url_prefix='/api/v1/videos')

    @app.route('/newsfeed', methods=['GET'])
    def get_newsfeed():
        return jsonify({'newsfeed': []})

    @app.route('/newsfeed/<int:newsfeed_id>', methods=['GET'])
    def get_news_item(newsfeed_id):
        news_item = []
        if len(news_item) == 0:
            abort(404)
        return jsonify({'news_item': news_item[0]})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app
