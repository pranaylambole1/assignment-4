
def rod_cutting(price, n):
    # Create a DP array
    dp = [0] * (n + 1)

    # Calculate maximum profit for each length
    for i in range(1, n + 1):
        max_profit = 0

        for j in range(1, i + 1):
            max_profit = max(
                max_profit,
                price[j - 1] + dp[i - j]
            )

        dp[i] = max_profit

    return dp[n]


# Example
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

result = rod_cutting(price, n)

print("Maximum Profit:", result)
