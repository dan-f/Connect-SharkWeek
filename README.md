# Connect-SharkWeek
Public API for [Sharknado](https://github.com/Bernie-2016/Connect-Sharknado) using the [JSON API 1.0 Spec](http://jsonapi.org/)
[Newsfeed spec](https://github.com/Bernie-2016/Connect-Sharknado/issues/1)

#### Requirements
Stack is [marshmallow](https://github.com/marshmallow-code/marshmallow) and [marshmallow-jsonapi](https://github.com/marshmallow-code/marshmallow-jsonapi) for serialization to JSON API Spec.
[Flask](https://github.com/mitsuhiko/flask) for routing and output.

Install via pip:
```bash
pip install marshmallow marshmallow-jsonapi Flask pyYAML flask-marshmallow psycopg2
```
#### Sample config
Config file goes in ```/opt/bernie/config.yml``` (you can use the same config as [Sharknado](https://github.com/Bernie-2016/Connect-Sharknado) if you are running on the same box and db)
```yaml
postgresql:
    dbname: __postgres__
    dbuser: __user__
    dbpass: __pass__
    host: __host__
    port: 5432

flask:
    host: 127.0.0.1
```