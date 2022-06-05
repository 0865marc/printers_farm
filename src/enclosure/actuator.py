

class Actuador(object):
    def __init__(self, printer_id, isFilament = False):
        self.status = 0
        self.id = printer_id
        self.isFilament = isFilament
    
    def set_status(self, value):
        self.status = value


class Fan(Actuador):
    def __init__(self, printer_id, isFilament=False):
        super().__init__(printer_id, isFilament)

    def activate(self):
        if self.isFilament:
            self.msg = f"Filament: Activating fan {self.id}"
        else:
            self.msg = f"Activating fan printer {self.id}"
        self.set_status(1)

    def deactivate(self):
        if self.isFilament:
            self.msg = f"Filament: Deactivating fan filament {self.id}"
        else:
            self.msg = f"Deactivating fan printer {self.id}"
        self.set_status(0)


class Gates(Actuador):
    def __init__(self, printer_id, isFilament=False):
        super().__init__(printer_id, isFilament)

    def activate(self):
        if self.isFilament:
            self.msg = f"Filament: Opening gates {self.id}"
        else:
            self.msg = f"Opening gates printer {self.id}"
        self.set_status(1)

    def deactivate(self):
        if self.isFilament:
            self.msg = f"Filament: Closing gates {self.id}"
        else:
            self.msg = f"Closing gates printer {self.id}"
        self.set_status(0)

