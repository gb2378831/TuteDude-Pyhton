#map
# map(functions,iterable)

def squares(a):
        return a**2

numbers = [1,2,3,4,5]

ans = list(map(squares,numbers))
print(ans)