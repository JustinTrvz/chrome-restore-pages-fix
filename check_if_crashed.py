import json
import os

home_dir = os.path.expanduser("~")
preferences_filepath = f"{home_dir}/.config/google-chrome/Default/Preferences"

with open(preferences_filepath, "r") as file:
    json_dict = json.load(file)
    file.close()
    
exit_type = json_dict["profile"]["exit_type"]
print(f"'exit_type': '{exit_type}'")
    
