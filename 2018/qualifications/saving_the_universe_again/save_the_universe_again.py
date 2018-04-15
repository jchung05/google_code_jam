import sys

num_cases = int(raw_input())

for itr in range(1, num_cases + 1):
  shield, instr  = [x for x in raw_input().split()]
  shield = int(shield)
  instr = list(instr.rstrip('C'))
  
  length = len(instr) - 1
  charge = 0
  damage = 0
  times = 0
  for c in instr:
    if c == 'C':
      charge += 1
    else:
      damage += 2**charge
  
  if charge > 0:
    i = length
    while damage > shield and i >= 0:
      if instr[i] == 'C':
        j = i + 1
        while j <= length and instr[j] == 'S':
          damage -= 2**(charge - 1)
          times += 1
          if damage <= shield:
            break
          if j == length:
            length -= 1
            break
          else:
            j += 1
        charge -= 1
        instr[i] = 'S'
        instr[j] = 'C'
        i = length
      else:
        i -= 1
      if damage <= shield:
        break  
  if damage > shield:
    print('Case #{}: IMPOSSIBLE'.format(itr))
  else:
    print('Case #{}: {}'.format(itr, times))
