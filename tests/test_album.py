from lib.album import Album
"""
Album constructs with 
an id, title, release year and artist id
"""
def test_album_constructs():
    album = Album(1, "Silent Alarm", 2005, 1)
    assert album.id == 1
    assert album.title == "Silent Alarm"
    assert album.release_year == 2005
    assert album.artist_id == 1

def test_albums_format_nicely():
    album = Album(1, "Silent Alarm", 2005, 1)
    assert str(album) == "Album(1, Silent Alarm, 2005, 1)"

def test_albums_are_equal():
    album1 = Album(1, "Silent Alarm", 2005, 1)
    album2 = Album(1, "Silent Alarm", 2005, 1)
    print(album1)
    print(album2)
    assert album1 == album2