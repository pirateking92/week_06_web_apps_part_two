from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repo = ArtistRepository(db_connection)

    artists = repo.all()

    assert artists == [
        Artist(1, "Bloc Party", "Indie"),
        Artist(2, "Men I Trust", "Dream Pop")
    ]

def test_add_artist(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repo = ArtistRepository(db_connection)

    repo.add(Artist(None, "Twice", "K-pop"))
    result = repo.all()

    print(result)

    assert result == [
        Artist(1, "Bloc Party", "Indie"),
        Artist(2, "Men I Trust", "Dream Pop"),
        Artist(3, "Twice", "K-pop")
    ]

def test_get_one_artist(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repo = ArtistRepository(db_connection)

    result = repo.get(1)
    print(result)
    assert result == Artist(1, "Bloc Party", "Indie")
