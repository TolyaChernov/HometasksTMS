from peewee import *

db = SqliteDatabase('chinook.db')


class BaseModel(Model):
    class Meta:
        database = db


class Albums(BaseModel):
    AlbumId = AutoField()
    Title = CharField()


class Tracks(BaseModel):
    AlbumId = AutoField()
    Name = CharField()


# Функция вывода треков по альбому
def trek(word: str):
    for i in Tracks.select().where(Tracks.AlbumId == Albums.get(Albums.Title == word)):
        print(i.Name)
    print(word)


word_1: str = input("Введите название альбома: ")

trek(word_1)

db.close()

