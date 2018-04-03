def which(N, K):
    s = [N]
    while K:
        if s[0] > 0:
            tmp = s[0] - 1
        else:
            tmp = s[0]
        if tmp % 2 == 0:
            s.append(tmp // 2)
            s.append(tmp // 2)
        else:
            s.append(tmp // 2 + 1)
            s.append(tmp // 2)
        K -= 1
        if K is not 0:
            s.sort(reverse=True)
            s = s[1:]
    return (max(s[-2:]), min(s[-2:]))

f = open('small1.in', 'r')
f2 = open('small1.out', 'w')
num_cases = int(f.readline())
for i in range(1, num_cases + 1):
    stalls,people = [int(x) for x in f.readline().split()]
    result = which(stalls,people)
    print(f'Case #{i}: {result[0]} {result[1]}', file=f2)
f.close()
f2.close()
