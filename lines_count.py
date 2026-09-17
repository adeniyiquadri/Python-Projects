import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line argument")
    else:
        file_name = sys.argv[1]
    #Calling a function that exits if the last two letters of the file name doesn't end in py
        ending(file_name)
    #Calling a function that opens the file, reads the number of lines and if the file does not exist, exit
        line_count = opening(file_name)
        print(f"{line_count}")
    #Writing a function that exits if the last two letters of the file name doesn't end in py
def ending(name):
    if name.endswith(".py"):
        pass
    else:
        sys.exit("Not a python file")
#Writing a function that opens the file, reads the number of lines and if the file does not exist, exit
def opening(file):
    try:
        count = 0
        with open(file,"r") as files:
            for line in files:
                line = line.strip()
                if line.startswith("#") or line == "":
                    continue
                else:
                    count = count + 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")
if __name__ == "__main__":
    main()