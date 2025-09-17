# Filter
# filter (function, iterable)

'''def even(a):
    return a%2==0


numbers = [1,2,3,4,5,6,7]

ans = list(filter(even,numbers))
print(ans)'''

ans = set(filter(lambda a : a%2==0,range(11)))
print(ans)