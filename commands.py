import os
import subprocess
from datetime import datetime

def execute_command(query):

    query = query.lower()

    if "open notepad" in query:
        os.system("notepad")
        return "Opening Notepad"

    elif "open calculator" in query:
        os.system("calc")
        return "Opening Calculator"

    elif "open chrome" in query:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Opening Chrome"

    elif "time" in query:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"Current time is {current_time}"

    return None