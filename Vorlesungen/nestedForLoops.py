def print_flower():
    # Stem
    for _ in range(3):
        print(" " * 4 + "|")

    # Petals
    for i in range(3):
        print(" " * (3 - i) + "/" + "*" * (2 * i + 1) + "\\")

    # Middle part of the flower
    print(" " * 3 + "|_|")


# Call the function to print the flower
print_flower()

print("");print("");print("")

def print_woman_symbol():
    # Upper part of the woman symbol
    for i in range(4):
        print(" " * (3 - i) + "/" + "|" * (2 * i + 1) + "\\")

    # Lower part of the woman symbol
    for i in range(3):
        print(" " * 3 + "|" * 3)


# Call the function to print the woman symbol
print_woman_symbol()

def print_octagon(size):
    if size < 3 or size % 2 == 0:
        print("Invalid size. Please choose an odd size greater than or equal to 3.")
        return

    # Calculate the number of spaces for the first row
    spaces = size // 2

    for i in range(size):
        # Print leading spaces
        for _ in range(spaces):
            print(" ", end="")

        # Print octagon sides
        if i == 0 or i == size - 1:
            print("*" * (size + i))
        else:
            print("*", end="")
            # Print spaces between the edges
            for _ in range(size - 2 + i):
                if i < size // 2:
                    print(" ", end="")
                else:
                    print("*", end="")
            print("*")

        # Update the number of spaces for the next row
        if i < size // 2:
            spaces -= 1
        else:
            spaces += 1

# Example: Print an octagon with size 7
print_octagon(7)


def print_stairway(height):
    for i in range(1, height + 1):
        for j in range(i):
            print('*', end=' ')
        print()

# Specify the height of the stairway
stairway_height = 9

# Call the function to print the stairway
print_stairway(stairway_height)

def print_bow_and_arrow(size):
    # Print upper part of the bow
    for i in range(size):
        for j in range(size * 2):
            if j == size or j == size * 2 - 1:
                print('*', end=' ')
            elif i == size - 1 and (j == 0 or j == size * 2 - 2):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

    # Print lower part of the bow
    for i in range(size):
        for j in range(size * 2):
            if j == 0 or j == size * 2 - 2:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

    # Print arrowhead
    for i in range(size):
        for j in range(size - i):
            print(' ', end=' ')
        for k in range(i * 2 + 1):
            print('*', end=' ')
        print()

# Specify the size of the bow and arrow
bow_and_arrow_size = 4

# Call the function to print the bow and arrow
print_bow_and_arrow(bow_and_arrow_size)

def print_ladder(height):
    for i in range(1, height + 1):
        # Print rungs of the ladder
        for j in range(2):
            for k in range(i):
                print('*', end=' ')
            print(' ', end=' ')
        print()

        # Print vertical part of the ladder
        for j in range(2):
            print('* ', end=' ')
        print()

# Specify the height of the ladder
ladder_height = 4

# Call the function to print the ladder
print_ladder(ladder_height)
