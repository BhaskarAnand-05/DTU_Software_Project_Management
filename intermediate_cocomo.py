while True:
    print("Enter project size in KLOC or -1 to terminate")
    n = float(input())
    
    if n == -1:
        break

    mode = ""
    ab, b, c, d = 0, 0, 0, 0

    if 2 < n <= 50:
        mode = "organic"
        ab = 3.2
        b = 1.05
        c = 2.5
        d = 0.38
    elif n >= 50 and n <= 300:
        mode = "semi-detached"
        ab = 3.0
        b = 1.12
        c = 2.5
        d = 0.35
    elif n > 300:
        mode = "Embedded"
        ab = 2.8
        b = 1.2
        c = 2.5
        d = 0.32
    else:
        print("Incorrect entry, try again")
        continue

    a = [[1 for j in range(7)] for i in range(16)]
    
    a[1][1] = 0.75
    a[1][2] = 0.88
    a[1][3] = 1.00
    a[1][4] = 1.15
    a[1][5] = 1.40

    a[2][2] = 0.94
    a[2][3] = 1.00
    a[2][4] = 1.08
    a[2][5] = 1.16

    a[3][1] = 0.7
    a[3][2] = 0.85
    a[3][3] = 1.00
    a[3][4] = 1.15
    a[3][5] = 1.30
    a[3][6] = 1.65

    a[4][3] = 1.00
    a[4][4] = 1.11
    a[4][5] = 1.30
    a[4][6] = 1.66

    a[5][3] = 1
    a[5][4] = 1.06
    a[5][5] = 1.21
    a[5][6] = 1.56

    a[6][2] = 0.87
    a[6][3] = 1
    a[6][4] = 1.15
    a[6][5] = 1.30

    a[7][2] = 0.87
    a[7][3] = 1
    a[7][4] = 1.07
    a[7][5] = 1.15

    a[8][1] = 1.46
    a[8][2] = 1.19
    a[8][3] = 1.0
    a[8][4] = 0.86
    a[8][5] = 0.71

    a[9][1] = 1.29
    a[9][2] = 1.13
    a[9][3] = 1.0
    a[9][4] = 0.91
    a[9][5] = 0.82

    a[10][1] = 1.42
    a[10][2] = 1.17
    a[10][3] = 1
    a[10][4] = 0.86
    a[10][5] = 0.70

    a[11][1] = 1.21
    a[11][2] = 1.1
    a[11][3] = 1
    a[11][4] = 0.9

    a[12][1] = 1.14
    a[12][2] = 1.07
    a[12][3] = 1.0
    a[12][4] = 0.95

    a[13][1] = 1.24
    a[13][2] = 1.1
    a[13][3] = 1
    a[13][4] = 0.91
    a[13][5] = 0.82

    a[14][1] = 1.24
    a[14][2] = 1.1
    a[14][3] = 1
    a[14][4] = 0.91
    a[14][5] = 0.83

    a[15][1] = 1.23
    a[15][2] = 1.08
    a[15][3] = 1.00
    a[15][4] = 1.04
    a[15][5] = 1.10

    s = ["", "Required software reliability", "Size of the application database", "The complexity of the product",
         "Execution time constraints", "Memory constraints", "The volatility of the virtual machine environment",
         "Required turnabout time", "Analyst capability", "Application experience", "Programmer capability",
         "Virtual machine experience", "Programming language experience", "Modern Programming Practices",
         "Use of Software tools", "Required Development schedule"]

    eaf = 1

    print("\nPlease enter the answer to the following things in any one of the following options:")
    print("very low - 1")
    print("low - 2")
    print("nominal - 3")
    print("high - 4")
    print("very high - 5")
    print("Extra high - 6")
    print("ELSE if you don't know - 0")

    for i in range(1, 16):
        print("\n" + s[i])
        print(": ", end='')
        x = int(input())

        if x > 6 or x < 1:
            continue

        eaf *= a[i][x]
        print("\n")

    print("\n")
    print("Mode= " + mode)
    print("Effective adjustment factor= " + str(eaf))
    Effort = ab * n ** b * eaf
    Development_time = c * Effort ** d
    Average_staff_size = Effort / Development_time
    print("Effort= " + str(Effort) + " Person Months")
    print("Development_time= " + str(Development_time) + " Months")
    print("Average_staff_size= " + str(Average_staff_size) + " Persons")
    print("\n")
