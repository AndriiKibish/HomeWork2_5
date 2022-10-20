a = int(input('Enter num1 '))
b = int(input('Enter num2 '))

d = min(a, b)
while a % d != 0 or b % d != 0:
    d -= 1

print("Max common devisor = ", d)

