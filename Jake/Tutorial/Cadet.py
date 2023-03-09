class Cadet:
    def __init__(self, name, major, gpa, demirits, command_position):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.demerits = demirits
        self.command_position = command_position

    def on_ac_pro(self):
        if self.gpa <= 3.0:
            return True
        else:
            return False