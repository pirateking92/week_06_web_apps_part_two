from lib.artist import Artist

"""
Artist constructs
id, name, genre
"""

def test_artist_constructs():
    artist = Artist(1, "Bloc Party", "Indie")
    assert artist.id == 1
    assert artist.name == "Bloc Party"
    assert artist.genre == "Indie"

def test_artist_formats_nicely():
    artist = Artist(1, "Bloc Party", "Indie")
    assert str(artist) == "Artist(1, Bloc Party, Indie)"

def test_artists_are_equal():
    artist1 = Artist(1, "Bloc Party", "Indie")
    artist2 = Artist(1, "Bloc Party", "Indie")
    assert artist1 ==  artist2