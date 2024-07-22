# lyrion_preamp
Lyrion_preamp is a small utility that runs as a daemon on a squeezelite server to which a multimedia pad is attached to. It captures volume, play, pause, mute, next, prev presses and sends them across to the Lyrion server. This allows for a consistent status of the system across all clients (mobile, local, ...).

## Disclaimer
Some chunks of the code come from https://github.com/molobrakos/lms. Thanks for this super clean work, this helped a lot in speeding up the development of lyrion_preamp. 

## Dependencies
Python3 code kept simple:
  - evdev
  - logging
  - json
  - requests

# Configuration
Not much really, I am using a 'Vaydeer Vaydeer Multimedia Console Keyboard' and it reports as 'Vaydeer Vaydeer Multimedia Console Keyboard' (here: https://www.amazon.com/Vaydeer-Multimedia-Controller-One-Click-Function/dp/B08V95ZZLM)
Adjust the name for your multimedia pad at line 51 in file lms_preamp.py.

# Installation
The way I do it:
- I copy both files in the ~/bin/ directory.
- Make sure lyrion_preamp.py as x rights: $ chmod u+x lyrion_preamp.py
- Check it works ok: $ ~/bin/lyrion_preamp_preamp.py
Then you may want to add this as a systemd service:
- Copy the lyrion_preamp.service file to /etc/systemd/system/
- Edit that file to change from user oubahoubah to your username (the one who owns the home directory that received the python scripts)
- That user should be in the 'input' group to be able to read input devices
- Run: $ sudo systemctl daemon-reload
- And: $ sudo systemctl enable --now /etc/systemd/system/lyrion_preamp.service

You should be ok to go !

# More ?
Yes, that simple daemon can do more if you adapt it. If your pad has more/less keys than those in lyrion_preamp.py, feel free to suit it to your needs !
