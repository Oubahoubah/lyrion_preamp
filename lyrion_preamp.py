#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-

import logging
import evdev
from time import time
from json import dumps as to_json
from sys import stderr
from collections import OrderedDict
from lyrion_lib import Server, __version__
from re import match

_LOGGER = logging.getLogger(__name__)

LOGFMT = "%(asctime)s %(levelname)5s (%(threadName)s) [%(name)s] %(message)s"
DATEFMT = "%y-%m-%d %H:%M.%S"

def timeFmt(secs):
    if not secs:
        return ''
    h, r = divmod(secs, 3600)
    m, secs = divmod(r, 60)
    return '%s%02d.%02d' % ('' if not h else '%02d:' % h, m, secs)


def main():
    log_level = logging.ERROR
    logging.basicConfig(level=log_level,
                    stream=stderr,
                    datefmt=DATEFMT,
                    format=LOGFMT)

    server = Server()
    server.update()

    player = None
    for p in server.players:
        _LOGGER.debug(f'listing players: player={p.name} id={p.player_id} ip={p.ip}')
        if p.name == 'isthme':
            player = p
            _LOGGER.info(f'Found target player: player={p.name} id={p.player_id} ip={p.ip}')
            break

    if player == None:
        exit(0)

    indev = None
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for dev in devices:
        _LOGGER.debug(f'listing input devices: path={dev.path}, name={dev.name}, phys={dev.phys}')
        if dev.name == 'Vaydeer Vaydeer Multimedia Console Keyboard':
            _LOGGER.info(f'Found target input devices: path={dev.path}, name={dev.name}, phys={dev.phys}')
            indev = dev

    if indev == None:
        exit(0)

    _LOGGER.info('Ready to go now !')
    
    for event in indev.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == 0:
                continue
            _LOGGER.debug(f'{evdev.categorize(event)}')
            if event.code == evdev.ecodes.KEY_VOLUMEUP:
                player.volume_up()
            if event.code == evdev.ecodes.KEY_VOLUMEDOWN:
                player.volume_down()
            if event.code == evdev.ecodes.KEY_MUTE:
                player.mute_toggle()
            if event.code == evdev.ecodes.KEY_PREVIOUSSONG:
                player.previous()
            if event.code == evdev.ecodes.KEY_NEXTSONG:
                player.next()
            if event.code == evdev.ecodes.KEY_PLAYPAUSE:
                player.play_toggle()

if __name__ == '__main__':
   main()
