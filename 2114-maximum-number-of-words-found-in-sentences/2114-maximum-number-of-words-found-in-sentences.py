class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=[]
        for s in sentences:
            ans.append(len(s.split()))
        return max(ans)