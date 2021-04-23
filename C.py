def summ(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

n, k = tuple(map(int, input().split()))
ans = list(filter(lambda x : not (summ(x) % k), range(1, n + 1)))
print(len(ans))