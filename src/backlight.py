from threading import Timer

class Backlight:
    def __init__(self,delay):
        self.data = []
        self.state = 'on'
        self.delay = delay
        self.lightTimer = None

    def on(self):
        self.state = 'on'
        print("Backlight on")
        self.lightTimer = Timer(self.delay, self.off)
        self.lightTimer.start()
        print("starting timer")

    def off(self):
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