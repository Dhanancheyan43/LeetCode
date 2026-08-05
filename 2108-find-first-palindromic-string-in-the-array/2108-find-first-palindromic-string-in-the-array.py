class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans=""
        for w in words:
            if w==w[::-1]:
                ans=w
                break
        return ans