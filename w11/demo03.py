# value vs reference for list copy

# Example 10 - What happens to x and y after changing x?

# def main():
#     x = 17
#     y = x
#     print(f"Before changing x: x {x}  y {y}")
#     x += 1
#     print(f"After changing x:  x {x}  y {y}")

# # Call main to start this program.
# if __name__ == "__main__":
#     main()



# Example 11 - What happens to lx and ly after changing lx?

# def main():
#     lx = [7, -2]
#     ly = lx
#     print(f"Before changing lx: lx {lx}  ly {ly}")
#     lx.append(5)
#     print(f"After changing lx:  lx {lx}  ly {ly}")

# # Call main to start this program.
# if __name__ == "__main__":
#     main()



def change_it(y):
    y.append(7)
    # y = [1,2,3,4,5,6,7,8]


x = [1,2,3,4,5]
y = x
print(x)
change_it(x)
print(x)
print(y)