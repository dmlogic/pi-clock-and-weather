import os
from threading import Timer

class Backlight:
    state = 'on'
    def __init__(self,delay):
        self.data = []
        self.delay = delay
        self.lightTimer = None

    def on(self):
        self.state = 'on'
        print("Backlight on")
        os.system("bash -c \"echo 0 | sudo tee /sys/class/backlight/rpi_backlight/bl_power\"")
        # echo 0 | sudo tee /sys/class/backlight/rpi_backlight/bl_power
        self.lightTimer = Timer(self.delay, self.off)
        self.lightTimer.start()
        print("starting timer")

    def off(self):
        os.system("bash -c \"echo 1 | sudo tee /sys/class/backlight/rpi_backlight/bl_power\"")
        # echo 1 | sudo tee /sys/class/backlight/rpi_backlight/bl_power
        self.state = 'off'
        print("Backlight off")

    def toggle(self):
        if(isinstance(self.lightTimer,Timer)):
            print("cancelling timer")
            self.lightTimer.cancel()

        if(self.state == 'on'):
            self.off()
        else:
            self.on()