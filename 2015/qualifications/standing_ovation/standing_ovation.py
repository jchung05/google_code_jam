def ovation(s_max, num):
    total = 0
    needed = 0

    for idx,val in enumerate(num):
        if idx > total:
            needed += idx - total
            total = idx
        total += int(val)
    return (needed)

f = open("large.in", "r")
f2 = open("large.out", "w")
num_cases = int(f.readline())

for i in range(1, num_cases + 1):
    s_max, num = [x for x in f.readline().strip().split(' ')]
    print(f'Case #{i}: {ovation(s_max, num)}', file=f2)
f.close()
f2.close()
