from gpiozero import MotionSensor

pir = MotionSensor(17)
i = 1

while True:
	pir.wait_for_motion()
	print(i, " - Motion detected!")
	i = i + 1

