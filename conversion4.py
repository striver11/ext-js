import subprocess
import time
import json
import os

def list_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):  # Optional: only include .js files
                full_path = os.path.join(root, file)
                file_paths.append(full_path)
    return file_paths

def open_goose(session_name, file_path, target_dir, prompt_template):
    prompt = prompt_template.format(file_path=file_path, target_dir=target_dir)
    
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name, "goose session"])
    time.sleep(2)

    subprocess.run(["tmux", "send-keys", "-t", session_name, prompt, "Enter"])
    subprocess.run(["gnome-terminal", "--", "tmux", "attach", "-t", session_name])

# Load prompts
with open("prompt.json", "r") as f:
    prompts = json.load(f)

# Get all .js files from target directory
target_directory = "/home/vboxuser/ext-js-singlepage/EXT-js-single-page-application/QuickStart-master/app"
all_files = list_all_file_paths(target_directory)


for i, file_path in enumerate(all_files):
    session_name = f"goose_sess_{i}"
    if i % 2 == 0 and i!=0:
        time.sleep(50)
    open_goose(session_name, file_path, "/home/vboxuser/react-application4", prompts["prompt_1"])
    

    
