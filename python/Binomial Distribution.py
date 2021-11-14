def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = float(input("n = "))
p = float(input("p = "))
q = 1 - p
s = int(input("start = "))
e = int(input("end = "))


total_probability = 0
probablities_list = []

for r in range(s, e + 1):
    current = round(((factorial(n))/(factorial(r)*factorial(n - r)))*(p**r)*(q**(n-r)), 3)
    probablities_list.append(current)
    total_probability += current

print(probablities_list)
print(round(total_probability, 3))