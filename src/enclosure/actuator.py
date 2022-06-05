class Actuador(object):
    def __init__(self, enclosure, isFilament = False):
        self.status = 0
        self.isFilament = isFilament
        self.enclosure = enclosure
    
    def set_status(self, value):
        self.status = value


class Fan(Actuador):
    def __init__(self, enclosure, isFilament=False):
        super().__init__(enclosure, isFilament)

    def activate(self):
        self.enclosure.fan.set_status(1)

    def deactivate(self):
        self.set_status(0)



class Gate(Actuador):
    def __init__(self, enclosure, isFilament=False):
        super().__init__(enclosure, isFilament)

    def open(self):
        self.set_status(1)

    def close(self):
        self.set_status(0)

