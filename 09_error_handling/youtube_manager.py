#1. show all videos
#2. add a video
#3. update a video
#4. delete a video
#5. exit app

import json

file_name = 'youtube.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file) #this convert the data of file into json-format | NOTE: the output here has come as STRING NOT list or dict or tuple
    except FileNotFoundError:
        return [] #if file-not-found, it returns an empty array

def save_video_helper(videos):
    # videos.append(video)
    with open(file_name, 'w') as file: #why 'w' → bcz we want to write (i.e. dump data with json.dump())
        json.dump(videos, file)     #takes two arguments .dump (what_to_dump, where_to_dump)

def show_all_videos(videos):
    # with open(youtube.txt, 'r') as file:
    #     print(file)
    # print(videos)
    print("\n")
    print("*" * 70)
    all_videos_dict_format = enumerate(videos, start= 1)
    for index, video in all_videos_dict_format: #D
        print(f"{index}. Title: {video['title']}, Duration: {video['duration']}") #D
    print("\n")
    print("*" * 70)  
def add_video(videos):
    # video_description = input("Name and Duration of video: (format : {'name' = "" , 'time' = ""}) ")
    # save_video_helper(video_description)
    title = input("Title of video: ")
    duration = input("Duration of the video: ")
    videos.append({'title' : title, 'duration' : duration}) #D
    save_video_helper(videos)

def update_video(videos):
    # index= int(input("Enter index of video that is to be deleted"))
    # new_video_description = input("Name and Duration of video: (format : {'name' = "" , 'time' = ""}) ")
    # videos[index] = new_video_description
    show_all_videos(videos)
    index = int(input("Which video details you want to update? : "))
    if 1 <= index <= len(videos):
        title = input("Enter new name of the video: ")
        duration = input("Enter new duration of the video: ")
        videos[index - 1] = {'title' : title, 'duration' : duration}
    else:
        print("Invalid index selected!")
    
def delete_video(videos):
    # index = int(input("Enter index"))
    # videos.remove(index)
    show_all_videos(videos)
    index = int(input("Enter video index you want to delete: "))
    if 1 <= index <= len(videos):
        del(videos[index - 1]) #NOTE: video deleted but only in ram not in file
        print (f"Index {index} Video removed sucessfully!") 
        save_video_helper(videos) #NOTE: this statement is mandotory for memory changes | think of this like git commit changes
    else:
        print("Invalid input selected!")


def main():
    # videos = []
    videos = load_data()  #VERY IMPORANT : this variable here "videos" is the base/roor/reference of all those parameter"videos" in used throughout the code , almost in every functions and cases as parameter.
    while True:
        print("Youtube video manager | Below are the available options")
        print("1. Show all videos.")
        print("2. Add a video.")
        print("3. Update a video.")
        print("4. Delete a video.")
        print("5. Exit the app.")

        user_input = input("Choose an option: ")

        match user_input:
            case '1':
                show_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Input, Please try again!")

# main() #bad practice; insted ↓
if __name__ == "__main__":
    main()

#Assignment : Read why we use (video) parameter in some function like save_video_helper, add_video(videos) but not everywhere also, in cases of match we took parameter.