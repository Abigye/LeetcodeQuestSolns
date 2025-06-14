def factorial (n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)
# tc=0(n), sc = 0(n)

def factorial_dp(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


print(factorial(5))
print(factorial(1))
print(factorial(0))
# print(factorial(4000))
# print(factorial_dp(4000))


