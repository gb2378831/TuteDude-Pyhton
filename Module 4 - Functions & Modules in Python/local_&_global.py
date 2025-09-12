n = 1   # GLOBAL VARIABLE

def fn():
    global n
    n = 5       # LOCAL VARIABLE
    print('in', n)

fn()


print('out',n)

'''local variable has been prefered in higher position than the global variable'''