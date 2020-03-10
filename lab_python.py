# Elliott Long
rings = 1
core = 1
while rings != 0 or core != 0:      # loop, choose 0 0 to exit
    rings = int(input("Rings: "))
    core = int(input("Core Size: "))
    # collected for forming rings/cores
    ringu = rings       # dummy value used to manipulate

    for x in range(0, rings):   # loop for upper part
        ringu = ringu - 1
        print(' ' * ringu, end='')
        print('/' * (x + 1), end='')
        print('-' * core, end='')
        print("\\" * (x + 1))
    for x in range(0, core):    # loop for middle
        print("|" * rings, end='')
        print(' ' * core, end='')
        print("|" * rings)
    ringu = rings   # resetting the ringu value
    for x in range(0, rings):   # loop for bottom
        print(' ' * x, end='')
        print("\\" * ringu, end='')
        print('-' * core, end='')
        print('/' * ringu)
        ringu = ringu - 1
