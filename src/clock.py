import datetime

class DateTime:
    def __init__(self):
        self.date = datetime.datetime.now()

    def hour(self):
        return self.date.strftime("%H")

    def minute(self):
        return self.date.strftime("%M")

    def second(self):
        if (self.date.second %2 == 0):
            return ':'
        return ' '

    def day(self):
        return self.date.strftime("%A")

    def fullDate(self):
        return str(self.date.day) + self.suffix( self.date.day )+self.date.strftime(" %B %Y")

    def suffix(self,d):
        return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
