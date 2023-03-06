import os
import instaloader
from art import *
import colorama
import instaloader as i
from instaloader.exceptions import BadCredentialsException
from instaloader.exceptions import *


class ChoiceException(Exception):  # Custom Exception class
    def __init__(self, value):
        self.value = value

print(colorama.Fore.CYAN)
tprint("INSTAGRAM     VIDEO     CONVERTER")
print(colorama.Fore.RESET)

ig = instaloader.Instaloader()  # Instance created of instaloader

while True:
    try:
        username = input("👉Enter Valid Username: ")
        password = input("👉Enter Valid Password: ")
        # Below we are setting the username and password properties of the context attribute of the ig instance of Instaloader.
        ig.context.username = username
        ig.context.password = password

        print("\n⏳Checking if entered credentials are correct, Please Wait...\n")

        # Pass this username and password login method of context attribute to login to user profile
        ig.context.login(username, password)

        if ig.context.is_logged_in:
            print("-------------------------")
            print("   ✅Login Success!")
            print("-------------------------")
            break

    except (BadCredentialsException, ConnectionException):
        print("🚫Username or password incorrect")


while True:
    try:
        input_link = input("⌨ Enter a valid Instagram Video Link: ")
        post_url = input_link.split("/")[-2]
        # Create a Instagram object for the video with the given link
        post = i.Post.from_shortcode(ig.context, post_url)  #  Splits and matches if shortcode valid
        break
    except (PostChangedException, ProfileNotExistsException, PermissionError, LoginRequiredException,
            PrivateProfileNotFollowedException, IndexError):
        print("🛑 Invalid Instagram Link!")

print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)
print("\n👉 Video Creator: " + str(post.owner_username))  # Prints the creator name of the video
print("\n👍 Total Likes: " + str(post.likes) + "\n\n📅 Publish Date: " + str(post.date))  # Prints the likes and publish date of the video
print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)

while True:  # Inside this while loop is exception handling on whether or not user wants to see caption or not
    try:
        caption_choice = input("Do You want to Display video Caption (Y/N): ")
        if caption_choice != "Y" and caption_choice != "N":
            raise ChoiceException("🛑 Invalid Choice")
        elif caption_choice == "Y":
            print("👉 Video Caption: \n" + str(post.caption))  # Prints the caption of video
            break
        elif caption_choice == "N":
            break
    except ChoiceException:
        print("🛑 Invalid Choice")

print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)
print(colorama.Fore.GREEN + "-----------------------------------------------------------------------------------------------------" + colorama.Fore.RESET)

print("⌛Your Post Files are Being Downloaded... Please Wait...")  # This will Download All Post Files including thumbnail, json file, video and caption
ig.download_post(post, target="Instagram Post Downloads")
print("✅ DOWNLOAD SUCCESS!")

print("\n⌛Your Video is Being Downloaded... Please Wait...")  # This will Download video
ig.download_post(post, target="Instagram Video Downloads")
print("✅ DOWNLOAD SUCCESS!")

# Below Code snippet removes all the files other than the mp4 file from folder
#-------------------------------------------------------------------------------------------------------------

folder_path = r"C:\Users\saadg\PycharmProjects\pythonProject7\Instagram Video Downloads"
extension1 = ".txt" # replace with the file extension you want to delete
extension2 = ".xz" # replace with the file extension you want to delete
extension3 = ".jpg" # replace with the file extension you want to delete
for filename in os.listdir(folder_path):
    if filename.endswith(extension1) or filename.endswith(extension2) or filename.endswith(extension3):
        os.remove(os.path.join(folder_path, filename))

#-------------------------------------------------------------------------------------------------------------

# print("⏳Logging Out...")
# ig.context.session.close()

print(colorama.Fore.MAGENTA)
tprint("========================")
tprint("CREDS:        SAAD     ABDUR     RAZZAQ")
tprint("========================")
print(colorama.Fore.RESET)