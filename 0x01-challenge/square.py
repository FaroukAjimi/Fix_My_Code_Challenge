#!/usr/bin/python3
"""square"""


class Square():
    """ class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ init square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area """
        return self.width * self.height

    def permiterofmysquare(self):
        """permiter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ print """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """square w h"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterofmysquare())
