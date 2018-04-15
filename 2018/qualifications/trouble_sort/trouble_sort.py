import sys
      
n = int(sys.stdin.readline())
for i in xrange(1, n + 1):
    size = int(sys.stdin.readline())
    nums = [int(x) for x in sys.stdin.readline().split()]
    odds = sorted(nums[::2])
    evens = sorted(nums[1::2])
    flag = None;
    a = 0
    b = 0
    while a < len(odds) and b < len(evens):
      if a == b:
        if odds[a] > evens[b]:
          flag = a * 2
          break
        a += 1
      else:
        if evens[b] > odds[a]:
          flag = b * 2 + 1
          break
        b += 1
    if flag is not None:
        print("Case #{}: {}".format(i, flag))
    else:
        print("Case #{}: OK".format(i))
