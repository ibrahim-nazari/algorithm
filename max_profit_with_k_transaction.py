
def find_max_profit(k,prices):
    # using dynamic programming to find max profit
    n=len(prices)
    dp=[[0] * n for _ in range(k+1)]

    for t in range(1,k+1):
        max_diff= -prices[0]
        for d in range(1,n):
            dp[t][d]=max(dp[t][d-1],prices[d] + max_diff)
            max_diff =max(max_diff, dp[t-1][d] - prices[d])
    return dp[k][n-1]




def main():
    t=int(input())

    for _ in range(t):
        k=int(input())
        prices=list(map(int,input().split(",")))
        result=find_max_profit(k,prices)
        print(result)



if __name__ =="__main__":
    main()