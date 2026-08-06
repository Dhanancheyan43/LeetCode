class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans=""
        for w in words:
            ans+=(w[0])
        return (ans==s)
      