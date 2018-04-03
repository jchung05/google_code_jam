def flip(s, p):
    plus = 0
    minus = 0
    length = 0
    for c in s:
        if c == '+':
            plus += 1
        if c == '-':
            minus += 1
        length += 1

    i = 0
    count = 0
    while i <= length - p:
        if minus == 0:
            return (count)
        if s[i] == '-':
            for j in range(p):
                if s[i + j] == '+':
                    s[i + j] = '-'
                    plus -= 1
                    minus += 1
                else:
                    s[i + j] = '+'
                    plus += 1
                    minus -= 1
            count += 1
        i += 1
    if minus == 0:
        return (count)
    return ("IMPOSSIBLE")

f = open('large.in', 'r')
f2 = open('large.out', 'w')
num_cases = int(f.readline())
for i in range(1, num_cases + 1):
    string, pan = [x for x in f.readline().split(' ')]
    pan = int(pan)
    string = list(string)
    print(f'Case #{i}: {flip(string, pan)}', file=f2)
f.close()
f2.close()
