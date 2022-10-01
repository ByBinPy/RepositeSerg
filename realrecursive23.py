global x
def f(n,end):
    if n == end:
        return 1
    if n > end:
        return 0
    x = n
    if n % 100//10<9:
        x+=10
    return f(n+1,end)+f(x,end)
def f_1(n,end):
    if n == end:
        return 1
    if n > end:
        return 0
    x = n
    if n % 100//10<9:
        x+=10
    return f(n+1,end)+f(x,end)
print(f_1(91,100))
