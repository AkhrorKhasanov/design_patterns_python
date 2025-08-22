class TV:
    def turn_on(self):
        pass

class SamsungTV(TV):
    def turn_on(self):
        print("Turning on Samsung")

class LGTV(TV):
    def turn_on(self):
        print("Turning on LGTV")

class RemoteControl:
    def __init__(self, tv):
        self.tv = tv

    def press_power_button(self):
        self.tv.turn_on()


samsung = SamsungTV()
lg = LGTV()

remote1 = RemoteControl(samsung)
remote2 = RemoteControl(lg)

remote1.press_power_button()
remote2.press_power_button()