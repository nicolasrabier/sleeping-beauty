from gpiozero import SmoothedInputDevice

sensor = SmoothedInputDevice(17,)


print("=== start test ===")

sensor._queue.start()
print("Sensor Active: ", sensor.is_active)

sensor.wait_for_inactive(1)
print("after wait for inactive")

sensor.wait_for_active(1)
print("after wait for active")
