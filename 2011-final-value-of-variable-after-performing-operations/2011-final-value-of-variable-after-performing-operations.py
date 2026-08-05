class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for o in operations:
            if "+" in o:
                x+=1
            elif "-" in o:
                x-=1
        return x