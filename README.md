# Chrome "Restore Pages" Bug Fix
<p><b>Applicable to:</b> Google Chrome/Chromium</p>
<p><b>Tested OS:</b> Linux Ubuntu 20.04.1</p>
<b>Description:</b> Google Chrome crashes when shutting down. Starting Google Chrome will display a "Restore pages?" pop up. Following the instructions, will fix this problem. This script will change the value of the key 'exit_type' in Google Chromes 'Preferences' file to the value 'Normal' instead of 'Crashed'.

## 1. Download files
<p>Download files to any directory.</p>

## 2. Install python
<p><i>Skip if already installed.</i></p>
<p>Python installation</p>

## 3. Create service
Add a new application to "Startup Applications".<br>
Use this path `<PATH_TO_REPOSITORY>/chromefix/chromefix.sh` and replace _PATH_TO_REPOSITORY_ with your path to the repository.

## 4. Done!
<p>This python script will be executed each time after startup.</p>

## 5. OPTIONAL: Check if script worked
<p>After startup up you can execute `python check_if_crashed.py` to see if the `exit_type` is `Normal` or `Crashed`.</p>
