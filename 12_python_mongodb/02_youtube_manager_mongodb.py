#Lecture 23 : Python Project Youtube manager with mongoDB
#Supporting Lecture 23.1 : Watch this before installing any database | link → https://www.youtube.com/watch?v=j4YeLqxgj1k

# Try to practice this from this doc only (then move to github or video) → https://pypi.org/project/pymongo/

import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://thearyandev:thearyandev@cluster0.3zdchzl.mongodb.net/", tlsAllowInvalidCertificates=True)
# Not a good idea to include id and password in code files
#  tlsAllowInvalidCertificates=True - Not a good way to handle ssl
db = client["youtube_manager_db"] #Name of your database
video_collection = db["videos"] #Name of collection (like tables in SQL DBs)

def list_videos():
    all_videos = video_collection.find() #NOTE: find() is enumuratable, So ↓
    print("\n")
    print("*" * 70)
    for vid in all_videos:
        # print(vid)
        print(f"Video ID: {vid['_id']}, Name: {vid['name']} and Duration: {vid['time']}") #Since vid is of dict data type.
    print("\n")
    print("*" * 70)

def add_videos(name, time):
    video_collection.insert_one({'name': name, 'time': time}) #NOTE: we always pass value in {} for adding/updating/deleting in mongo
    print("Added Successfully!")

def update_videos(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {'$set': {'name': new_name, 'time': new_time}}) #NOTE: you MUST pass mongo '_id' on ObjectId() (just keep in mind that, a data type that is specifically designed to pass ID in ObjectId() type NOT String NOT Tuple.) |     .update_one({}, {}) → always takes 2 parameters : 1st → where to update, 2nd → what to update 
    print(f"Video ID {video_id} is updated successfully!")

def delete_videos(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})
    print(f"Video ID {video_id} deleted successfully!")

def main():
    while True:
        print("\nYouTube Manager App | Choose an option")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_videos(name, time)
        elif choice == '3':
            list_videos()
            video_id = input("Enter video ID you want to update: ")
            name = input("Enter video new name: ")
            time = input("Enter video new time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            list_videos()
            video_id = input("Enter video ID you want to delete: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()

