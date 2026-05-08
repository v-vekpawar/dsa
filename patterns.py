# ----1----
def p1_0(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

def p1_1(n):
    for i in range(n):
        print("*"*(n))

# ----2----
def p2_0(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()

def p2_1(n):
    for i in range(n):
        print("*"*(i+1))

# ----3----
def p3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        print()

# ----4----
def p4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print()

# ----5----
def p5(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print()

# ----6----
def p6(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(j+1,end="")
        print()

# ----7----
def p7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()

# ----8----
def p8(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        for l in range(n-i):
            print(" ",end="")
        print()

# ----9----


# ----10----


# ----11----


# ----12----




def run_all(n):
    print("Pattern 1.0")
    p1_0(n)
    print()
    print("Pattern 1.1")
    p1_1(n)
    print()
    print("Pattern 2.0")
    p2_0(n)
    print() 
    print("Pattern 2.1")
    p2_1(n)
    print()
    print("Pattern 3")
    p3(n)
    print()
    print("Pattern 4")
    p4(n)
    print()
    print("Pattern 5")
    p5(n)
    print()
    print("Pattern 6")
    p6(n)
    print()
    print("Pattern 7")
    p7(n)
    print()
    print("Pattern 8")
    p8(n)
    print()

# if __name__ == "__main__":
#     n = int(input("Enter the number of rows: "))
#     run_all(n)