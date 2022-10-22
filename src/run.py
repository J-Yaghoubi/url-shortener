from app import app, workers
from app.config import Config


if __name__ == '__main__':

    app.run(
        host=Config.HOST.value,
        port=Config.PORT.value,
        workers=workers,
        access_log=False,
        debug=False
    )
