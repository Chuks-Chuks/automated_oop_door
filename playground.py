class Play:
    def __int__(self):
        self.play = self.open()
        self.times_opened = 0

    def open(self):
        self.times_opened += 1
        return self.times_opened


car = Play()
print(car)
