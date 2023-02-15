from random import randint

class Rgb:
    i = 0
    e = 255

    def random_rgb(self):
        r = randint(self.i, self.e)
        g = randint(self.i, self.e)
        b = randint(self.i, self.e)
        return r, g, b

    def random_rgb2(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b
