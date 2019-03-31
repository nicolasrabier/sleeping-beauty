from gpiozero import LightSensor

ldr = LightSensor(17)
ldr.wait_for_light()
print("Sound detected!")