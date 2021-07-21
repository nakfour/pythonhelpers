class MinSub(object):
    def __init__(self):
        print("MinSub")
    def findMinimium(self, a):
        a.sort()
        print(list(zip(a, a[1:])))
        return min(abs(x - y) for x, y in zip(a, a[1:]))