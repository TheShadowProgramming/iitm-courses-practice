n = int(input())
l = []
prime_factors = []

for i in range(1, n+1):
    if (n % i == 0):
        l.append(i)

j = 1
while j < len(l):
    new_factor = l[j]
    j += 1
    if new_factor == 2:
        prime_factors.append(new_factor)
    else:
        flag = True
        for k in range(2, new_factor):
            if new_factor % k == 0:
                flag = False
                break
        if (flag):
            prime_factors.append(new_factor)

for i in range(len(prime_factors)):
    print(prime_factors[i])
