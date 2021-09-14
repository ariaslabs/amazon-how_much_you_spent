import sys
import csv

def spacer(spaces):
    counter = 0
    while counter < spaces:
        print()
        counter += 1

def main():

    amazon_csv_file = sys.argv[1]

    with open(amazon_csv_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        total = 0.00

        for line in csv_reader:
            transaction_string = line[29].replace("$", "")
            transaction_total = float(transaction_string)
            total += transaction_total

        spacer(2)
        print("Your total spent at amazon is: $" + str(round(total, 2)))
        spacer(2)
if __name__ == "__main__":
    main()


