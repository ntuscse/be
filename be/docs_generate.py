import os
from os import makedirs
from os.path import join, dirname
import json
from be.docs import app

filePath = join(dirname(__file__), '..', 'out', 'openapi.json')
makedirs(dirname(filePath), exist_ok=True)

base_api_server_url: str = os.getenv('BASE_API_SERVER_URL')

with open(filePath, 'w') as f:
    json.dump(app.openapi(), f)
