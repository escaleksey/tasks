try:
    string = input()
    if not string.strip():
        raise ValueError
    symbol = input()
    if not symbol:
        raise ValueError
    n = int(input())
    if n <= 0:
        raise ValueError
    counter = 0
    string_out = ''
    for i in range(len(string)):
        if string[i] != symbol:
            string_out += string[i]
        else:
            counter += 1
        if counter == n:
            string_out += string[i+1:]
            break

    print(string_out)
except Exception:
    print('ERROR')