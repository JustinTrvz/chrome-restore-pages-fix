# Chrome "Restore Pages" Bug Fix
<p><b>Applicable to:</b> Google Chrome/Chromium</p>
<p><b>OS:</b> Linux Ubuntu 20.04.1</p>
<p><b>Description:</b> Google Chrome crashes when shutting down. Starting Google Chrome will display a "Restore pages?" pop up. Following the instructions, will fix this problem.</p>

## 1. Download files
<p>Download files to any directory.</p>

## 2. Install python
<p><i>Skip if already installed.</i></p>
<p>Python installation</p>

## 3. Create service
`sudo gedit /etc/systemd/system/chromefix-before-shutdown.service`
<p>Create new service file.</p>

```
[Unit]
Description=Chromefix before shutdown
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=oneshot
ExecStart=<PATH_TO_CHROMEFIX.SH_FILE>
TimeoutStartSec=0

[Install]
WantedBy=shutdown.target
```

<p>Replace <i>PATH_TO_CHROMEFIX.SH_FILE</i> with the path to your <i>chromefix.sh</i> file.</p>

`systemctl daemon-reload`
`systemctl enable chromefix-before-shutdown.service`
<p>Makes service file available.</p>

## 4. Done!
<p>This python script will be executed before shutting down your computer.</p>
<p>Alternatively you can create a process that will be executed when starting your computer.</p>
<p>Since on my computer many processes start when I boot, I set the execution in front of the shutdown process.</p>
