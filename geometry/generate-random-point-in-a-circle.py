from random import random as rand
from math import sin, cos, pi, sqrt
class Solution:

    def __init__(self, radius: float, x_center: float = 0, y_center: float = 0):
        self.x = x_center
        self.y = y_center
        self.r = abs(radius)

    def randPoint(self) -> List[float]:
        thet = rand()*(2*pi)
        dis = sqrt(rand())*self.r
        return [self.x + dis*cos(thet), self.y + dis*sin(thet)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()