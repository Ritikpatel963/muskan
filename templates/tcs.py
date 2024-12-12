def minCost(arr, n):
    if (n < 3):
        print(arr[0])
        return

    # Store the results in table
    dp = [0] * n
 
    # Initialize base cases
    dp[0] = arr[0]
    dp[1] = dp[0] + arr[1] + arr[2]
 
    # Iterate over the range[2, N - 2]
    # to construct the dp array
    for i in range(2, n - 1):
        dp[i] = min(dp[i - 2] + arr[i],
                    dp[i - 1] + arr[i]
                    + arr[i + 1])
 
    # Handle case for the last index, i.e. N - 1
    dp[n - 1] = min(dp[n - 2],
                    dp[n - 3] + arr[n - 1])\
 
    # Print the answer
    print(dp[n - 1])
 
# Driver Code
# if _name_ == "_main_":
 
lst = []
n =int(input())
# for i in range(0, n):
#     ele = int(input())
#     lst.append(ele)
lst  = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
minCost(lst,n)