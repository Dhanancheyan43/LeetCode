class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n,m=len(skill),len(station)
        if n<=1:
            return 0
        pre=[-1]*(n+1)
        pos=-1
        for i in range(n):
            j=pos+1
            while station[j]!=skill[i]:
                j+=1
            pos=j
            pre[i+1]=pos
        suf=[m]*(n+1)
        pos=m
        for i in range(n-1,-1,-1):
            j=pos-1
            while station[j]!=skill[i]:
                j-=1
            pos=j
            suf[i]=pos
        return max(suf[i]-pre[i] for i in range(1,n))
            