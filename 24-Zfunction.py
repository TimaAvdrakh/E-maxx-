def z_func(s):
  s += '$'
  l, r = 0, 0
  z = [0] * len(s)
  for i in range(1, len(s)):
    z[i] = max(0, min(z[i - l], r - i))
    while s[z[i]] == s[i + z[i]]:
      z[i] += 1
    if i + z[i] > r:
      l, r = i, i + z[i]
  return z[:-1]

