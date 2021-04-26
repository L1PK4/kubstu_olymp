n, m = tuple(map(int, input().split()))

def dfs(arr, i, j, color):
    arr[i][j] = color
    for di in range(-1,2):
        for dj in range(-1,2):
            i1 = (i + di) % n
            j1 = (j + dj) % m
            if (arr[i1][j1] == 1) and (abs(dj) + abs(di) != 2):
                dfs(arr, i1, j1, color)
arr = [list(map(int, input().split(maxsplit=m))) for _ in range(n)]
clr = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            clr += 1
            dfs(arr, i, j, clr)
print(clr - 1)