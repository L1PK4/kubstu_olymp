def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a, b = tuple(map(int, input().split()))
d = gcd(a,b)
print(a // d, b // d)