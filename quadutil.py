
from math import sqrt
from ti_system import disp_clr

def n(x):
    return str(round(x,4))

def pause():
    input("ENTER")

def eq(a,b,c,h,k):
    disp_clr()
    print("=== EQUATIONS ===")
    print("STANDARD:")
    print("y=",end="")
    print(n(a)+"x^2",end="")
    if b!=0:
        print(("+" if b>0 else "")+n(b)+"x",end="")
    if c!=0:
        print(("+" if c>0 else "")+n(c),end="")
    print()

    print("VERTEX:")
    print("y="+n(a)+"(x"+("-" if h>=0 else "+")+n(abs(h))+")^2"+("+" if k>=0 else "")+n(k))

    d=b*b-4*a*c
    print("FACTORED:")
    if d<0:
        print("No real factors")
    else:
        r=sqrt(max(0,d))
        x1=(-b-r)/(2*a)
        x2=(-b+r)/(2*a)
        print("y="+n(a)+"(x"+("-" if x1>=0 else "+")+n(abs(x1))+")(x"+("-" if x2>=0 else "+")+n(abs(x2))+")")

    pause()

    disp_clr()
    print("=== POINTS ===")
    print("VERTEX:")
    print("("+n(h)+","+n(k)+")")
    print("Y-INTERCEPT:")
    print("(0,"+n(c)+")")
    print("X-INTERCEPTS:")
    if d<0:
        print("None")
    elif d==0:
        print("("+n(h)+",0)")
    else:
        print("("+n(x1)+",0)")
        print("("+n(x2)+",0)")

    pause()

    disp_clr()
    print("=== PROPERTIES ===")
    print("AXIS: x="+n(h))
    if a>0:
        print("OPENS: UP")
        print("MIN: "+n(k))
    else:
        print("OPENS: DOWN")
        print("MAX: "+n(k))
    pause()

def main():
    while True:
        disp_clr()
        print("QUADRATIC UTILITY")
        print("1 FROMSTD")
        print("2 FROMVERT")
        print("3 FROMINT")
        print("4 FROM3PTS")
        print("5 EXIT")
        m=input("SELECT: ")

        if m=="5":
            break

        try:
            if m=="1":
                disp_clr()
                print("FROMSTD")
                a=float(input("a: "))
                b=float(input("b: "))
                c=float(input("c: "))

            elif m=="2":
                disp_clr()
                print("FROMVERT")
                h=float(input("h: "))
                k=float(input("k: "))
                x=float(input("x: "))
                y=float(input("y: "))
                if x==h:
                    raise ValueError
                a=(y-k)/(x-h)**2
                b=-2*a*h
                c=a*h*h+k

            elif m=="3":
                disp_clr()
                print("FROMINT")
                c=float(input("Y-int: "))
                r1=float(input("X1: "))
                r2=float(input("X2: "))
                if r1*r2==0:
                    raise ValueError
                a=c/(r1*r2)
                b=-a*(r1+r2)

            elif m=="4":
                disp_clr()
                print("FROM3PTS")
                x1=float(input("X1: "))
                y1=float(input("Y1: "))
                x2=float(input("X2: "))
                y2=float(input("Y2: "))
                disp_clr()
                x3=float(input("X3: "))
                y3=float(input("Y3: "))
                m1=(y2-y1)/(x2-x1)
                m2=(y3-y2)/(x3-x2)
                a=(m2-m1)/(x3-x1)
                b=m1-a*(x1+x2)
                c=y1-a*x1*x1-b*x1

            else:
                continue

            if a==0:
                raise ValueError

            h=-b/(2*a)
            k=a*h*h+b*h+c
            eq(a,b,c,h,k)

        except (ValueError,ZeroDivisionError):
            disp_clr()
            print("INVALID INPUT")
            pause()

main()
