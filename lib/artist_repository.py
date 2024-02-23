from lib.artist import Artist

class ArtistRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(
                row["id"], row["name"], row["genre"]
            )
            artists.append(item)
        return artists
    
    def add(self, artist):
        self._connection.execute('INSERT INTO artists(name, genre) VALUES( %s, %s)',[
            artist.name, artist.genre
        ])
        return None
    
    def get(self,id):
        rows = self._connection.execute('SELECT * from artists WHERE id = %s', [id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])