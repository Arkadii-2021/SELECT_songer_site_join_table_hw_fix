import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://songer_site:123@localhost:5432/songer_site_playlist_DB')
connection = engine.connect()

music_genre = [
    'Поп', 'Рок', 'Хип-хоп', 'РЭП', 'R&B', 'Джаз',
    'Инструментальная музыка', 'Народная музыка',
    'Электро', 'Транс'
]

for genre_name in music_genre:
    connection.execute(f"""INSERT INTO Genre(genre_name)
    VALUES('{genre_name}');
""")

artist_data = [
    'Звонкий', 'Звонкий', 'Звонкий', 'Леша Свик', 'Maruv','Zivert', 'Zivert', 'Irish Woman',
    'Sylvering', 'Клава Кока', 'Dabro', 'Taylor Swift', 'Taylor Swift', 'beabadoobee',
    'Lil Uzi Vert', 'Paul van Dyk feat. Hemstock & Jennings', 'Armin vаn Buurеn fеаt. Susаnа',
    'Mitsky', 'Mitsky', 'James Blake', 'James Blake'
]

for artist_name in artist_data:
    connection.execute(f"""INSERT INTO Artist(artist_name)
    VALUES('{artist_name}');
""")

genre_artist = [
    (1, 4), (2, 4), (3, 5), (4, 1), (5, 1), (6, 1), (7, 1),
    (8, 8), (9, 8), (10, 1), (11, 4), (12, 2), (13, 2), (14, 1),
    (15, 1), (16, 10), (17, 10), (18, 1), (19, 1), (20, 1), (21, 1)
]

for data_genre_artist in genre_artist:
    connection.execute(f"""INSERT INTO genre_artist (artist_id, genre_id)
    VALUES({data_genre_artist[0]}, {data_genre_artist[1]});
""")

album = [('Мир моих иллюзий', 2019), ('Vinyl #1', 2019), ('Vinyl #2', 2019), ('Folklore', 2020),
    ('Fake it Flowers', 2020), ('Eternal Atake', 2020), ('Be the Cowboy', 2018),
    ('Assume Form', 2019), ('Other album - 2018', 2018), ('Other album - 2019', 2019),
    ('Other album - 2020', 2020), ('Other album - 2021', 2021), ('Other album - 2014', 2014)
]

for data_album_to_year in album:
    connection.execute(f"""INSERT INTO album (album_name, year_of_issue)
    VALUES('{data_album_to_year[0]}', {data_album_to_year[1]});
""")

data_artist_to_album = [
    (1, 1), (2, 1), (3, 1), (4, 3), (5, 9), (6, 2), (7, 3), (8, 13),
    (9, 13), (10, 11), (11, 11), (12, 4), (13, 4), (14, 5), (15, 6),
    (16, 10), (17, 10), (18, 7), (19, 7), (20, 8), (21, 8)
]

for artist_to_album in data_artist_to_album:
    connection.execute(f"""INSERT INTO artist_album (id_artist, id_album)
    VALUES({artist_to_album[0]}, {artist_to_album[1]});
""")

track_data_not_album = [    
    (5, 'Focus On Me', 153, 1, 5), (8, 'KoolSax', 305, 8, 8), (9, 'Cruel Summer', 150, 8, 9),
    (10, 'ЛА ЛА ЛА', 144, 1, 10), (11, 'Услышит весь район', 120, 4, 11),
    (13, 'The last great american dynasty', 211, 2, 13), (16, 'Nothing But You (UK Radio Edit)', 190, 10, 16),
    (17, 'Shivers (Original Mix)', 187, 10, 17),  (19, 'Old Friend', 91, 1, 19),
    (21, 'Cannot Believe The Way We Flow', 256, 1, 10, 21)
]

for td in track_data_not_album:
    connection.execute(f"""INSERT INTO track (track_id, name_track, track_duration, genre_id, artist_id)
    VALUES('{td[0]}', '{td[1]}', '{td[2]}', '{td[3]}', '{td[4]}');
""")

track_data_in_album = [
    (1, 'Из окон', 203, 4, 9, 1), (2, 'Голоса', 196, 4, 9, 2), (3, 'Падаем в небо', 155, 5, 9, 3), 
    (4, 'Малиновый свет', 184, 1, 9, 4), (6, 'Безболезненно', 203, 1, 2, 6), (7, 'Beverly Hills', 182, 1, 3, 7),
    (12, 'Cardigan', 215, 2, 4, 12), (14, 'Worth It', 188, 1, 5, 14), (15, 'Lil Uzi Vert', 189, 1, 6, 15),
    (18, 'Geyser', 134, 1, 7, 18), (20, 'Mile High', 188, 1, 8, 20)
]

for tda in track_data_in_album:
    connection.execute(f"""INSERT INTO track (track_id, name_track, track_duration, genre_id, track_id_is_album, artist_id)
    VALUES('{tda[0]}', '{tda[1]}', '{tda[2]}', '{tda[3]}', '{tda[4]}', '{tda[5]}');
""")

collection_data = [
    ('Hits 2019', 2019), ('Hits 2018', 2018), ('Autumn Music 2018', 2018), ('Hotel Deluxe Music Vol5', 2014),
    ('2020 vs 2021 главные русские хиты', 2020), ('Новые песни 2021', 2021), ('Popular 2020', 2020),
    ('VER11 CLASSIC VOCAL TRANCE', 2019)
]

for collection in collection_data:
    connection.execute(f"""INSERT INTO collection (collection_name, year_of_issue)
    VALUES('{collection[0]}', {collection[1]});
""")

collection_to_track = [
    (2, 1), (3, 2), (4, 3), (5, 3), (8, 4), (9, 4), (10, 5), (11, 6),
    (13, 7), (15, 7), (16, 8), (17, 8), (19, 2), (21, 1)
]

for cd in collection_to_track:
    connection.execute(f"""INSERT INTO collection_track (track_id, collection_id)
    VALUES('{cd[0]}', {cd[1]});
""")
