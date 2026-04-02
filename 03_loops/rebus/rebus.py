# REBUS: a + 3 * b + 2 * c == m
# Find all possible solutions and output
n, m = (int(input()) for _ in range(2))
flag = True  # if there are no solutions, the program will report this using a flag.
for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a + 3 * b + 2 * c == m:
                flag = False  # flag false - at least 1 solution was found
                print(f'{a} + 3×{b} + 2×{c} = {m}')
if flag:
    print('For given n and m, there are no solutions.')
