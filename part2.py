import sys

def print_x(height, out=sys.stdout):
    '''
    This function prints out an x of *'s depending on a given height.

    Args:
        height: The height of the x to be printed.
        out: An optional argument for setting the desired system output.

    Raises:
        SystemExit: exits program
    '''
    # A check if height is an integer
    if str(height).isdigit(): # Converting height to str allows use of isdigit
        height = int(height)
    else:
        out.write("Argument is not an integer and cannot be less than 0!")
        exit(-1)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_x(sys.argv[1])
    else:
        print("Invalid command line arguments. Usage: python part2.py <height of x>")
        exit(-1)