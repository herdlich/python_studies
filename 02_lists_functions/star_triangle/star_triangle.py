def draw_triangle(fill, base):
    total = 1
    if base % 2 != 0:
        while total <= base // 2:
            print(fill * total)
            total += 1

        print(fill * total)

        while total > 0:
            total -= 1
            print(fill * total)

    else:
        print('Only odd numbers allowed')


draw_triangle(input('Enter a symbol: '), int(input('Enter a number: ')))
