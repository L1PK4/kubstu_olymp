def getm(n, m):
    return [list(map(int, input().split(maxsplit=m))) for _ in range(n)]
n, m  = tuple(map(int, input().split()))
arr = getm(n, m)
ans = 0
for i in range(m):
    temp = 0
    for j in range(n):
        temp += arr[j][i]
    ans += temp & 0b1
print(ans)