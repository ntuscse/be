from fastapi import FastAPI
from mangum import Mangum
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

tags_metadata = [
    {
        "name": "merchandise",
        "description": (
            "CRUD for merchandise products."
            "GET for all users, POST/DELETE/PATCH for admin users."
        ),
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(v1_products_get)

app.include_router(v1_product_categories_get)
app.include_router(v1_product_categories_post)
app.include_router(v1_product_categories_delete)

handler = Mangum(app)
