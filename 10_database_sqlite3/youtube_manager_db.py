#Lecture 21: Python project Youtube manager with sqlite3
#Reference Docs: https://docs.python.org/3/library/sqlite3.html

import sqlite3

conn = sqlite3.connect("youtube.db") #NOTE: connection commit and close connection with DB (connection_var.commit(), connection_var.close())
cursor = conn.cursor() #NOTE: cursor helpto perform DB operations (CREATE, UPDATE, DELETE, READ/SHOW → fetchall(),fetchone(), etc)

cursor.execute('''CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
               ''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos") #all data of 'videos' is now available in cursor
    print("\n")
    print("*" * 70)
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" * 70)

def add_video(name, time):
    # cursor.execute("INSERT INTO videos where name = ?, time = ?", (name, time)) #my_first_syntax_mistake_☺
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added sucessfully!")

def update_video(id, name, time):
    # cursor.execute("UPDATE INTO videos WHERE id = ") #my_first_syntax_mistake_☺
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id)) #we pass the arguments name in order respective to sql syntax (i.e name → time → id)
    conn.commit()
    print(f"Videos {id} updated sucessfully")

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,)) #NOTE: even if there is only one argumnets you MUST write comma ',' at the end (id,)
    conn.commit()
    print(f"Videos {id} deleted sucessfully")

def main():
    while True:
        print("\n Youtube manager application with DB | Select any one option")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = int(input("Please enter video id that you want to update: "))
            new_name = input("Please enter the new name: ")
            new_time = input("Please enter the new duration: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            id = int(input("Enter the video ID you want to delete: "))
            delete_video(id)
        elif choice == '5':
            break
        else:
            print("Invalid Input ")

    conn.close() #after the main file ran successfully, you should close() connection to avoid database corruption.
        
if __name__ == '__main__':
    main()