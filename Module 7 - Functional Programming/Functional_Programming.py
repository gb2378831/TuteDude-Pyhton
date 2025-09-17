def add(i,j):
    return i + j
def call(i,j):
    return add(i,j)
def pas(i,j,fn):
    return fn(i,j)


# a = add
# res = a(1,2)
# print(res)

res = call(1,2)
print(res)

res = pas(1,2,call)
print(res)


