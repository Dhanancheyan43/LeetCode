class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A,B=nums1,nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        half = (m + n + 1) // 2
        INF = float('inf')
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2 
            j = half - i 
            aL = A[i - 1] if i > 0 else -INF
            aR = A[i]     if i < m else INF
            bL = B[j - 1] if j > 0 else -INF
            bR = B[j]     if j < n else INF
            if aL <= bR and bL <= aR:
                if (m + n) & 1:
                    return float(max(aL, bL))
                return (max(aL, bL) + min(aR, bR)) / 2
            elif aL > bR:
                hi = i - 1
            else:
                lo = i + 1