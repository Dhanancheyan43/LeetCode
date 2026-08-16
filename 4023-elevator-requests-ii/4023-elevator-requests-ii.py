class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        a = sorted(requests)
        m = len(a)
        INF = float('inf')

        dp = [[[INF, INF] for _ in range(m)] for _ in range(m)]

        for i in range(m):
            dp[i][i][0] = dp[i][i][1] = abs(start - a[i]) * m

        for length in range(2, m + 1):
            for l in range(m - length + 1):
                r = l + length - 1
                rem = m - (r - l)  

                dp[l][r][0] = min(dp[l+1][r][0] + (a[l+1] - a[l]) * rem,dp[l+1][r][1] + (a[r] - a[l]) * rem)

                dp[l][r][1] = min(dp[l][r-1][0] + (a[r] - a[l]) * rem,dp[l][r-1][1] + (a[r] - a[r-1]) * rem)

        return min(dp[0][m-1][0], dp[0][m-1][1])