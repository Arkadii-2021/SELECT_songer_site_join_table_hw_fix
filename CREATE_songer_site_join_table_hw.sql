create user songer_site with password '123';
create database songer_site_playlist_DB;
alter database songer_site_playlist_DB owner to songer_site;

create table if not exists Genre (
	genre_id serial primary key,
	genre_name varchar(40) unique
);
create table if not exists Artist (
	artist_id serial primary key,
	artist_name varchar(40)
);
create table if not exists Genre_artist (
	ID serial primary key,
	genre_id integer not null references Genre(genre_id),
	artist_id integer not null references Artist(artist_id)
);
create table if not exists Album (
	id_album serial primary key,
	album_name text,
	year_of_issue integer check(year_of_issue > 0)
);
create table if not exists Artist_album (
	ID serial primary key,
	id_album integer not null references Album(id_album),
	id_artist integer not null references Artist(artist_id)
);
create table if not exists Track (
	id serial primary key,
	track_id integer unique,
	track_id_is_album integer references Album(id_album),
	name_track text unique,
	track_duration numeric check (track_duration > 0),
	genre_id integer references Genre(genre_id),
	artist_id integer references artist(artist_id)
);
create table if not exists Collection (
	collection_id serial primary key,
	collection_name varchar(40) unique,
	year_of_issue integer check(year_of_issue > 0)
);
create table if not exists Collection_track (
	id serial primary key,
	collection_id integer not null references Collection(collection_id),
	track_id integer not null references Track(track_id)
);
