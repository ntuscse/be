from os.path import join, dirname
from fastapi.openapi.utils import get_openapi
import json
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '..', '.test.env'))

from be.docs import app

with open('openapi.json', 'w') as f:
    json.dump(get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
        # openapi_prefix=app.openapi_prefix,
    ), f)
