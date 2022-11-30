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
`sudo gedit /etc/systemd/system/chromefix-after-startup.service` 
<p>Create new service file.</p>

```
[Unit]
Description=Chromefix after startup

[Service]
Type=simple
ExecStart=<PATH_TO_REPOSITORY>/chromefix/chromefix.sh

[Install]
WantedBy=multi-user.target
```

<p>Replace <i>PATH_TO_REPOSITORY</i>.</p>

`systemctl daemon-reload`<br>
`systemctl enable chromefix-before-shutdown.service`<br>
<p>Makes service file available.</p>

## 4. Done!
<p>This python script will be executed each time after startup.</p>

## 5. OPTIONAL: Check if script worked
<p>After startup up you can execute `python check_if_crashed.py` to see if the `exit_type` is `Normal` or `Crashed`.</p>
