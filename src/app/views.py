from sanic import text, redirect, request, HTTPResponse
from sanic_ext import render
from uuid import uuid4
from .models import Urls
from .config import Config


async def create_tb(request: request) -> None:
    """ create table if not exists """
    Urls.create_table()


async def redirecting(request: request, shorten: str) -> HTTPResponse:
    """ redirect user to the original link """
    data = Urls.select().where(Urls.shorten == shorten).first()
    return redirect(data.original) if data else redirect('/', status=301)


async def index(request: request) -> HTTPResponse:
    """ if the URL is new save and shorten it, else return shorten link """

    if request.method == 'POST':

        url = request.form.get('original')

        data = Urls.select().where(Urls.original == url).first()

        if data:
            shorten = data.shorten

        else:
            last = Urls.select().order_by(Urls.id.desc()).first()
            code = str(uuid4()).split('-')[0][:4]
            shorten = str(last.id) + code if last else code
            Urls(url, shorten).save()

        return text(f'shorten link is: {Config.DOMAIN.value}{str(shorten)}', status=200)
    return await render('./index.html', status=200)
