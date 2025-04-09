import subprocess
import time

import json

import os

# def list_all_file_paths(directory):
#     file_paths = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             full_path = os.path.join(root, file)
#             file_paths.append(full_path)
#     return file_paths

# # Replace this with your target directory
# target_directory = "/home/vboxuser/ext-js-singlepage/EXT-js-single-page-application/QuickStart-master/app"
# all_files = list_all_file_paths(target_directory)




def open_goose(session_name, file_path, target_dir, prompt_template):
    # Customize the prompt with file_path and target_dir
    prompt = prompt_template.format(file_path=file_path, target_dir=target_dir)
    
    # Start a new detached tmux session
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name, "goose session"])
    time.sleep(2)

    # Send the prompt to the session
    subprocess.run(["tmux", "send-keys", "-t", session_name, prompt, "Enter"])

    # Open a terminal and attach to the tmux session
    subprocess.run(["gnome-terminal", "--", "tmux", "attach", "-t", session_name])

# Load prompt from JSON file
with open("prompt.json", "r") as f:
    data = json.load(f)
    prompt_template = data["prompt"]

# Example usage
open_goose("goo_sess", "/home/vboxuser/ext-js-singlepage/EXT-js-single-page-application/QuickStart-master/app/store/Employee.js", "/home/vboxuser/react-application", prompt_template)
open_goose("goo_sess2", "/home/vboxuser/ext-js-singlepage/EXT-js-single-page-application/QuickStart-master/app/view/main/ListViewController.js", "/home/vboxuser/react-application", prompt_template)
