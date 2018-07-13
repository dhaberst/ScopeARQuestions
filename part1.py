import sys

def print_pyramid(height, out=sys.stdout):
    '''
    This function prints out a pyramid of *'s depending on a given height.

    Args:
        height: The height of the tree to be printed.
        out: An optional argument for setting the desired system output.
    '''
    # A check if height is an integer, if it is, overrite height
    #  else print an exit message and exit.
    if height.isdigit():
        height = int(height)
    else:
        print("Argument is not an integer!")
        exit(-1)

        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_pyramid(sys.argv[1])
    else:
        print("Invalid command line arguments. Usage: python part1.py <height of tree>")