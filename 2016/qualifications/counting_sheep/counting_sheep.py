def sleep(n):
    numbers = {'0':True, '1':True, '2':True, '3':True, '4':True,
            '5':True, '6':True, '7':True, '8':True, '9':True}
    i = 1
    num = None
    while (bool(numbers) is not False):
        num = str(n * i)
        if num == '0':
            return ("INSOMNIA")
        for digit in num:
            numbers.pop(digit, None)
        i += 1
    return (num)

f = open("large.in", "r")
f2 = open("large.out", "w")

num_cases = int(f.readline())
for i in range(1, num_cases + 1):
    num = int(f.readline())
    print(f'Case #{i}: {sleep(num)}', file=f2)
f.close()
f2.close()
