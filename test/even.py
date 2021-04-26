def even(n):
    return not (n & 0b1)
while True:    
    print(even(int(input())))