class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=[]
        for ac in accounts:
            ans.append(sum(ac))
        return max(ans)