def count(n):
    int_n = int(n)
    for i in range(int_n, 0, -1):
        str_i = str(i)
        j = len(str_i) - 1
        while j > 0:
            if ord(str_i[j]) >= ord(str_i[j - 1]):
                j -= 1
            else:
                break
        if j is 0:
            return (i)

f = open('small.in', 'r')
f2 = open('small.out', 'w')
num_cases = int(f.readline())
for i in range(1, num_cases + 1):
    n = f.readline().strip()
    print(f'Case #{i}: {count(n)}', file=f2)
f.close()
f2.close()
