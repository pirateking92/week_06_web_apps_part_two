import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums = repo.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/albums/<id>', methods=['GET'])
def get_an_album(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = repo.get(id)
    artist_id = album.artist_id
    artist_repo = ArtistRepository(connection)
    artist = artist_repo.get(artist_id)
    return render_template('albums/show.html', album=album, artist_name=artist)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()
    return render_template('artists/show_artists.html', artists=artists)

@app.route('/artists/<id>', methods=['GET'])
def get_an_artist(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    album = repo.get(id)
    artist_id = album.artist_id
    artist_repo = ArtistRepository(connection)
    artist = artist_repo.get(artist_id)
    return render_template('artists/show_one_artist.html', album=album, artist_name=artist)


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
