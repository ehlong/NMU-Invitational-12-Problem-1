# Elliott Long
rings = int(input("Rings: "))
core = int(input("Core Size: "))
# collected for forming rings/cores

# nest loops to generate shapes, these generally work
print(' ' * (rings - 1), end='')
print('/', end='')
print('-' * core, end='')
print(r"\ ")
