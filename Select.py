import sqlalchemy
import pandas as pd

def select2018(connection):
    sel = connection.execute("""SELECT album_name, year_of_issue FROM album
        WHERE year_of_issue = 2018;
    """).fetchall()
    return sel

def mustduration(connection):
    sel = connection.execute("""SELECT track_name, duration FROM tracks
            ORDER BY duration DESC;
        """).fetchmany(1)
    return sel

def lowduration(connection):
    sel = connection.execute("""SELECT track_name FROM tracks
        WHERE duration < 210;
    """).fetchall()
    return sel

def compilationissue(connection):
    sel = connection.execute("""SELECT compilation_name FROM compilation
        WHERE year_of_issue BETWEEN 2018 AND 2020;
    """).fetchall()
    return sel

def performers_names(connection):
    sel = connection.execute("""SELECT nickname FROM performer
        WHERE nickname NOT LIKE '%% %%';
    """).fetchall()
    return sel

def name_my(connection):
    sel = connection.execute("""SELECT track_name FROM tracks
        WHERE track_name iLIKE '%%my%%' OR track_name iLIKE '%%мой%%';
    """).fetchall()
    return sel

if __name__ == '__main__':
    engine = sqlalchemy.create_engine('postgresql://alex1:Volgograd2@localhost:5432/pdlesson2')
    connection = engine.connect()
    # # название и год выхода альбомов, вышедших в 2018 году
    print(pd.DataFrame(select2018(connection)))
    # # название и продолжительность самого продолжительного трека
    print(pd.DataFrame(mustduration(connection)))
    # # название треков, продолжительность которых менее 3.5 мин
    print(pd.DataFrame(lowduration(connection)))
    # названия сборников, вышедших с 2018 по 2020г включительно
    print(pd.DataFrame(compilationissue(connection)))
    # исполнители чье имя состоит из одного слова
    print(pd.DataFrame(performers_names(connection)))
    # название треков, которые содержат слово "мой"/"my
    print(pd.DataFrame(name_my(connection)))
