def main():
    fuel_gauge = input("How much fuel is in the tank? ")
    fuel_fraction = convert(fuel_gauge)
    fuel_percentage = gauge(fuel_fraction)
    print(f"{fuel_percentage}")
def convert(fraction):
    p,q = fraction.split("/")
    x = int(p)
    y = int(q)
    if y == 0:
        raise ZeroDivisionError("the denominator should never be 0")
    elif x > y or x < 0:
        raise ValueError("the numerator cannot be negative neither can the fraction be greater than 1")
    else:
        percentage = round((x / y) * 100)
        return percentage
def gauge(fuel_fraction):
    if 1 >= fuel_fraction:
        return("E")
    elif 1< fuel_fraction <99:
        return(f"{fuel_fraction}%")
    elif 99 <= fuel_fraction:
        return("F")
if __name__ == "__main__":
    main()