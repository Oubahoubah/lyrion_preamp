# lyrion_preamp
When I initially ran my digital audio hub (CamillaDSP + Squeezelite) on a Linux PC, its user interface from a small touchscreen was less than practical. Very esthetic but the feel of a rotary encoder/potentiometer and buttons is so practical. Much more to my taste than a remote controller, and light years from a phone app - although Lyrion + Material is the best you can get.
It is easy to add a small USB Multimedia keyboard (here: https://www.amazon.com/Vaydeer-Multimedia-Controller-One-Click-Function/dp/B08V95ZZLM) but you need the software glue to send your inputs to the Lyrion server for volume, play/pause, skip and mute. Lyrion_preamp is that small utility that runs as a daemon on the squeezelite client PC/raspberry to which the multimedia keyboard is attached to. It captures volume, play, pause, mute, next, prev presses and sends them across to the Lyrion server using its API (https://lyrion.org/reference/cli/using-the-cli/). This allows for a consistent status of the system across all clients (local touchscreen, mobile, laptop, desktop, HomeAssistant ...).

## Disclaimer
Some (large) chunks of the code are extracted from https://github.com/molobrakos/lms. Thanks for this super clean work, this provided stable foundation with the LMS server and player APIs to speed up the development of that lyrion_preamp tool.

## Dependencies
Python3 code kept simple:
  - evdev
  - logging
  - json
  - requests

        $ pip3 install evdev logging json requests

# Configuration
Not much really, I am using a 'Vaydeer Vaydeer Multimedia Console Keyboard' and it reports as 'Vaydeer Vaydeer Multimedia Console Keyboard' 
Adjust the name for your multimedia pad at line 51 in file lms_preamp.py.
I'll probably provide a way to make this more practical with a command-line argument, avoiding a configuration file

# Installation
The way I do it:
- I copy both files in the ~/bin/ directory.
- Make sure lyrion_preamp.py as x rights:

        $ chmod u+x lyrion_preamp.py

- Check it works ok:

        $ ~/bin/lyrion_preamp_preamp.py
  
Then you may want to add this as a systemd service:
- Copy the lyrion_preamp.service file to /etc/systemd/system/
- Edit that file to change from user oubahoubah to your username (the one who owns the home directory that received the python scripts)
- That user should be in the 'input' group to be able to read input devices
- Run:

        $ sudo systemctl daemon-reload
  
- And:

        $ sudo systemctl enable --now /etc/systemd/system/lyrion_preamp.service

You should be ok to go !

# More ?
Yes, that simple daemon can do more if you adapt it. If your pad has more/less keys than those in lyrion_preamp.py, feel free to suit it to your needs !
