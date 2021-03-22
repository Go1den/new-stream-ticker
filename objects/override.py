class Override:
    def __init__(self, duration: str = "", intermission: str = "", scrollSpeed: str = "",
                 font: str = "", fontSize: str = "", fontColor: str = "", arrival: str = "", departure: str = "",
                 bold: bool = False, overstrike: bool = False):
        self.duration = duration
        self.intermission = intermission
        self.scrollSpeed = scrollSpeed
        self.font = font
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.arrival = arrival
        self.departure = departure
        self.bold = bold
        self.overstrike = overstrike

    def print(self):
        print("Override:")
        print("Duration: " + self.duration)
        print("Intermission: " + self.intermission)
        print("Scroll Speed: " + self.scrollSpeed)
        print("Font: " + self.font)
        print("Font Size: " + self.fontSize)
        print("Font Color: " + self.fontColor)
        print("Arrival: " + self.arrival)
        print("Departure: " + self.departure)
        print("Bold: " + str(self.bold))
        print("Overstrike: " + str(self.overstrike))
