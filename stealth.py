import json
import jpegdec

def stealth(badger, display):
    # Loading config
    file = open("./stealth.json", "r")
    config = json.loads(file.read())
    file.close()
    print(config)
    
    # Clearing screen
    display.set_pen(15)
    display.clear()
    
    # Name rectangle (outer)
    display.set_pen(0)
    display.rectangle(128, 0, 296, 22)
    display.set_pen(15)
    
    # Name rectangle (name)
    display.set_pen(15)
    display.set_font("bitmap8")
    display.text(config['nickname'], 140, 4, scale=2)
    
    # Name rectangle (pronouns)
    #display.set_pen(15)
    #txt = config['pronouns'][0] + " | " + config['pronouns'][1]
    #display.text(txt, 296 - (8 + (len(txt) * 9)), 4, scale=2)
    
    # Separator lines
    display.set_pen(0)
    display.line(127, 0, 127, 128)
    display.line(128, 103, 295, 103)
    display.line(0, 0, 0, 128)
    display.line(295, 0, 295, 128)
    display.line(0, 0, 295, 0)
    display.line(0, 127, 295, 127)
    
    # Image
    j = jpegdec.JPEG(display)
    j.open_file("stealth.jpeg")
    j.decode(1, 1, jpegdec.JPEG_SCALE_FULL, dither=True)
    
    # Lines (real name)
    j = jpegdec.JPEG(display)
    j.open_file("icons/name.jpg")
    j.decode(91 + 47, 20 + 4, jpegdec.JPEG_SCALE_FULL, dither=False)
    display.set_pen(0)
    display.set_font("bitmap8")
    display.text(config['realname'], 119 + 47, 25 + 4, scale=2)
    
    # Lines (pronouns)
    j = jpegdec.JPEG(display)
    j.open_file("icons/pronouns.jpg")
    j.decode(91 + 47, 45 + 4, jpegdec.JPEG_SCALE_FULL, dither=False)
    display.set_pen(0)
    display.set_font("bitmap8")
    display.text(config['pronouns'], 119 + 47, 50 + 4, scale=2)
    
    # Lines (website)
    j = jpegdec.JPEG(display)
    j.open_file("icons/website.jpg")
    j.decode(91 + 47, 70 + 4, jpegdec.JPEG_SCALE_FULL, dither=False)
    display.set_pen(0)
    display.set_font("bitmap8")
    display.text(config['web'], 119 + 47, 75 + 4, scale=2)
    
    # Quote
    display.set_pen(0)
    display.set_font("bitmap8")
    display.text(config['quote'][0], 12 + 128, 107, scale=1)
    display.text("  " + config['quote'][1], 12 + 128, 117, scale=1)
    
    display.update()