class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        for i ,words in enumerate(words):
            if x in words:
                res.append(i)
        return res