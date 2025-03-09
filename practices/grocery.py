try:
    dict1 = {}

    while True:
        key = input().capitalize().strip()
        if key in dict1:
            dict1[key] += 1
        else:
            dict1[key] = 1

except EOFError:
    for key in sorted(dict1.keys()):
        print(dict1[key], key)
