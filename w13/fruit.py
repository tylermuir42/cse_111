def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    reversed_list = fruit_list[::-1]
    print(reversed_list)

    fruit_list.append("orange")
    print(fruit_list)

    fruit_list.insert(2,"cherry")
    print(fruit_list)

    fruit_list.pop(1)
    print(fruit_list)

    popped_element = fruit_list.pop()
    print(popped_element)
    print(fruit_list)

    fruit_list.sort()
    print(fruit_list)

    fruit_list.clear()
    print(fruit_list)


if __name__ == '__main__':
    main()