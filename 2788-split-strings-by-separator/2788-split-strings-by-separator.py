class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        res=[]
        for w in words:
            for i in w.split(separator):
                if i:
                    res.append(i)
        return res


