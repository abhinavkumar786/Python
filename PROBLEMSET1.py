# external module
import pyttsx3
engine = pyttsx3.init()
engine.say("abhinav beat ritu she is not listening")
engine.runAndWait()

# import os

# # Specify the directory (use '.' for current directory)
# directory = '.'

# try:
#     # List all files and directories in the specified path
#     contents = os.listdir(directory)

#     print(f"Contents of directory '{directory}':")
#     for item in contents:
#         print(item)

# except FileNotFoundError:
#     print(f"The directory '{directory}' does not exist.")
# except PermissionError:
#     print(f"Permission denied to access '{directory}'.")
