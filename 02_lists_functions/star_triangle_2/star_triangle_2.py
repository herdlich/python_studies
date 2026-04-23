def draw_triangle():
    total = 15
    space = 0
    l = []
    for i in range(8, 0, -1):
        l.append(" " * space + ("*" * total))
        total -= 2
        space += 1
    print(*l[::-1], sep='\n')


draw_triangle()
