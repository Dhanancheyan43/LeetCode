class Solution(object):
    def largestString(self, nums):
        res=[]
        Z=1<<25
        for x in nums:
            q,r=divmod(x,Z)
            s=['z']*q
            p=24
            while r:
                if r & (1<<p):
                    s.append(chr(ord('a')+p))
                    r-=1<<p
                p-=1
            res.append(''.join(s))
        return res