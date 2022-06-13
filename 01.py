try:
    x = float(input())
    result = (x - x ** 2 + x ** 5) ** (1. / 3.)
    print(result)

except Exception:
    print('ERROR')
