from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repo = AlbumRepository(db_connection)

    albums = repo.all()

    assert albums == [
        Album(1, "Silent Alarm", 2005, 1),
        Album(2, "Oncle Jazz", 2019, 2)
    ]

def test_add_album(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repo = AlbumRepository(db_connection)

    repo.add(Album(None, "With You", 2024, 3))
    result = repo.all()

    print(result)

    assert result == [
        Album(1, "Silent Alarm", 2005, 1),
        Album(2, "Oncle Jazz", 2019, 2),
        Album(3, "With You", 2024, 3)
    ]

def test_get_one_album(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repo = AlbumRepository(db_connection)

    result = repo.get(1)
    print(result)
    assert result == Album(1, "Silent Alarm", 2005, 1)