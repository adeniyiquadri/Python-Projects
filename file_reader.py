import sys
import csv
def main():
    output = []
    if len(sys.argv) < 3:
        sys.exit("Too few command line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line argument")
    else:
        try:
            file_name = sys.argv[1]
            with open(file_name) as file_content:
                reader = csv.DictReader(file_content)
                for row in reader:
                    name, house = row["name"], row["house"]
                    last, first = name.split(", ")
                    output.append({"first": first,"last": last,"house":house})
        except FileNotFoundError:
            sys.exit("File does not exist")
# Writing the content in file 1 to a new file
    new_file = sys.argv[2]
    with open(new_file, "w", newline = "") as second_file:
        writer = csv.DictWriter(second_file, fieldnames = ["first","last","house"])
        writer.writeheader()
        for row in output:
            writer.writerow(row)
if __name__ == "__main__":
    main()
