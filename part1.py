import sys

def print_pyramid(height, out=sys.stdout):
    '''
    This function prints out a pyramid of *'s depending on a given height.

    Explanation:
    We need to keep track of the spaces at each level which corresponds
     to height - 1 (the number of stars at the bottom is (height * 2) - 1)

    Args:
        height: The height of the tree to be printed.
        out: An optional argument for setting the desired system output.

    Raises:
        SystemExit: exits program
    '''
    # A check if height is an integer, if it is, overrite height
    #  else print an exit message and exit.
    # ***Convert to string first so that it can run isdigit which 
    #   checks if its an int/float/<0)***
    if str(height).isdigit():
        height = int(height)
    else:
        out.write("Argument is not an integer and cannot be less than 0!")
        exit(-1)

    # Need to check if height is > 0 so we don't print empty newlines
    if height > 0:
        # First start with a newline
        out.write('\n')

        # Spaces is the number of ' ' on each side of the *'s
        spaces = height - 1

        # Stars is the number of *'s at each level (start at 1)
        stars = 1

        # Now we take the height and loop through
        for i in range(height):
            out.write(' ' * spaces + '*' * stars + '\n')

            # At each iteration we need to update spaces & stars
            spaces -= 1
            stars += 2

        # End with a newline
        out.write('\n')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_pyramid(sys.argv[1])
    else:
        print("Invalid command line arguments. Usage: python part1.py <height of tree>")
        exit(-1)