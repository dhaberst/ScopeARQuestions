import unittest
from part1 import print_pyramid
from io import StringIO

class TestPart1(unittest.TestCase):

    def test_print_pyramid_height_invalid_arg(self):
        '''
        This test should terminate the program with an exit
        code of -1 with the following args 'a', '-1', '1.1'
        '''
        out = StringIO()
        
        # Testing 'a'
        with self.assertRaises(SystemExit) as cm:
            print_pyramid('a', out=out)
        
        self.assertEqual(cm.exception.code, -1)

        # Testing -1
        with self.assertRaises(SystemExit) as cm:
            print_pyramid(-1, out=out)

        self.assertEqual(cm.exception.code, -1)

         # Testing 1.1
        with self.assertRaises(SystemExit) as cm:
            print_pyramid(1.1, out=out)

        self.assertEqual(cm.exception.code, -1)

    def test_print_pyramid_height_8(self):
        '''
        This test should print a pyramid of height 8, starting 
        with 1 * in the middle and increasing by 2 each level 
        to end at 15.
        '''
        out = StringIO()
        print_pyramid(8, out=out)
        output = out.getvalue()
        assert output == ("\n"
                          "       *\n"
                          "      ***\n"
                          "     *****\n"
                          "    *******\n"
                          "   *********\n"
                          "  ***********\n"
                          " *************\n"
                          "***************\n"
                          "\n")

    def test_print_pyramid_height_0(self):
        '''
        This test should print a pyramid of height 0, it
        should print an empty string
        '''
        out = StringIO()
        print_pyramid(0, out=out)
        output = out.getvalue()
        assert output == ''

if __name__ == '__main__':
    unittest.main()