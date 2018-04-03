def count(n):
    length = len(n)
    i = 0
    tmp = '0'
    while i < length:
        if n[i] < tmp:
            left = str(int(n[:i]) - 1)
            right = '9' * (length - i)
            return (count(left + right))
        tmp = n[i]
        i += 1
    return (n.strip('0'))


f = open('large.in', 'r')
f2 = open('large.out', 'w')
num_cases = int(f.readline())
for i in range(1, num_cases + 1):
    n = f.readline().strip()
    print(f'Case #{i}: {count(n)}', file=f2)
f.close()
f2.close()
