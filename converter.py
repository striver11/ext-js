import subprocess
import time

def open_goose(session_name, file_path, target_dir):
    # Create a new tmux session with a unique name
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name, "goose session"])
    time.sleep(2)
    
    # Send a command to the tmux session
    subprocess.run(["tmux", "send-keys", "-t", session_name, 
                    f"go through this ext.js file in the dir {file_path} and convert it into react js application and store it in dir {target_dir} with same file name.please convert as many times as I ask.", "Enter"])

    # Attach to the tmux session in a new terminal window
    subprocess.run(["gnome-terminal", "--", "tmux", "attach", "-t", session_name])

# Open the sessions with specific names, paths, and target directories
open_goose("goo_sess", "/home/ubuntu/praveen/QuickStart/app/store/Employees.js", "/home/ubuntu/praveen/react-app")
open_goose("goo_sess2", "/home/ubuntu/praveen/QuickStart/app/Application.js", "/home/ubuntu/praveen/react-app")

