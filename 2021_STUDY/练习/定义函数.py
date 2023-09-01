def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


j = int(input('j = '))
n = int(input('n = '))
print(fac(j) // fac(n) // fac(j - n))
