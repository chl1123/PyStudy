"""
适配器
"""
import math


class RoundHole(object):
    def __init__(self, radius):
        self.radius = radius

    def round_hole(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()


class RoundPeg(object):
    def __init__(self, radius):
        self.radius = radius

    def round_peg(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius


class SquarePeg(object):
    def __init__(self, width):
        self.width = width

    def square_peg(self, width):
        self.width = width

    def get_width(self):
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg):
        round_peg = peg.get_width() * math.sqrt(2) / 2
        super().__init__(round_peg)
        self.round_peg = round_peg

    def get_radius(self):
        return self.round_peg


if __name__ == '__main__':
    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    if hole.fits(rpeg):
        print('Round peg r5 fits round hole r5')

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    if hole.fits(small_sqpeg_adapter):
        print('Square peg w5 fits round hole r5')
    if not hole.fits(large_sqpeg_adapter):
        print('Square peg w10 does not fit into round hole r5')
