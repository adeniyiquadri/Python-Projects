def main():
    plate = input("Plate: ")
    if is_valid(plate):
            print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    #generating the first two letters of the plate and assigning it to a variable
    first_two_letter = s[:2]
#calling a function that return true if the first two letter are alphabet and assigning it to a variable
    x = is_true(first_two_letter)
#calling a function that return true if the length is MIN2 AND MAX6
    y = min_max(len(s))
#calling a function that returns true if only the number ends with letter and the first number is not 0
    p = position(s)
#calling a function that doesn't allow for ("."," ",":",";","_" etc) and returns true
    z = punctuation_mark(s)
    if x == True and y == True and p == True and z == True:
        return True
    else:
        return False
def is_true(x):
    for char in x:
        if char.isdigit():
            return False
    return True
def min_max(y):
    if 2 <= y <=6:
        return True
    else:
        return False
def position(p):
    have_seen = False
    for char in p:
        if char.isalpha() and have_seen:
            return False
        if char.isdigit():
            if not have_seen and char == "0":
                return False
            have_seen = True
    return True
def punctuation_mark(z):
    if z.isalnum():
        return True
    else:
        return False
if __name__ == "__main__":
    main()
