import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

mean = float(input("mean = "))
exp = math.e
s = int(input("start = "))
e = int(input("end = "))

total_probability = 0
probablities_list = []

for x in range(s, e + 1):
    current = ((mean ** x)*(exp ** (mean * (-1))))/factorial(x)
    probablities_list.append(current)
    total_probability += current

lesser_or_greater = input("lesser_or_greater = ")

print(probablities_list)
if (lesser_or_greater == "l"):
    print(total_probability)
elif lesser_or_greater == "g":
    print(1 - total_probability)