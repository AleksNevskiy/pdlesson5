import sqlalchemy
import pandas as pd

def performers_in_genre(connection):
    sel = connection.execute("""SELECT genre_name, COUNT(performer_id) FROM genre g
                                    JOIN genreperformer gp ON g.id = gp.genre_id
                                    GROUP BY g.id;
                                    """).fetchall()
    return sel
def tracks_in_album_218_2020(connection):
    sel = connection.execute("""SELECT COUNT(t.id) FROM tracks t
                                    JOIN album a ON t.album_id = a.id
                                    WHERE a.year_of_issue BETWEEN 2018 AND 2020;
                                    """).fetchall()
    return sel
def avr_dur(connection):
    sel = connection.execute("""SELECT album_name, AVG(t.duration) FROM tracks t
                                    JOIN album a ON t.album_id = a.id
                                    GROUP BY a.id;
                                    """).fetchall()
    return sel
def not_in_2020(connection):
    sel = connection.execute("""SELECT nickname FROM performer p
                                    WHERE p.id NOT IN (
                                        SELECT performer_id FROM album a
                                            JOIN albumperformer ap ON a.id = ap.album_id
                                            WHERE year_of_issue = 2020);
                                    """).fetchall()
    return sel
def Metallica(connection):
    sel = connection.execute("""SELECT DISTINCT compilation_name FROM compilation c
                                    JOIN compilationtracks ct ON c.id = ct.compilation_id
                                    JOIN tracks t ON ct.compilation_id = t.id
                                    JOIN album a ON t.album_id = a.id
                                    JOIN albumperformer ap ON a.id = ap.album_id
                                    JOIN performer p ON ap.performer_id = p.id
                                    WHERE nickname = 'Metallica';
                                    """).fetchall()
    return sel
def more_one_genre(connection):
    sel = connection.execute("""SELECT a.album_name FROM album a
                                    JOIN albumperformer ap ON a.id = ap.album_id
                                    JOIN performer p ON ap.performer_id = p.id
                                    JOIN genreperformer gp ON p.id = gp.performer_id
                                    JOIN genre g ON gp.performer_id = g.id
                                    GROUP BY a.album_name
                                    HAVING COUNT(g.genre_name) > 1;
                                    """).fetchall()
    return sel
def not_in_comp(connection):
    sel = connection.execute("""SELECT track_name FROM tracks t
                                    LEFT JOIN compilationtracks cp ON t.id = cp.tracks_id
                                    WHERE cp.tracks_id IS NULL
                                    """).fetchall()
    return sel
def min_dur(connection):
    sel = connection.execute("""SELECT DISTINCT nickname FROM performer p
                                    JOIN albumperformer ap ON p.id = ap.album_id
                                    JOIN album a ON ap.album_id = a.id
                                    JOIN tracks t ON a.id = t.album_id
                                    WHERE duration = (SELECT MIN(duration) FROM tracks t);
                                    """).fetchall()
    return sel
def min_count_tracks(connection):
    sel = connection.execute("""SELECT a.album_name FROM album a
                                  JOIN tracks t ON a.id = t.album_id
                                  GROUP BY a.album_name
                                  HAVING COUNT(t.track_name) = 
                                    (SELECT COUNT(track_name) FROM album a
                                         JOIN tracks t ON a.id = t.album_id
                                         GROUP BY a.album_name
                                         ORDER BY COUNT(track_name)
                                         LIMIT 1)
                                    """).fetchall()
    return sel


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('postgresql://alex1:Volgograd2@localhost:5432/pdlesson2')
    connection = engine.connect()

    # Количество исполнителей в каждом жанре
    print(pd.DataFrame(performers_in_genre(connection)))
    # количество треков, вошедших в альбомы 2019 - 2020 годов;
    print(pd.DataFrame(tracks_in_album_218_2020(connection)))
    # средняя продолжительность треков по каждому альбому;
    print(pd.DataFrame(avr_dur(connection)))
    # все исполнители, которые не выпустили альбомы в 2020 году;
    print(pd.DataFrame(not_in_2020(connection)))
    # названия сборников, в которых присутствует конкретный исполнитель(выберите сами);
    print(pd.DataFrame(Metallica(connection)))
    # название альбомов, в которых присутствуют исполнители более 1 жанра;
    print(pd.DataFrame(more_one_genre(connection)))
    # наименование треков, которые не входят в сборники;
    print(pd.DataFrame(not_in_comp(connection)))
    # исполнителя(-ей), написавшего самый короткий по продолжительности трек(теоретически таких треков может быть несколько);
    print(pd.DataFrame(min_dur(connection)))
    # название альбомов, содержащих наименьшее количество треков.
    print(pd.DataFrame(min_count_tracks(connection)))