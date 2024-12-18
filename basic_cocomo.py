def basic_cocomo(size, mode):
    # Effort Equation Constants
    constants = {
        'organic': (2.4, 1.05, 2.5, 0.38),
        'semidetached': (3.0, 1.12, 2.5, 0.35),
        'embedded': (3.6, 1.20, 2.5, 0.32)
    }

    if size >= 2000 and size <= 50000:
        mode = 'organic'
        print("Project Mode: Organic")
    elif size > 50000 and size <= 300000:
        mode = 'semidetached'
        print("Project Mode: Semidetached")
    elif size > 300000:
        mode = 'embedded'
        print("Project Mode: Embedded")
    else:
        print("Invalid size. Size should be greater than 2000 KLOC.")
        return

    try:
        a, b, c, d = constants[mode]
    except KeyError:
        print("Invalid mode. Choose from 'organic', 'semidetached', or 'embedded'.")
        return

    effort = a * (size ** b)
    time = c * (effort ** d)

    return effort, time

# Input the size of the software project (in KLOC)
size = float(input("Enter the size of the software project (in KLOC): "))

effort, time = basic_cocomo(size, None)  # Use None for the mode

if effort and time:
    print(f"Effort Required (in person-months): {effort}")
    print(f"Development Time (in months): {time}")

