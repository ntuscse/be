import os
from os import makedirs
from os.path import join, dirname
from fastapi.openapi.utils import get_openapi
import json
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '..', '.test.env'))

from be.docs import app

filePath = join(dirname(__file__), '..', 'out', 'openapi.json')
makedirs(dirname(filePath), exist_ok=True)

base_api_server_url: str = os.getenv('BASE_API_SERVER_URL')

with open(filePath, 'w') as f:
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
        servers=[{"url": base_api_server_url}]
        # openapi_prefix=app.openapi_prefix,
    )

    openapi_schema["info"]["x-logo"] = {
        "url": "https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg"
    }

    json.dump(openapi_schema, f)
