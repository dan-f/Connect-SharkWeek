from flask import Blueprint
from app.videos.models import Videos, VideosSchema
from flask_restful import Api, Resource

videos = Blueprint('videos', __name__)
# http://marshmallow.readthedocs.org/en/latest/quickstart.html#declaring-schemas
# https://github.com/marshmallow-code/marshmallow-jsonapi
schema = VideosSchema(strict=True)
api = Api(videos)


# Videos
class ListVideos(Resource):

    def get(self):
        videos_query = Videos.query.all()
        results = schema.dump(videos_query, many=True).data
        return results


class GetVideo(Resource):

    def get(self, id):
        video_query = Videos.query.get_or_404(id)
        result = schema.dump(video_query).data
        return result

api.add_resource(ListVideos, '.json')
api.add_resource(GetVideo, '/<int:id>.json')
