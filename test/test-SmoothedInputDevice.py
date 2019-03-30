from gpiozero import SmoothedInputDevice
from time import sleep

sensor = SmoothedInputDevice(17,pull_up=True,queue_len=1,sample_wait=0.0)


print("=== start test ===")

sensor._queue.start()
print("Sensor Active: ", sensor.is_active)

print("Sensor value:", sensor.value)

sensor.wait_for_inactive(1)
print("after wait for inactive")


print("Sensor value: ", sensor.value)

sensor.wait_for_active(1)
print("after wait for active")

previousvalue = 0
while True:
	currentvalue = sensor.value
	if currentvalue != previousvalue:
		print("Value:", currentvalue, "Sound detected!" if currentvalue == 1 else "------------------")
		sleep(2)
	previousvalue=currentvalue
