# This program writes out correspondences to the formula h ** n = m
n = int(input('Enter number: '))
if n == 1:  # for 1 range 23
    for h in range(24):
        for m in range(24):
            if h ** n == m:
                hf = h
                mf = m
                if h < 10:
                    hf = str(0) + str(h)  # zero added if hours or minutes < 10
                if m < 10:
                    mf = str(0) + str(m)
                print(f"{hf}:{mf}")

else:  # if n != 1 this is performed
    for h in range(60):
        for m in range(60):
            if h ** n == m:
                hf = h
                mf = m
                if h < 10:
                    hf = str(0) + str(h)
                if m < 10:
                    mf = str(0) + str(m)
                print(f"{hf}:{mf}")
