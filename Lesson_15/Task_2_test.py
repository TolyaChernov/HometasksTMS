from peewee import *


db = SqliteDatabase ('Task_2_test.db')


class Albums(Model):
    album_id = PrimaryKeyField(unique=True)
    album_name = CharField()
    artist = CharField()

    class Meta:
        database = db


class Tracks(Model):
    track_id = PrimaryKeyField(unique=True)
    track_name = CharField()
    album_id = ForeignKeyField(Albums)

    class Meta:
        database = db



# Создание таблиц в БД
Albums.create_table()
Tracks.create_table()



# Очистка содержимого таблиц БД на случай повторного запуска при тестировании
for i in Tracks.select():
    i.delete_instance()

for j in Albums.select():
    j.delete_instance()



# Заполнение таблиц БД
album_dict={
    "Album_1": "Artist_1",
    "Album_2": "Artist_2",
    "Album_3": "Artist_3",
    "Album_4": "Artist_5",
    "Album_5": "Artist_2",
    "Album_6": "Artist_7",
    "Album_7": "Artist_8",
    "Album_8": "Artist_9",
    "Album_9": "Artist_10",
    "Album_10": "Artist_1"
    }

for key, value in album_dict.items():
    Albums(album_name=key, artist=value).save()

track_album1_dict={
    "Track_1.1": 1,
    "Track_2.1": 1,
    "Track_3.1": 1,
    "Track_4.1": 1,
    "Track_5.1": 1,
    "Track_6.1": 1,
    "Track_7.1": 1,
    "Track_8.1": 1,
    "Track_9.1": 1,
    "Track_10.1": 1,
    "Track_1.2": 2,
    "Track_2.2": 2,
    "Track_3.2": 2,
    "Track_4.2": 2,
    "Track_5.2": 2,
    "Track_6.2": 2,
    "Track_7.2": 2,
    "Track_8.2": 2,
    "Track_9.2": 2,
    "Track_10.2": 2,
    "Track_1.3": 3,
    "Track_2.3": 3,
    "Track_3.3": 3,
    "Track_4.3": 3,
    "Track_5.3": 3,
    "Track_6.3": 3,
    "Track_7.3": 3,
    "Track_8.3": 3,
    "Track_9.3": 3,
    "Track_10.3": 3,
    }

for key, value in track_album1_dict.items():
    #print (key, value)
    Tracks(track_name=key, album_id=value).save()



# Функция вывода треков по альбому
def trek(word: str):
    for i in Tracks.select().where(Tracks.album_id == Albums.get(Albums.album_name == word)):
        print (i.track_name)



word_1: str = input("Введите название альбома: ")

trek(word_1)

db.close()