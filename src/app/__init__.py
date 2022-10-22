import multiprocessing
from sanic import Sanic
from .config import Config
from .views import index, redirecting, create_tb


app = Sanic(__name__)
app.config.FORWARDED_SECRET = Config.SECRET.value
app.config["OAS_UI_DEFAULT"] = 'swagger'
app.static('/static', './static')

app.before_server_start(create_tb)
app.add_route(index, '/', methods=['GET', 'POST'])
app.add_route(redirecting, '/<shorten:str>')

# half of cpu power in multi-cores
count = multiprocessing.cpu_count()
workers = int(count / 2) if count >= 2 else 1
