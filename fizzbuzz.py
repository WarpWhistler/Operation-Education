def fb():
    y = []
    for x in range(101):
        if x % 5 == 0 and x % 3 == 0:
            y += ['fizzbuzz']
        elif x % 3 == 0:
            y += ['fizz']
        elif x % 5 == 0:
            y += ['buzz']
        else:
            y += [x]
    print y
