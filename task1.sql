create table if not exists genre (
	id serial primary key,
	genre_name varchar(70) not null unique
);
create table if not exists performer (
	id serial primary key,
	Nickname varchar(70) not null unique
);
create table if not exists GenrePerformer (
	genre_id integer references genre(id),
	performer_id integer references performer(id),
	constraint GenrePerformer_pk primary key (genre_id, performer_id)
);
create table if not exists album (
	id serial primary key,
	album_name varchar(70) not null unique,
	year_of_issue integer not null
);
create table if not exists AlbumPerformer (
	performer_id integer references performer(id),
	album_id integer references album(id),
	constraint AlbumPerformer_pk primary key (performer_id, album_id)
);
create table if not exists tracks (
	id serial primary key,
	track_name varchar(70) not null unique,
	duration integer not null,
	album_id integer references album(id)
);
create table if not exists compilation (
	id serial primary key,
	compilation_name varchar(70) not null unique,
	year_of_issue integer not null
);
create table if not exists CompilationTracks (
	compilation_id integer references compilation(id),
	tracks_id integer references tracks(id),
	constraint CompilationTracks_pk primary key (compilation_id, tracks_id)
);	