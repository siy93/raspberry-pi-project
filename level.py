
import sys
import wave
import getopt
import alsaaudio
import audioop
import math
import curses
import time
import RPi.GPIO as GPIO
from pygame import mixer

mixer.init()
Do = mixer.Sound("./musicFile/piano/piano_1.ogg")
Le = mixer.Sound("./musicFile/piano/piano_2.ogg")
Mi = mixer.Sound("./musicFile/piano/piano_3.ogg")
Fa = mixer.Sound("./musicFile/piano/piano_4.ogg")
So = mixer.Sound("./musicFile/piano/piano_5.ogg")
Ra = mixer.Sound("./musicFile/piano/piano_6.ogg")
Si = mixer.Sound("./musicFile/piano/piano_7.ogg")
HD = mixer.Sound("./musicFile/piano/piano_8.ogg")

drum1 = mixer.Sound("./musicFile/drum/cl_hihat.ogg")
drum2 = mixer.Sound("./musicFile/drum/claves.ogg")
drum3 = mixer.Sound("./musicFile/drum/conga1.ogg")
drum4 = mixer.Sound("./musicFile/drum/cowbell.ogg")
drum5 = mixer.Sound("./musicFile/drum/crashcym.ogg")
drum6 = mixer.Sound("./musicFile/drum/handclap.ogg")
drum7 = mixer.Sound("./musicFile/drum/hi_conga.ogg")
drum8 = mixer.Sound("./musicFile/drum/hightom.ogg")
drum9 = mixer.Sound("./musicFile/drum/kick1.ogg")
drum10 = mixer.Sound("./musicFile/drum/kick2.ogg")
drum11 = mixer.Sound("./musicFile/drum/maracas.ogg")
drum12 = mixer.Sound("./musicFile/drum/open_hh.ogg")
drum13 = mixer.Sound("./musicFile/drum/rimshot.ogg")
drum14 = mixer.Sound("./musicFile/drum/snare.ogg")
drum15 = mixer.Sound("./musicFile/drum/tom1.ogg")

Bg = mixer.Sound("./musicFile/DJ/Bg.ogg")
B = mixer.Sound("./musicFile/DJ/B.ogg")
TT = mixer.Sound("./musicFile/DJ/TT.ogg")
ZI = mixer.Sound("./musicFile/DJ/ZI.ogg")



def piano():
	stdscr = curses.initscr()
	curses.cbreak()
	quit = False
	device = alsaaudio.PCM(card=card)
	while quit !=True :
	   c = stdscr.getch()
	   print curses.keyname(c),
	   if curses.keyname(c)=="a" :
		Do.play()
		continue
	   elif curses.keyname(c)=="s" :
	        Le.play()
		continue
	   elif curses.keyname(c)=="d" :
	        Mi.play()
		continue
	   elif curses.keyname(c)=="f" :
	        Fa.play()
		continue
	   elif curses.keyname(c)=="g" :
	        So.play()
		continue
	   elif curses.keyname(c)=="h" :
	        Ra.play()
		continue
	   elif curses.keyname(c)=="j" :
	        Si.play()
		continue
	   elif curses.keyname(c)=="k" :
	        HD.play()
		continue
	   elif curses.keyname(c)=="q" :
	        quit=True
		curses.endwin()


def drum():
        stdscr = curses.initscr()
        curses.cbreak()
        quit = False
        device = alsaaudio.PCM(card=card)
        while quit !=True :
           c = stdscr.getch()
           print curses.keyname(c),
           if curses.keyname(c)=="a" :
                drum1.play()
		continue
           elif curses.keyname(c)=="s" :
		drum2.play()
		continue
           elif curses.keyname(c)=="d" :
		drum3.play()
		continue
           elif curses.keyname(c)=="f" :
		drum4.play()
		continue
           elif curses.keyname(c)=="g" :
		drum5.play()
		continue
           elif curses.keyname(c)=="h" :
		drum6.play()
		continue
           elif curses.keyname(c)=="j" :
		drum7.play()	
		continue
           elif curses.keyname(c)=="k" :
		drum8.play()
		continue
           elif curses.keyname(c)=="z" :
                drum9.play()
                continue
           elif curses.keyname(c)=="x" :
                drum10.play()
                continue
           elif curses.keyname(c)=="c" :
                drum11.play()
                continue
           elif curses.keyname(c)=="v" :
                drum12.play()
                continue
           elif curses.keyname(c)=="b" :
                drum13.play()
                continue
           elif curses.keyname(c)=="n" :
                drum14.play()
                continue
           elif curses.keyname(c)=="m" :
                drum15.play()
                continue
           elif curses.keyname(c)=="q" :
                quit=True
                curses.endwin()

def DJ():
        stdscr = curses.initscr()
        curses.cbreak()
        quit = False
        device = alsaaudio.PCM(card=card)
        while quit !=True :
           c = stdscr.getch()
           print curses.keyname(c),
           if curses.keyname(c)=="a" :
                Bg.play()
                continue
           elif curses.keyname(c)=="s" :
                B.play()
                continue
           elif curses.keyname(c)=="d" :
                TT.play()
                continue
           elif curses.keyname(c)=="f" :
                ZI.play()
                continue
           elif curses.keyname(c)=="q" :
                quit=True
                curses.endwin()




def play(device, f):    
    listPin = [4,17,27,22,18,23,24,15]

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

    sys.stdout.write('%d channels, %d sampling rate\n' % (f.getnchannels(),
                                                          f.getframerate()))
    # Set attributes
    device.setchannels(f.getnchannels())
    device.setrate(f.getframerate())

    # 8bit is unsigned in wav files
    if f.getsampwidth() == 1:
        device.setformat(alsaaudio.PCM_FORMAT_U8)
    # Otherwise we assume signed data, little endian
    elif f.getsampwidth() == 2:
        device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    elif f.getsampwidth() == 3:
        device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
    elif f.getsampwidth() == 4:
        device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
    else:
        raise ValueError('Unsupported format')

    device.setperiodsize(320)
    lo  = 2000
    hi = 32000
 
    log_lo = math.log(lo)
    log_hi = math.log(hi)    
    data = f.readframes(320)
    while data:
       	# Read data from stdin
        device.write(data)
       	data = f.readframes(320)
	vuTemp = (math.log(float(max(audioop.max(data, 2),1)))-log_lo)/(log_hi-log_lo)/2
	vu = chr(ord('a')+min(max(int(vuTemp*20),0),19))
	print vu
	volume = 0
    
	if vu == 'd' :
	 	 GPIO.output(17,False)
                 GPIO.output(4,False)
                 GPIO.output(27,False)
                 GPIO.output(22,False)
                 GPIO.output(18,False)
                 GPIO.output(23,False)
                 GPIO.output(24,False)
                 GPIO.output(25,False)
	elif vu == 'e' :
                 GPIO.output(4,True)
                 GPIO.output(17,False)
                 GPIO.output(27,False)
                 GPIO.output(22,False)
                 GPIO.output(18,False)
                 GPIO.output(23,False)
                 GPIO.output(24,False)
                 GPIO.output(25,False)
	elif vu == 'f' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,False)
                 GPIO.output(22,False)
                 GPIO.output(18,False)
                 GPIO.output(23,False)
                 GPIO.output(24,False)
                 GPIO.output(25,False)
	elif vu == 'g' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,True)
                 GPIO.output(22,False)
                 GPIO.output(18,False)
                 GPIO.output(23,False)
                 GPIO.output(24,False)
                 GPIO.output(25,False)
	elif vu == 'h' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,True)
                 GPIO.output(22,True)
                 GPIO.output(18,False)
                 GPIO.output(23,False)
                 GPIO.output(24,False)
                 GPIO.output(25,False)
	elif vu == 'i' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,True)
                 GPIO.output(22,True)
                 GPIO.output(18,True)
                 GPIO.output(23,False)
                 GPIO.output(24,False)
                 GPIO.output(25,False)
	elif vu == 'j' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,True)
                 GPIO.output(22,True)
                 GPIO.output(18,True)
                 GPIO.output(23,True)
                 GPIO.output(24,True)
                 GPIO.output(25,False)
	elif vu == 'k' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,True)
                 GPIO.output(22,True)
                 GPIO.output(18,True)
                 GPIO.output(23,True)
                 GPIO.output(24,True)
                 GPIO.output(25,True)
	elif vu == 'l' :
                 GPIO.output(4,True)
                 GPIO.output(17,True)
                 GPIO.output(27,True)
                 GPIO.output(22,True)
                 GPIO.output(18,True)
                 GPIO.output(23,True)
                 GPIO.output(24,True)
                 GPIO.output(25,True)

def usage():        
    sys.stderr.write('usage: level.py [mode] (mode:piano,drum,music)\n')
    sys.exit(2)

if __name__ == '__main__':

    card = 'default'

    opts, args = getopt.getopt(sys.argv[1:], 'c:')


    if args[0] == 'piano':
       	piano()

    elif args[0] == 'drum':
	drum()

    elif args[0] == 'DJ':
	DJ()
        
    else :
	f = wave.open(args[0], 'rb')
	device = alsaaudio.PCM(card=card)
	play(device, f)
	f.close()
