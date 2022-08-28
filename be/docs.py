from mangum import Mangum
import os
from os.path import join, dirname
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '..', '.env.test'))
base_api_server_url: str = os.getenv('BASE_API_SERVER_URL')

from be.api.v1.endpoints.products.get import router as v1_products_get


from be.api.v1.endpoints.product_categories.get import (
    router as v1_product_categories_get,
)
from be.api.v1.endpoints.product_categories.post import (
    router as v1_product_categories_post,
)
from be.api.v1.endpoints.product_categories.delete import (
    router as v1_product_categories_delete,
)

from be.api.v1.endpoints.payments.intent.post import router as v1_payments_intent_post
from be.api.v1.endpoints.checkout.post import router as v1_checkout_post

tags_metadata = [
    {
        "name": "merchandise",
        "description": (
            "CRUD for merchandise products."
            "GET for all users, POST/DELETE/PATCH for admin users."
        ),
    },
]

app = FastAPI(
    title="NTU SCSE Site API Docs",
    description="![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(v1_products_get)

app.include_router(v1_product_categories_get)
app.include_router(v1_product_categories_post)
app.include_router(v1_product_categories_delete)

app.include_router(v1_payments_intent_post)
app.include_router(v1_checkout_post)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
        servers=[{"url": base_api_server_url}]
        # openapi_prefix=app.openapi_prefix,
    )
    # openapi_schema["info"]["x-logo"] = {
    #     "url": "https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg"
    # }

    app.openapi_schema = openapi_schema
    return openapi_schema


app.openapi = custom_openapi

handler = Mangum(app)
