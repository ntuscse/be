from fastapi import FastAPI
from mangum import Mangum
from be.api.v1.endpoints.products.get import router as v1_endpoints_products_get
from be.api.v1.endpoints.product_categories.get import router as v1_endpoints_product_categories_get
from be.api.v1.endpoints.product_categories.post import router as v1_endpoints_product_categories_post
from be.api.v1.endpoints.product_categories.delete import router as v1_endpoints_product_categories_delete


app = FastAPI()

app.include_router(v1_endpoints_products_get)

app.include_router(v1_endpoints_product_categories_get)
app.include_router(v1_endpoints_product_categories_post)
app.include_router(v1_endpoints_product_categories_delete)

handler = Mangum(app)
