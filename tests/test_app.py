from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
    
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Silent Alarm\nReleased: 2005\n",
        "Oncle Jazz\nReleased: 2019"
    ])

def test_get_an_album_with_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text([
        "Release year: 2005\nArtist: Bloc Party"
    ])

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Silent Alarm'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Silent Alarm")

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web.sql")
    page.goto(f"http://{test_web_address}/artists")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Bloc Party\nGenre: Indie\n",
        "Men I Trust\nGenre: Dream Pop"
    ])

def test_get_one_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text([
        "Albums: Silent Alarm\nGenre: Indie"
    ])

def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Bloc Party'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Bloc Party")
