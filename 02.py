try:
    n = int(input())
    if n <= 0:
        raise ValueError

    positive = 0
    negative = 0
    for i in range(n):
        a = int(input())
        if a > 0:
            positive += 1
        elif a < 0:
            negative += 1

    if positive > negative:
        print('POSITIVE')
    elif positive < negative:
        print('NEGATIVE')
    else:
        print('EQUALS')

except Exception:
    print('ERROR')