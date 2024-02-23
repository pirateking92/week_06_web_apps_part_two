DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artist_id_seq;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
); 

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
); 

INSERT INTO albums (title, release_year, artist_id) VALUES ('Silent Alarm', '2005', '1');
INSERT INTO albums (title, release_year, artist_id) VALUES ('Oncle Jazz', '2019', '2');
INSERT INTO artists (name, genre) VAlUES ('Bloc Party', 'Indie');
INSERT INTO artists (name, genre) VAlUES ('Men I Trust', 'Dream Pop')
