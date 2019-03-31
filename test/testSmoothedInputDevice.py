from gpiozero import SmoothedInputDevice
from time import sleep

sensor = SmoothedInputDevice(17,pull_up=True,queue_len=1,sample_wait=0.0)

print("=== start test ===")
print("Queue Starts")
sensor._queue.start()

print("Sensor Active: ", sensor.is_active)
print("Sensor value:", sensor.value)

previousvalue = 0
while True:
	currentvalue = sensor.value
	if currentvalue != previousvalue:
		# print("Sound detected!" if currentvalue == 1 else "------------------")
		if currentvalue == 1:
			print("Sound detected!")
			sleep(3)
		else:
			print("------------------")
	previousvalue=currentvalue
