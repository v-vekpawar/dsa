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
def p9(n):
    p7(n)
    p8(n)

# ----x----
def px(n):
    for i in range((n//2)+1):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()
    for i in range((n//2),0,-1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        for l in range(n-i):
            print(" ",end="")
        print()

# ----10----
def p10_1(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end="")
        print()

def p10_2(n):
    for i in range(1,2*n):
        stars=i if i<=n else 2*n-i
        for j in range(stars):
            print("*",end="")
        print()

# ----11----
def p11(n):
    for i in range(n):
        start=1 if i%2==0 else 0
        for j in range(i+1):
            print(start,end="")
            start=1-start
        print()

# ----12----
def p12(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end="")
        for k in range((2*(n-i-1)),0,-1):
            print(" ",end="")
        for l in range(i+1,0,-1):
            print(l,end="")
        print()

# ----13----
def p13(n):
    x=1
    for i in range(n):
        for j in range(i+1):
            print(x,end=" ")
            x+=1
        print()

# ----14----
def p14(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end=" ")
        print()

# ----15----
def p15(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j),end=" ")
        print()

# ----16----
def p16(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print()

# ----17----
def p17_1(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            if k<=((2*i+1)//2):
                print(chr(65+k),end="")
            else:
                print(chr(65-(k-(2*i))),end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()

def p17_2(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        ch = ord('A')
        break_point = (2*i+1)//2
        for k in range(2*i+1):
            print(chr(ch),end="")
            if k < break_point:
                ch += 1
            else:
                ch -= 1
        print()

# ----18----
def p18_1(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j+(n-i-1)),end=" ")
        print()

def p18_2(n):
    for i in range(n):
            # Print characters from ('A' + N - 1 - i) to ('A' + N - 1)
            for ch in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(ch), end=" ")
            # Move to next line after each row
            print()

# ----19----
def p19(n):
    for i in range(n-1, -1, -1):
        left = "*" * (i + 1)
        spaces = " " * (2 * (n - i - 1))
        right = "*" * (i + 1)
        print(left + spaces + right)
    for i in range(n):
        left = "*" * (i + 1)
        spaces = " " * (2 * (n - i - 1))
        right = "*" * (i + 1)
        print(left + spaces + right)   

# ----20----
def p20(n):
    for i in range(n):
        left = "*" * (i + 1)
        spaces = " " * (2 * (n - i - 1))
        right = "*" * (i + 1)
        print(left + spaces + right)
    for i in range(n-2,-1,-1):
        left = "*" * (i + 1)
        spaces = " " * (2 * (n - i - 1))
        right = "*" * (i + 1)
        print(left + spaces + right)

# ----21----
def p21(n):
    for i in range(n):
        if i == 0 or i == n-1:
            for j in range(n):
                print("*",end="")
            print()
        else:
            print("*",end="")
            for k in range(n-2):
                print(" ",end="")
            print("*",end="")
            print()

# ----22----
def p22(n):
    for i in range(2 * n - 1):
        # Inner loop for columns
        for j in range(2 * n - 1):
            # Calculate distance from top
            top = i
            # Calculate distance from left
            left = j
            # Calculate distance from bottom
            bottom = (2 * n - 2) - i
            # Calculate distance from right
            right = (2 * n - 2) - j

            # Take the minimum of all four distances
            minDist = min(top, bottom, left, right)

            # Print number (starts with n at border, decreases inside)
            print(n - minDist, end=" ")
        # Move to the next row
        print()

# ----Run All----
def run_all(n):
    print("Pattern 1.0\n")
    p1_0(n)
    print()
    print("Pattern 1.1\n")
    p1_1(n)
    print()
    print("Pattern 2.0\n")
    p2_0(n)
    print() 
    print("Pattern 2.1\n")
    p2_1(n)
    print()
    print("Pattern 3\n")
    p3(n)
    print()
    print("Pattern 4\n")
    p4(n)
    print()
    print("Pattern 5\n")
    p5(n)
    print()
    print("Pattern 6\n")
    p6(n)
    print()
    print("Pattern 7\n")
    p7(n)
    print()
    print("Pattern 8\n")
    p8(n)
    print()
    print("Pattern 9\n")
    p9(n)
    print()
    print("Pattern X\n")
    px(n)
    print()
    print("Pattern 10.1\n")
    p10_1(n)
    print()
    print("Pattern 10.2\n")
    p10_2(n)
    print()
    print("Pattern 11\n")
    p11(n)
    print()
    print("Pattern 12\n")
    p12(n)
    print()
    print("Pattern 13\n")
    p13(n)
    print()
    print("Pattern 14\n")
    p14(n)
    print()
    print("Pattern 15\n")
    p15(n)
    print()
    print("Pattern 16\n")
    p16(n)
    print()
    print("Pattern 17.1\n")
    p17_1(n)
    print()
    print("Pattern 17.2\n")
    p17_2(n)
    print()
    print("Pattern 18.1\n")
    p18_1(n)
    print()
    print("Pattern 18.2\n")
    p18_2(n)
    print()
    print("Pattern 19\n")
    p19(n)
    print()
    print("Pattern 20\n")
    p20(n)
    print()
    print("Pattern 21\n")
    p21(n)
    print()
    print("Pattern 22\n")
    p22(n)
    print()
    

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    run_all(n)