from mangum import Mangum

from be.root import app

handler = Mangum(app)
