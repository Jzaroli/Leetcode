"""
You are given an array prices where prices[i] is the stock price on the i-th
day. Find the maximum profit you can achieve by buying and selling once.

🔴 You cannot sell before you buy.
🔴 If no profit is possible, return 0.
"""

# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Input: prices = [7,6,4,3,1]
# Output: 0

prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    min_price = float('inf')  # Set min_price to a very high value
    max_profit = 0  # Initialize max profit to 0

    for price in prices:
        if price < min_price:  # Update min_price if we find a lower price
            min_price = price
        profit = price - min_price  # Calculate profit
        max_profit = max(max_profit, profit)  # Update max profit

    return max_profit  # Return the highest profit found


profit = maxProfit(prices)
print(profit)
