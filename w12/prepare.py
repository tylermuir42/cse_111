

def main():
    provinces_list = read_list("provinces.txt")

    #remove first element
    provinces_list.pop(0)

    #remove last element
    provinces_list.pop()

    #replace AB with Alberta
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    print(provinces_list)

    #count how many times Alberta shows up
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the list")


def read_list(filename):
    #make an empty list
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            #remove white space
            clean_line = line.strip()

            text_list.append(clean_line)

    return text_list

if __name__ == "__main__":
    main()
