# W5D2
import psycopg2


def get_all_data():
    conn = psycopg2.connect("dbname=nfl_data user=RobertWard")
    cur = conn.cursor()
    cur.execute("SELECT * FROM nflTable;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return items


def report_print():
    items = get_all_data()
    print_all_stats(items)


def print_all_stats(items):
    print("\n"*60)
    print("IDX\tRank\tName\t\t\t\tteam\tGmsSt\tAtts\tYards\tRecTDs\tTarget\tRecps\tR-Yards\tR-TDs")
    for each in items:
        for every in each:
            print(every, "\t", end='')
        print("\n")


def what_to_do():
    while True:
        print("\n"*60)
        ent = input("Would you like to:\t(P)rint your player report\n\t\t\t(S)earch\n\t\t\t(A)dd\n\t \t\t(D)elete a player?  ")
        entry = ent.lower()
        if entry == 's' or entry == 'a' or entry == 'd' or entry == 'p':
            return entry


def add_a_player():
    columns = ['rank', 'name', 'team', 'gamestart', 'attempts', 'yard', 'rTDs', 'target', 'receptions', 'yards', 'pTDs']
    new_player = []
    print("\n"*60)
    for each in columns:
        entry = input("Please enter player's {} :".format(each))
        new_player.append(entry)

    ent = input("/nIs this all correct? (y/n) ")
    if ent == "n" or ent == "N":
        add_a_player()
    else:
        conn = psycopg2.connect("dbname=nfl_data user=RobertWard")
        cur = conn.cursor()
        cur.execute("INSERT INTO nflTable (rank, name, team, gamestart, attempts, yard, rTDs, target, receptions, yards, pTDs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (new_player[0], new_player[1], new_player[2], new_player[3], new_player[4], new_player[5], new_player[6], new_player[7], new_player[8], new_player[9], new_player[10]))
        conn.commit()
        cur.close()
        conn.close()
        # WHERE NOT EXISTS (SELECT id FROM example_table WHERE id = 1);


def search_player():
    place = 0
    choice = ""
    print("\n"*60)
    ent = input("Do you want to search by (N)ame, (R)ank, or (T)eam code? ")
    entry = ent.lower()
    if entry == 'n':
        choice = "name"
        place = 2
    elif entry == 'r':
        choice = "rank"
        place = 1
    elif entry == 't':
        choice = "team code"
        place = 3

    entry = input("Enter the {} :".format(choice))

    if place == 3:
        return place, entry

    items = get_all_data()
    for i, each in enumerate(items):
        if each[place] == entry:
            print("\n", each, "\n")
            return 0, each


def prt_all_matching(entry):
    report = []
    items = get_all_data()
    for i, each in enumerate(items):
        if each[place] == entry:
            report.append(each)
    print("\n"*60)
    print("IDX\tRank\tName\t\t\t\tteam\tGmsSt\tAtts\tYards\tRecTDs\tTarget\tRecps\tR-Yards\tR-TDs")
    for each in report:
        for every in each:
            print(every, "\t", end='')
        print("\n")


def del_player():
    while True:
        ent = input("Which player do you want to delete - please enter the INDEX\n---> enter X if you need to see the report printed first: ")
        entry = ent.lower()
        if entry == 'x':
            report_print()
        else:
            conn = psycopg2.connect("dbname=nfl_data user=RobertWard")
            cur = conn.cursor()
            cur.execute("SELECT * FROM nflTable;")

            x = int(entry)
            for i in range(x):
                item = cur.fetchone()
            thisone = item[2]
            print(type(item[2]))
            cur.execute("DELETE FROM nflTable WHERE name=%s;", (thisone,))
            conn.commit()
            cur.close()
            conn.close()


# =============================   MAIN   ==============================

while True:
    place = 0
    decision = what_to_do()
    if decision == 'a':
        add_a_player()
        report_print()
    elif decision == 's':
        place, player = search_player()
    elif decision == 'd':
        del_player()
    elif decision == 'p':
        report_print()

    if place == 3:
        prt_all_matching(player)

    ent = input("All done ?   (y/n) ")
    entry = ent.lower()
    if entry == 'y':
        print("\nGood bye !\n")
        break
