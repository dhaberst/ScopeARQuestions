import unittest
from part1 import print_pyramid
from io import StringIO

class TestPart1(unittest.TestCase):

    def test_print_pyramid(self):
        '''
        This tests that print_pyramid of part1 is correct.
        Should be a pyramid of height 8, starting with 1 * in the middle
        and increasing by 2 each level to end at 15.
        '''
        out = StringIO()
        print_pyramid(8, out=out)
        output = out.getvalue()
        assert output == ("\n"
                          "       *       \n"
                          "      ***      \n"
                          "     *****     \n"
                          "    *******    \n"
                          "   *********   \n"
                          "  ***********  \n"
                          " ************* \n"
                          "***************\n")

if __name__ == '__main__':
    unittest.main()