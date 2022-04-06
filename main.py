import sqlalchemy
def input_genre():

    connection.execute("""INSERT INTO genre(genre_name)
                    VALUES('Jaz');
  """)
    connection.execute("""INSERT INTO genre(genre_name)
                    VALUES('Metal');
    """)
    connection.execute("""INSERT INTO genre(genre_name)
                    VALUES('Pop');
    """)
    connection.execute("""INSERT INTO genre(genre_name)
                    VALUES('Folk');
    """)
    connection.execute("""INSERT INTO genre(genre_name)
                    VALUES('Classic');
    """)

def input_performer():
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Francis Sinatra');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Bob Dylan');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Sabaton');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Michael Jackson');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Ludwig van Beethoven');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Fryderyk Chopin');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Louis Armstrong');
    """)
    connection.execute("""INSERT INTO performer(nickname)
                    VALUES('Metallica');
    """)

def input_album():
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('With Heart', 2022);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('My Lovely Sea', 2021);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('Metalizer', 2007);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('Dangerous', 1991);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('Sonata', 2022);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('Chopin Study Music', 2020);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('The Complete Set', 1996);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('Death Magnetic', 2008);
    """)
    connection.execute("""INSERT INTO album(album_name, year_of_issue)
                    VALUES('The Shortest Straw', 2018);
    """)

def input_tracks():
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Cyanide', 399, 8);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Got Butter On It', 188, 7);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Chopin: Mazurka No.27 In E Minor Op.41 No.1', 114, 6);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Beethoven: Piano Sonata No. 12 in A-Flat Major, Op. 26: IV. Allegro', 180, 5);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('In the Closet', 390, 4);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Shadows', 208, 3);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('A Hard Rains A-Gonna Fall', 419, 2);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Ready, Willing And Able', 144, 1);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('My Back Pages', 259, 2);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Masters Of The World', 243, 3);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Give In to Me', 328, 4);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Beethoven: Piano Sonata No. 15 in D Major, Op. 28 "Pastoral": II. Andante', 361, 5);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Chopin: Variations in E, "Hexameron"', 99, 6);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('Jazz Battle', 163, 7);
    # """)
    # connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
    #                 VALUES('My Apocalypse', 361, 8);
    # """)
    connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
                    VALUES('The Unforgiven III', 466, 8);
    """)
    connection.execute("""INSERT INTO tracks(track_name, duration, album_id)
                    VALUES('The End Of The Line', 472, 8);
    """)

def input_compilation():
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                    VALUES('My faforite', 2009);
    """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('Firsts', 2018);
        """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('People', 2021);
        """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('XYZ', 2007);
        """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('Rockstar', 2012);
        """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('7887', 2022);
        """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('Popcllasic', 2006);
        """)
    connection.execute("""INSERT INTO compilation(compilation_name, year_of_issue)
                        VALUES('Open Space', 2019);
        """)

def input_genreperformer():
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(1, 1);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(1, 7);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(2, 3);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(2, 8);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(3, 4);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(3, 2);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(4, 3);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(4, 2);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(5, 6);
        """)
    connection.execute("""INSERT INTO genreperformer(genre_id, performer_id)
                        VALUES(5, 5);
        """)

def input_albumperformer():
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(1, 1);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(1, 5);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(2, 2);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(3, 3);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(4, 4);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(5, 5);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(5, 6);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(6, 6);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(7, 7);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(8, 8);
            """)
    connection.execute("""INSERT INTO albumperformer(performer_id, album_id)
                            VALUES(8, 3);
            """)

def inpit_compilationtracks():
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(1, 6);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(1, 2);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(1, 12);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(2, 13);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(2, 1);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(2, 7);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(3, 3);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(3, 8);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(3, 11);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(4, 14);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(4, 5);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(4, 4);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(5, 9);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(5, 15);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(6, 10);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(6, 3);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(6, 8);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(7, 6);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(7, 13);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(7, 7);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(8, 9);
            """)
    connection.execute("""INSERT INTO compilationtracks(compilation_id, tracks_id)
                            VALUES(8, 15);
            """)


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('postgresql://alex1:Volgograd2@localhost:5432/pdlesson2')
    connection = engine.connect()
    # заполняем жанры
    # input_genre()
    # заполняем исполнителей
    # input_performer()
    # заполняем альбомы
    # input_album()
    # заполняем треки
    input_tracks()
    # заполняем сборники
    # input_compilation()
    # заполняем связи жанр-исполнитель
    # input_genreperformer()
    # заполняем связи альбом-исполнитель
    # input_albumperformer()
    # заполняем связи сборник-трек
    # inpit_compilationtracks()