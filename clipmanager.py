import pyperclip # we will need to install this using pip install pyperclip
import time
import os
HISTORY_FILE = "clipboard_history.txt"
if not os.path.isfile(HISTORY_FILE):  #first we check if the file already exist
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        f.write("clipboard history: \n\n")

def get_clipboard():
    return pyperclip.paste() #get the last clipboard items

print("Clipmanager has been enabled, press keys ctrl c to stop it.\n")
last_clipboard_data = ""
try:
    while True:
        clipboard_content = get_clipboard().strip()
        if clipboard_content and clipboard_content != last_clipboard_data:
            with open(HISTORY_FILE, "a", encoding="utf-8") as f:
                f.write(clipboard_content + "\n" + "-" * 50 + "\n")

            print(f"saved: {clipboard_content[:50]}...")  #preview of the save content
            last_clipboard_data = clipboard_content
        time.sleep(2)  #we wait a little bit to not overload the system

except KeyboardInterrupt:
    print("\nClipmanager has been disabled.")
