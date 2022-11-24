class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        x_rect1 = set([])
        for i in range(ax1, ax2 + 1):
            x_rect1.add(i)
        x_rect2 = set([])
        for i in range(bx1, bx2 + 1):
            x_rect2.add(i)

        y_rect1 = set([])
        for i in range(ay1, ay2 + 1):
            y_rect1.add(i)
        y_rect2 = set([])
        for i in range(by1, by2 + 1):
            y_rect2.add(i)

        y_shared = y_rect1.intersection(y_rect2)
        x_shared = x_rect1.intersection(x_rect2)
        print(x_rect1)
        print(x_rect2)
        print(y_rect1)
        print(y_rect2)
        a_size = abs(ax2 - ax1) * abs(ay2 - ay1)
        b_size = abs(bx2 - bx1) * abs(by2 - by1)

        goo = 0
        gaa = 0
        if len(x_shared) > 0:
            goo = len(x_shared) - 1
        if len(y_shared) > 0:
            gaa = len(y_shared) - 1
        print("a size: " + str(a_size))
        print("b size: " + str(b_size))
        print("shared: " + str(x_shared))

        return a_size + b_size - (goo * gaa)
