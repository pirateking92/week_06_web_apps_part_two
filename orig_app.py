import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

@app.route('/all', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    # return "\n".join([
    #     str(album) for album in repo.all()
    # ])
    render_template('all.html', all="'\n'.join([str(album) for album in repo.all()')")

@app.route('/add', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repo.add(album)
    return "Album added successfully"

@app.route('/all_artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    return "\n".join([
        str(artist) for artist in repo.all()
    ])

@app.route('/add_artist', methods=['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    artist = Artist(None, request.form['name'], request.form['genre'])
    artist = repo.add(artist)
    return "Artist added successfully"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

