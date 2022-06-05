class Actuador(object):
    def __init__(self, enclosure):
        self.status = 0
        self.enclosure = enclosure
    
    def set_status(self, value):
        self.status = value


class Fan(Actuador):
    def __init__(self, enclosure):
        super().__init__(enclosure)

    def activate(self):
        self.enclosure.fan.set_status(1)

    def deactivate(self):
        self.set_status(0)



class Gate(Actuador):
    def __init__(self, enclosure):
        super().__init__(enclosure)

    def open(self):
        self.set_status(1)

    def close(self):
        self.set_status(0)

