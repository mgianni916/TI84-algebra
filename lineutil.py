
from ti_system import disp_clr

def n(x):
    if abs(x)<0.0000001:
        x=0
    return str(round(x,5))

def pause():
    input("ENTER")

def solve(perp):
    disp_clr()
    if perp:
        print("PERPENDICULAR")
    else:
        print("PARALLEL")

    print("POINT:")
    x=float(input("x: "))
    y=float(input("y: "))

    print("ORIGINAL LINE:")
    m=float(input("Slope m: "))

    if perp:
        if m==0:
            disp_clr()
            print("RESULT:")
            print("x="+n(x))
            print("Vertical line")
            pause()
            return
        m=-1/m

    b=y-m*x

    disp_clr()
    print("=== RESULT ===")
    print("SLOPE: "+n(m))
    print("Y-INT: "+n(b))
    print("")
    print("SLOPE-INTERCEPT:")
    print("y="+n(m)+"x"+
          ("+" if b>=0 else "")+n(b))
    pause()

    disp_clr()
    print("POINT-SLOPE:")
    print("y-("+n(y)+")=")
    print(n(m)+"(x-("+n(x)+"))")
    pause()

def main():
    while True:
        disp_clr()
        print("LINE UTILITY")
        print("--------------")
        print("1 PARALLEL")
        print("2 PERPENDICULAR")
        print("3 EXIT")

        c=input("SELECT: ")

        try:
            if c=="1":
                solve(False)
            elif c=="2":
                solve(True)
            elif c=="3":
                break
        except (ValueError,ZeroDivisionError):
            disp_clr()
            print("INVALID INPUT")
            pause()

main()
