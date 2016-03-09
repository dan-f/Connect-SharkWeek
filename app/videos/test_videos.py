# http://werkzeug.pocoo.org/docs/0.11/test/#werkzeug.test.Client
# http://flask.pocoo.org/docs/0.10/api/#test-client

import unittest
import os
import sys
import json

from app import create_app

# Add app path to module path
sys.path.append(os.path.dirname(os.path.realpath(__file__).rsplit('/', 2)[0]))

app = create_app('config')
add_data = """{
  "data": {
    "attributes":

    {"site": "foo",
    "url": "foo",
    "description": "foo",
    "thumbnail_url": "foo",
    "status": 35678, "title": "foo",
    "description_snippet": "foo",
    "video_id": "foo"}
         ,

    "type": "videos"
  }

}"""


class TestVideos(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_read(self):
        # TODO this is a placeholder, need to add data into the DB by mock or fixture.
        # request = self.app.get('/api/v1/videos.json')
        # dict = json.loads(request.data.decode('utf-8'))
        # id = dict['data'][0]['id']
        # assert request.status_code == 200
        pass

if __name__ == '__main__':
    unittest.main()
