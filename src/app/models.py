from peewee import SqliteDatabase
import peewee


class BaseModel(peewee.Model):
    """This is the base class that all models inherit from it"""

    class Meta:
        database = SqliteDatabase('app.db')


class Urls(BaseModel):
    id = peewee.AutoField()
    original = peewee.CharField(max_length=100)
    shorten = peewee.CharField()

    def __init__(self, original: str, shorten: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.original = original
        self.shorten = shorten
