
from math import sqrt
from ti_system import disp_clr

# QUADFORM - Quadratic Formula

def read(p):
    s=input(p)
    if "/" in s:
        a,b=s.split("/")
        return float(a)/float(b)
    return float(s)

def frac(x):
    if abs(x)<0.00000001:
        return "0"

    sign=""
    if x<0:
        sign="-"
        x=-x

    bn=round(x)
    bd=1
    err=abs(x-bn)

    for d in range(1,1001):
        n=round(x*d)
        e=abs(x-n/d)
        if e<err:
            bn=n
            bd=d
            err=e
        if err<0.00000001:
            break

    if bd==1:
        return sign+str(bn)
    return sign+str(bn)+"/"+str(bd)

def pause():
    input("ENTER")

def solve():
    disp_clr()
    print("QUADRATIC FORMULA")
    print("ax^2+bx+c=0")
    print("")
    a=read("a: ")
    b=read("b: ")
    c=read("c: ")

    if a==0:
        disp_clr()
        print("ERROR: a=0")
        pause()
        return

    d=b*b-4*a*c

    disp_clr()
    print("=== RESULTS ===")
    print("DISCRIMINANT:")
    print(frac(d))
    print("")

    if d<0:
        print("NO REAL ROOTS")
        print("Complex solutions")
        pause()
        return

    if d==0:
        x=-b/(2*a)
        print("ONE REAL ROOT:")
        print("x="+frac(x))
        pause()
        return

    r=sqrt(d)
    x1=(-b-r)/(2*a)
    x2=(-b+r)/(2*a)

    print("TWO REAL ROOTS:")
    print("x1="+frac(x1))
    print("x2="+frac(x2))
    pause()

    disp_clr()
    print("DECIMAL VALUES:")
    print("x1="+str(round(x1,6)))
    print("x2="+str(round(x2,6)))
    pause()

while True:
    solve()
    disp_clr()
    c=input("Again? Y/N: ")
    if c.upper()!="Y":
        break
