def factorial(n):
    factorial = 1
    for i in range(1,int(n) + 1):
       factorial = factorial*i
    return factorial

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