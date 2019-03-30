from gpiozero import SmoothedInputDevice 

print('=======')

sensor = SmoothedInputDevice(17)
sensor.is_active()
print('Sound detected')
