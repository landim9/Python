for i in range(10):
    print((i + 1) * "*")

print()

for i in range(10, -1, -1):
    print((i + 1) * "*")

print()

for i in range(9, -1, -1):
    print(f'{(i + 1) * "*" : >10}')

print()

for i in range(10):
    print(f'{(i + 1) * "*" : >10}')
