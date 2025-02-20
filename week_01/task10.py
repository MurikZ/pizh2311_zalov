"""This module is designed to calculate the surface area
of the treated surface and
the number of necessary rolls of wallpaper."""

class WinDoor:
    """The class for storing the square of a rectangle that is not being
    processed.
    The constructor takes the length and width, the object is assigned "square"
    field."""
    def __init__(self, w, h):
        self.square = w * h

class Room:
    """This class creates rooms."""
    def __init__(self, l, w, h):
        """The constructor takes the dimensions of the room."""
        self.length = l
        self.width = w
        self.height = h
        self.wd = []

    def addWD(self, w, h):
        """The method adds an object of WinDoor."""
        self.wd.append(WinDoor(w, h))

    def fullSurface(self):
        """The method calculates the full square of walls."""
        return 2 * self.height * (self.length + self.width)

    def workSurface(self):
        """The method calculates the square of the walls that being
        processed."""
        new_square = self.fullSurface()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def wallpapers(self, l, w):
        """The method determines the number of required rolls."""
        return int(self.workSurface() / (w * l)) + 1