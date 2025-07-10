import csv
from datetime import datetime

PRODUCT_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

def main():
    try:
        product_dict = read_dictionary("products.csv", PRODUCT_INDEX)
        
        #Print the whole list
        # print("All Products: ")
        # print(product_dict)
        # print()

        #Print the requested items list
        request_list = read_list("request.csv")

        print("Muir Grocery")
        print()

        print("Requested Items: ")

        subtotal = 0
        num_items = 0
        for item in request_list:
            product_id = item[PRODUCT_INDEX]
            quantity = int(item[1])

            try:
                if product_id in product_dict:
                    product = product_dict[product_id]
                    name = product[NAME_INDEX]
                    price = float(product[PRICE_INDEX])
                    subtotal += price * quantity
                    num_items += quantity
                    print(f"{name.title()}: {quantity} @ ${price:.2f}")
                else:
                    print(f"Product ID {product_id} not found.")
            
            except KeyError:
                print(f"Product ID {product_id} not found in product dictionary")

    
        #Subtotals and taxes
        print()
        print(f"Number of Items: {num_items}")
        print(f"Subtotal: ${subtotal:.2f}")

        tax = 0.06
        total = (tax * subtotal) + subtotal
        print(f"Sales Tax: {tax}")
        print(f"Total: ${total:.2f}")
        

        #Thank you and date
        print()
        now = datetime.now()
        print("Thank you for shopping with us!")
        print(now.strftime("%m-%d-%Y"))
        target_date = datetime(2026, 1, 1)
        days_remaining = (target_date - now).days
        print(f"{days_remaining} until our new years sale!")

    except FileNotFoundError as e:
        print(f"Error: {e}")


def read_dictionary(filename, key_col):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary1 = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_col]
                dictionary1[key] = row_list

    return dictionary1

def read_list(filename):
    """Read the contents of a CSV file into a list and return the list.

    Parameters
        filename: the name of the CSV file to read.

    Return: a list
    """

    list1 = []

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                list1.append(row_list)

    return list1


if __name__ == "__main__":
    main()