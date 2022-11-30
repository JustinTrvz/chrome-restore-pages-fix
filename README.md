# Chrome "Restore Pages" Bug Fix
<p><b>Applicable to:</b> Google Chrome/Chromium</p>
<p><b>Tested OS:</b> Linux Ubuntu 20.04.1</p>
<p><b>Description:</b> Google Chrome crashes when shutting down. Starting Google Chrome will display a "Restore pages?" pop up. Following the instructions, will fix this problem.</p>

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
