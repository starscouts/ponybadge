import badger2040w
import picographics
import jpegdec
import json
import sys
import uos as os
import machine
import stealth as stealth_mode

global display
global badger

import config

def update(index):
    badger.led(128)
    display.set_pen(15)
    display.clear()
    
    if stealth:
        stealth_mode.stealth(badger, display)
    else:
        j = jpegdec.JPEG(display)
        j.open_file("data/" + list[index]['id'] + ".jpeg")
        j.decode(0, 0, jpegdec.JPEG_SCALE_FULL)

        display.set_pen(0)
        display.set_font("bitmap8")
        display.text(list[index]['name'], 130, 20, scale=2)
        
        display.set_font("bitmap6")
        display.text(list[index]['pronouns'] + list[index]['age'], 130, 40, scale=2)
        
        display.set_font("bitmap6")
        display.text(list[index]['species'], 130, 55, scale=2)

    display.update()
    
    f = open("state/fronter.txt", "w")
    f.write(str(current))
    f.close()
    
    f = open("state/stealth.txt", "w")
    f.write("1" if stealth else "0")
    f.close()
    badger.led(0)

badger = badger2040w.Badger2040W()

display = picographics.PicoGraphics(display=picographics.DISPLAY_INKY_PACK)

try:
    badger2040w.system_speed(badger2040w.SYSTEM_SLOW)
except ValueError:
    pass
    
    try:
        badger2040w.system_speed(badger2040w.SYSTEM_NORMAL)
    except ValueError:
        pass

badger.led(128)
display.set_pen(15)
display.clear()

file = open("./data/list.json", "r+")
list = json.loads(file.read())

list = [i for i in list if i['system'] is config.SYSTEM]

f = open("state/fronter.txt", "r")
current = int(f.read().strip())
f.close()


f = open("state/stealth.txt", "r")
stealth = int(f.read().strip()) == 1
f.close()

if not (0 <= current < len(list)):
    current = 0

badger.set_update_speed(2)

display.set_pen(15)
display.clear()
display.update()

badger.set_update_speed(3)

update(current)
badger.led(0)

while True:
    machine.Pin(25, machine.Pin.OUT).value(1)
    
    try:
        badger2040w.system_speed(badger2040w.SYSTEM_SLOW)
    except ValueError:
        try:
            badger2040w.system_speed(badger2040w.SYSTEM_NORMAL)
        except ValueError:
            pass
      
    if badger.pressed(badger2040w.BUTTON_C):
        badger.led(128)
        stealth = not stealth
        update(current)
        badger.led(0)
    elif badger.pressed(badger2040w.BUTTON_DOWN):
        badger.led(128)
        if current < len(list) - 1:
            current += 1
        
        update(current)
        badger.led(0)
    elif badger.pressed(badger2040w.BUTTON_UP):
        badger.led(128)
        if current > 0:
            current -= 1
            
        update(current)
        badger.led(0)
    elif badger.pressed(badger2040w.BUTTON_A):
        badger.led(128)
        badger.set_update_speed(0)

        display.set_pen(15)
        
        display.clear()
        display.update()
        
        display.clear()
        display.update()
        
        update(current)

        badger.set_update_speed(3)
        badger.led(0)