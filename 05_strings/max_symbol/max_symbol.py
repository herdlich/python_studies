# This exercise finds the most frequent symbol
s = input()
maximum = 0
for el in s:
    if s.count(el) >= maximum:
        maximum = s.count(el)
        symbol = el
print(symbol)