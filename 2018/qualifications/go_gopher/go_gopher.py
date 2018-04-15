import sys

def make_map(area, h):
  map = []
  for x in xrange(h):
    map.append([0,0,0])
  return (map)

num_cases = int(raw_input())

for i in xrange(1, num_cases + 1):
  a = int(raw_input())
  h = a // 3 + 1
  map = make_map(a, h)
  output = [2,2]
  while (True):
    print('{} {}'.format(output[0],output[1]))
    sys.stdout.flush()
    input = [int(x) for x in raw_input().split(' ')]
    if input[0] <= 0 and input[1] <= 0 and input[0] == input[1]:
      break
    map[input[1] - 1][input[0] - 1] = 1
    if map[output[1] - 2][output[0] - 2] == 1 and map[output[1] - 2][output[0] - 1] == 1 and map[output[1] - 2][output[0]] == 1 and output[1] != h - 1:
      output[1] += 1
