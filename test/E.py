def getm(m, n):
    return [list(map(int, input().split(maxsplit=n))) for _ in range(m)]


m, n = tuple(map(int, input().split()))
arr = getm(m, n)
minarr = list(map(min, arr))
print(minarr.index(max(minarr)) + 1)