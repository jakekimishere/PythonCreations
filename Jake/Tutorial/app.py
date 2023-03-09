from Chef import Chef

myChef = Chef()
myChef.make_clam_chowder()

class MilitaryChef(Chef):

    def make_cadets_happy(self):
        print("The military chef makes cadets happy")

myChef = MilitaryChef
myChef.make_cadets_happy()