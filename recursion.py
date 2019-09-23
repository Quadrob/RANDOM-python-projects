from functools import lru_cache

@lru_cache(1000)
def recursion_dp(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return recursion_dp(n - 1) + recursion_dp(n - 2)
    
for n in range(1, 500):
    print (str(recursion_dp(n)) + "\n")