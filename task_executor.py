import os
import pyautogui
import time

def execute_task(command):
    command = command.lower()  # Make it case-insensitive

    if "open notepad" in command:
        os.system("start notepad")
        return "Opening Notepad"
    
    elif "open calculator" in command:
        os.system("start calc")
        return "Opening Calculator"

    elif "type" in command:
        msg = command.split("type", 1)[1].strip()
        time.sleep(1)  # Brief pause before typing
        pyautogui.typewrite(msg, interval=0.05)
        return f"Typing: {msg}"

    else:
        return "Command not recognized"