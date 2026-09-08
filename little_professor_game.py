import random
def main():
    n = get_level()
    count = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        correct = False
        for _ in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
                if z == x + y:
                    correct = True
                    count = count + 1
                    break
                else:
                    print("EEE")
            except ValueError:
                continue
        if not correct:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {count}")
def get_level():
    while True:
        try:
            x = int(input("Level :"))
            if x != 1 and x != 2 and x != 3:
                continue
            else:
                return x
        except ValueError:
            continue
def generate_integer(n):
    if n == 1:
        return random.randint(0,9)
    else:
        return random.randint(10 ** (n - 1), (10 ** n) - 1)
if __name__ == "__main__":
    main()