import sys

def print_x(height, out=sys.stdout):
    '''
    This function prints out an x of *'s depending on a given height.

    Explanation:
    In this problem its easier to use a list for each line of size height.
     That way as we loop through the height we can set the index at i and
      height - i.
        ex: 
           I   P
            I P 
             I
            P I
           P   I
        Where I is the index and P is height - index - 1

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

    # Need to check if height is > 0 so we don't print empty newlines
    if height > 0:
        # First start with a newline
        out.write('\n')

        # Now we take the height and loop through
        for i in range(height):
            # Make a list of ' ' of size height
            line = [' '] * height

            # Set the stars to i and height - i - 1
            line[i] = '*'
            line[height - i - 1] = '*'

            # Join the list together making sure to strip the trailing whitspace
            out.write(''.join(line).rstrip() + '\n')

        # End with a newline
        out.write('\n')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print_x(sys.argv[1])
    else:
        print("Invalid command line arguments. Usage: python part2.py <height of x>")
        exit(-1)