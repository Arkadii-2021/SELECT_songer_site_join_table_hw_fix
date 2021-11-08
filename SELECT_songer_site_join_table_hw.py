import psycopg2
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql+psycopg2://songer:123@localhost:5432/play_list')
connection = engine.connect()


def sel_1():
    print(str('количество исполнителей в каждом жанре').upper())
    select_1 = connection.execute("""SELECT COUNT (DISTINCT artist_name), g.genre_name FROM artist art
    JOIN genre_artist ga ON art.artist_id = ga.id
    JOIN genre g ON g.genre_id = ga.genre_id
    GROUP BY g.genre_name;
    """).fetchall()

    for artist_genre in select_1:
        print(f'{artist_genre[0]} artist in genre {artist_genre[1]}')
    print('\n')


# количество треков, вошедших в альбомы 2019-2020 годов
def sel_2():
    select_2 = connection.execute("""SELECT COUNT (t.name_track) FROM album a
    JOIN track t ON t.track_id_is_album = a.id_album
    WHERE year_of_issue IN (2019, 2020)
    """).fetchall()

    select_2 = list(select_2[0])
    print(str("Количество треков, вошедших в альбомы 2019-2020 годов:").upper(), int(select_2[0]), "\n")


def sel_3():
    print(str('средняя продолжительность треков по каждому альбому').upper())
    select_3 = connection.execute("""SELECT a.album_name, ROUND(AVG(t.track_duration)) FROM album a
    JOIN track t ON t.track_id_is_album = a.id_album
    GROUP BY a.album_name;
    """).fetchall()

    for tracks_duration in select_3:
        print(f'В альбоме "{tracks_duration[0]}" средняя продолжительность треков: {tracks_duration[1]} сек.')
    print('\n')


def sel_4():
    print(str(f'все исполнители, которые не выпустили альбомы в 2020 году').upper())
    select_4 = connection.execute("""SELECT DISTINCT a.artist_name FROM artist a 
    WHERE a.artist_name NOT IN (
    SELECT DISTINCT a.artist_name FROM artist a 
    LEFT JOIN artist_album aa ON a.artist_id = aa.id_artist
    LEFT JOIN album alb ON alb.id_album = aa.id_album
    WHERE alb.year_of_issue = 2020)
    ORDER BY a.artist_name;
    """).fetchall()

    n = 0
    for artist in select_4:
        n += 1
        print(f'{n}. {artist[0]}')
    print('\n')


def sel_5():
    print(str(f'названия сборников, в которых присутствует конкретный исполнитель').upper())
    select_5 = connection.execute("""SELECT DISTINCT c.collection_name, art.artist_name FROM collection_track ct
    JOIN collection c ON ct.collection_id = c.collection_id
    JOIN track t ON ct.track_id = t.track_id
    JOIN artist art ON t.artist_id = art.artist_id
    WHERE artist_name IN ('Звонкий');
     """).fetchall()

    print(f'Исполнитель "{str(select_5[0][1]).upper()}" входит в следующие сборники:')
    for col in select_5:
        print(f'--> {col[0]}')
    print('\n')


def sel_6():
    print(str(f'название альбомов, в которых присутствуют исполнители более 1 жанра').upper())
    select_6 = connection.execute("""SELECT a.album_name, art.artist_name, COUNT (DISTINCT ga.genre_id) FROM artist_album ab
    JOIN album a ON ab.id_album = a.id_album
    JOIN artist art ON ab.id_artist = art.artist_id
    JOIN genre_artist ga ON art.artist_id = ga.artist_id
    GROUP BY art.artist_name, a.album_name
    HAVING COUNT (DISTINCT ga.genre_id) > 1
    ORDER BY a.album_name;
    """).fetchall()

    for artist_genre in select_6:
        print(f'--> В альбоме "{str(artist_genre[0]).upper()}" у исполнителя "{str(artist_genre[1]).upper()}" есть {artist_genre[2]} жанра')
    print('\n')


def sel_7():
    print(str(f'наименование треков, которые не входят в сборники').upper())
    select_7 = connection.execute("""SELECT name_track FROM track
    WHERE track_id_is_album IS NULL
    ORDER BY name_track;
    """).fetchall()

    print("Следующие треки, которых нет в сборниках:")
    for tracks in select_7:
        print(f'--> {tracks[0]}')
    print('\n')


def sel_8():
    print(str(f'Исполнители, написавшего самый короткий по продолжительности трек').upper())
    select_8 = connection.execute("""SELECT artist_name, t.name_track, t.track_duration FROM track t
    JOIN artist a ON a.artist_id = t.artist_id
    WHERE t.track_duration = (SELECT MIN(t.track_duration) FROM track t)
    """).fetchall()

    for artists in select_8:
        print(f'--> "{artists[0]}" с треком "{artists[1]}" имеет наименьшую продолжительность - {artists[2]} секунд')
    print('\n')


def sel_9():
    print(str(f'название альбомов, содержащих наименьшее количество треков').upper())
    select_9 = connection.execute("""SELECT album_name Album, COUNT(Track.name_track) Track_count FROM Album 
    JOIN Track ON Album.id_album = Track.track_id_is_album
    GROUP BY album_name
    HAVING COUNT(Track.name_track) = (
    SELECT COUNT(Track.name_track) FROM Album
    JOIN Track ON Album.id_album = Track.track_id_is_album
    GROUP BY Album.album_name
    ORDER BY COUNT(Track.name_track)
    LIMIT 1);
    """).fetchall()

    for albums in select_9:
        print(f'--> {albums[0]}')
    print('\n')

sel_1()
sel_2()
sel_3()
sel_4()
sel_5()
sel_6()
sel_7()
sel_8()
sel_9()
