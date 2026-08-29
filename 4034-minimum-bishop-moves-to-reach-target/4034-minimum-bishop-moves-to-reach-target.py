class Solution(object):
    def minBishopMoves(self, source, target):
        r,c=source
        tr,tc=target
        if source==target:
            return 0
        if (r-c)%2!=(tr-tc)%2:
            return -1
        if abs(r-tr)==abs(c-tc):
            return 1
        return 2
