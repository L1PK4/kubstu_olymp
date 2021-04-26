def five_counter(a):
    ans = 0
    while a:
        if not a%5:
            ans += 1
            a //= 5
        else:
            a = 0
    return ans
n = int(input())
ans = 0
for i in range(5, n + 1, 5):
    ans += five_counter(i)
print(ans)