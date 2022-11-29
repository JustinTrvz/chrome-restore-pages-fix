import json
import os

home_dir = os.path.expanduser("~")
preferences_filepath = f"{home_dir}/.config/google-chrome/Default/Preferences"

with open(preferences_filepath, "r") as file:
    json_dict = json.load(file)
    file.close()

if json_dict["profile"]["exit_type"] != "Normal":
    json_dict["profile"]["exit_type"] = "Normal"

with open(preferences_filepath, "w") as outfile:
    outfile.write(json.dumps(json_dict))
