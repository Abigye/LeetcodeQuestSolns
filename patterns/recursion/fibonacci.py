def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
#  Time: O(2ⁿ) — exponential!
# Repeats the same subproblems multiple times

# Space: O(n) — call stack depth
# Bad for n > 30

def fibnocci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
# Time: O(n)
# Space: O(n) (DP table)


def fib_with_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_with_memo(n-1, memo) + fib_with_memo(n-2, memo)
    return memo[n]
# Time: O(n)
# Each fib(n) computed only once
# Space: O(n) (call stack + memo dictionary)


def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
# Time: O(n)
# Space: O(1) — only stores two previous result

print(fib(3))

# print(f(5))
# print(factorial(1))
# print(factorial(0))