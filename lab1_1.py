from gpiozero import MotionSensor, LED
from person_detector import start_video
led = LED(17)
led.off()
pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print('detected')
    led.on()
    start_video()
    pir.wait_for_no_motion()
    print('not')
    led.off()