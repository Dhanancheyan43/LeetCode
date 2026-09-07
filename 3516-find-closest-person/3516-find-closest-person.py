class Solution(object):
    def findClosest(self, x, y, z):
        m,n=abs(x-z),abs(y-z)
        if m<n:
            return 1
        elif m>n:
            return 2
        return 0
        