from gpiozero import SmoothedInputDevice
from time import sleep

sensor = SmoothedInputDevice(17,pull_up=True,queue_len=1,sample_wait=0.0)

sensor._queue.start()

def listen():
    
    previousvalue = 0
    while True:
        currentvalue = sensor.value
        if currentvalue != previousvalue:
            # print("Sound detected!" if currentvalue == 1 else "------------------")
            if currentvalue == 1:
                #play music only if music is not playing yet            
                print("Sound detected!")
                sleep(3)
            else:
                print("------------------")
        previousvalue=currentvalue
    
    # sensor._queue.stop()
    
    
    #import pygame
    # Load and play the music
    #    pygame.mixer.init()
    #    pygame.mixer.music.load("xmas.mp3")
    #    pygame.mixer.music.play()
    
def stop():    
    sensor._queue.stop()
    
    