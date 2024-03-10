import sqlite3

connection = sqlite3.connect('W02/activity.db')

cursor = connection.cursor()

option = None
options = [
"Dates With Messages Less Than 1000",
"Dates With Messages Greater Than 20000",
"Print 2018",
"Print December 2020"
]

def display_options(options):
    index = 1
    for item in options:
        print(f"[{index}] {item}")
        index += 1
    print("[Q] Quit")
while option != "Q":
    display_options(options)
    option = input("> ").upper()
    match option:
        case "Q":
            cursor.close()
            connection.close()
        case "1":
            print("\nDates With Messages Less Than 1000\n")
            cursor.execute("SELECT * FROM messages_per_day WHERE messages < 1000")
            for row in cursor.fetchall():
                print(f"{row[0]} | {row[1]}")
        case "2":
            print("\nDates With Messages Greater Than 20000\n")
            cursor.execute("SELECT * FROM messages_per_day WHERE messages > 20000")
            for row in cursor.fetchall():
                print(f"{row[0]} | {row[1]}")
        case "3":
            print("\nPrint 2018\n")
            cursor.execute("SELECT * FROM messages_per_day WHERE theDate < '2019-01-01'")
            for row in cursor.fetchall():
                print(f"{row[0]} | {row[1]}")
        case "4":
            print("\nPrint December 2020\n")
            cursor.execute("SELECT * FROM messages_per_day WHERE theDate > '2020/12/01' AND theDate <= '2020/12/31'")
            for row in cursor.fetchall():
                print(f"{row[0]} | {row[1]}")
                



