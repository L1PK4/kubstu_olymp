def getm(n):
    return [list(map(int, input().split())) for _ in range(n)]

def check(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i] and i != j:
                return 'NO'
    return 'YES'

n = int(input())
arr = getm(n)
print(check(arr))