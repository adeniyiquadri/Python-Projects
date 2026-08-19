grocery = {}
while True:
    try:
        item = input("").lower()
        if item in grocery:
            grocery[item] = grocery[item] + 1
        else:
            grocery[item] = 1
        continue
    except EOFError:
        for item, count in sorted(grocery.items()):
            print(count, item.upper())
            break