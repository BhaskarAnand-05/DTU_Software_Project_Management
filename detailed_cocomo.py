import math

intermediate_cocomo_table = [
    [3.2, 1.05, 2.5, 0.38],
    [3.0, 1.12, 2.5, 0.35],
    [2.8, 1.20, 2.5, 0.32]
]

mu = [
    [0.06, 0.16, 0.26, 0.42, 0.16],
    [0.06, 0.16, 0.24, 0.38, 0.22],
    [0.07, 0.17, 0.25, 0.33, 0.25],
    [0.07, 0.17, 0.24, 0.31, 0.28],
    [0.08, 0.18, 0.26, 0.42, 0.16],
    [0.06, 0.16, 0.26, 0.42, 0.16]
]

tao = [
    [0.1, 0.19, 0.24, 0.39, 0.18],
    [0.12, 0.19, 0.21, 0.34, 0.26],
    [0.20, 0.26, 0.21, 0.27, 0.18],
    [0.26, 0.22, 0.24, 0.25, 0.29],
    [0.36, 0.36, 0.18, 0.18, 0.28],
    [0.40, 0.38, 0.16, 0.16, 0.30]
]

size = 0
model = 0
rating = 0

mode = [
    "Organic small",
    "Organic medium",
    "Semi Detached medium",
    "Semi-Detached large",
    "Embedded large",
    "Embedded extra large"
]

driver = [
    "RELY", "DATA", "CPLX", "TIME", "STOR",
    "VIRT", "TURN", "ACAP", "AEXP", "PCAP",
    "VEXP", "LEXP", "MODP", "TOOL", "SCED"
]

effort = 0
EAF = 1
a = 0
time1 = 0
staff = 0
productivity = 0

costdrivers = [
    [0.75, 0.88, 1, 1.15, 1.40, -1],
    [-1, 0.94, 1, 1.08, 1.16, -1],
    [0.70, 0.85, 1, 1.15, 1.30, 1.65],
    [-1, -1, 1, 1.11, 1.30, 1.66],
    [-1, -1, 1, 1.06, 1.21, 1.56],
    [-1, 0.87, 1, 1.15, 1.30, -1],
    [-1, 0.87, 1, 1.07, 1.15, -1],
    [1.46, 1.19, 1, 0.86, 0.71, -1],
    [1.29, 1.13, 1.00, 0.91, 0.82, -1],
    [1.42, 1.17, 1, 0.86, 0.70, -1],
    [1.21, 1.10, 1, 0.90, -1, -1],
    [1.14, 1.07, 1, 0.95, -1, -1],
    [1.24, 1.10, 1.00, 0.91, 0.82, -1],
    [1.24, 1.10, 1, 0.91, 0.83, -1],
    [1.23, 1.08, 1, 1.04, 1.10, -1]
]

while True:
    print("\nEnter the size of the project : ", end='')
    size = int(input())

    if size <= 2:
        model = 0
    elif 2 < size <= 32:
        model = 1
    elif 32 < size <= 128:
        model = 2
    elif 128 <= size < 300:
        model = 3
    elif 300 < size < 320:
        model = 4
    else:
        model = 5
    print("\nMode =", mode[model])

    EAF = 1
    for i in range(15):
        while True:
            print(f"\nRate cost driver {driver[i]} on a scale of 0-5:")
            print("0 - Very Low\t1 - Low\t2 - Nominal\t3 - High\t4 - Very High\t5 - Extra High")
            rating = int(input())
            a = costdrivers[i][rating]
            if a == -1:
                print("\nNo value exists for this rating. Enter another rating...")
            else:
                break
        EAF = EAF * a

    print("EAF =", EAF)

    effort = (intermediate_cocomo_table[model][0] * size ** intermediate_cocomo_table[model][1]) * EAF
    time1 = intermediate_cocomo_table[model][2] * effort ** intermediate_cocomo_table[model][3]
    staff = effort / time1
    productivity = size / effort

    print("\nFor phase Plan and requirement")
    print("Effort =", effort * mu[model][0], "Person-Month")
    print("Development Time =", time1 * tao[model][0], "Months")

    print("\nFor phase system design")
    print("Effort =", effort * mu[model][1], "Person-Month")
    print("Development Time =", time1 * tao[model][1], "Months")

    print("\nFor phase detail design")
    print("Effort =", effort * mu[model][2], "Person-Month")
    print("Development Time =", time1 * tao[model][2], "Months")

    print("\nFor phase code and test")
    print("Effort =", effort * mu[model][3], "Person-Month")
    print("Development Time =", time1 * tao[model][3], "Months")

    print("\nFor phase integration and test")
    print("Effort =", effort * mu[model][4], "Person-Month")
    print("Development Time =", time1 * tao[model][4], "Months")
