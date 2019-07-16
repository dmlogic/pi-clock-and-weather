import datetime

class DateTime:
    lastMinute = 99
    lastHour = 99
    date = None

    def reset(self):
        self.lastMinute = 99
        self.lastHour = 99

    def theTime(self):
        self.date = datetime.datetime.now()
        return self.date

    def isNewMinute(self):
        self.theTime()
        minute = self.date.minute
        if(minute == self.lastMinute):
            ret = False
        else:
            ret = True
        self.lastMinute = minute
        return ret

    def isNewHour(self):
        self.theTime()
        if(self.date.hour == self.lastHour):
            ret = False
        else:
            ret = True
        self.lastHour = self.date.hour
        return ret

    def hour(self):
        self.theTime()
        return self.date.strftime("%H")

    def minute(self):
        return self.theTime().strftime("%M")

    def day(self):
        return self.theTime().strftime("%A")

    def fullDate(self):
        d = self.theTime()
        return str(d.day) + self.suffix( d.day )+d.strftime(" %B %Y")

    def suffix(self,d):
        return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
