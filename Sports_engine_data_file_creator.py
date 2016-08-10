# W5D2

import csv
import psycopg2


def load_file():
    raw_data = []
    with open('rush_rec_data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            raw_data.append(row)
    return raw_data


def make_file_DB(raw):
    conn = psycopg2.connect("dbname=nfl_data user=RobertWard")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS nflTable (id serial PRIMARY KEY, rank varchar, name varchar, team varchar, d1 varchar, d2 varchar, d3 varchar, gamestart varchar, attempts varchar, yard varchar, rTDs varchar, d4 varchar, d5 varchar, d6 varchar, d7 varchar, target varchar, receptions varchar, yards varchar, d8 varchar, pTDs varchar, d9 varchar,d10 varchar,d11 varchar,d12 varchar,d13 varchar,d14 varchar,d15 varchar);")

    for each in raw:
        cur.execute("INSERT INTO nflTable (rank, name, team, d1 , d2 , d3, gamestart, attempts, yard, rTDs, d4, d5, d6, d7, target, receptions, yards, d8, pTDs, d9,d10,d11,d12,d13,d14,d15) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (each[0], each[1], each[2], each[3], each[4], each[5], each[6], each[7], each[8], each[9], each[10], each[11], each[12], each[13], each[14], each[15],
         each[16], each[17], each[18], each[19], each[20], each[21], each[22], each[23], each[24], each[25]))

    cur.execute("ALTER TABLE nflTable DROP COLUMN d1, DROP COLUMN d2, DROP COLUMN d3, DROP COLUMN d4, DROP COLUMN d5, DROP COLUMN d6, DROP COLUMN d7, DROP COLUMN d8, DROP COLUMN d9, DROP COLUMN d10, DROP COLUMN d11, DROP COLUMN d12, DROP COLUMN d13, DROP COLUMN d14, DROP COLUMN d15;")

    conn.commit()
    cur.close()
    conn.close()



raw_data = load_file()

make_file_DB(raw_data)
