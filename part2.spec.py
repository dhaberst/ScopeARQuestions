import unittest
from part2 import print_x
from io import StringIO

class TestPart2(unittest.TestCase):

    def test_print_x_height_invalid_arg(self):
        '''
        This test should terminate the program with an exit
        code of -1 with the following args 'a', '-1', '1.1'
        '''
        out = StringIO()
        
        # Testing 'a'
        with self.assertRaises(SystemExit) as cm:
            print_x('a', out=out)
        
        self.assertEqual(cm.exception.code, -1)

        # Testing -1
        with self.assertRaises(SystemExit) as cm:
            print_x(-1, out=out)

        self.assertEqual(cm.exception.code, -1)

         # Testing 1.1
        with self.assertRaises(SystemExit) as cm:
            print_x(1.1, out=out)

        self.assertEqual(cm.exception.code, -1)

    def test_print_x_height_5(self):
        '''
        This test should print an x of height 5.
        '''
        out = StringIO()
        print_x(5, out=out)
        output = out.getvalue()
        assert output == ("\n"
                          "*   *\n"
                          " * *\n"
                          "  *\n"
                          " * *\n"
                          "*   *\n"
                          "\n")

    def test_print_x_height_6(self):
            '''
            This test should print an x of height 6.
            Because of my assumption this should only
            print an x of height 5.
            '''
            out = StringIO()
            print_x(6, out=out)
            output = out.getvalue()
            assert output == ("\n"
                            "*   *\n"
                            " * *\n"
                            "  *\n"
                            " * *\n"
                            "*   *\n"
                            "\n")

    def test_print_x_height_0(self):
        '''
        This test should print a pyramid of height 0, it
        should print an empty string.
        '''
        out = StringIO()
        print_x(0, out=out)
        output = out.getvalue()
        assert output == ''

if __name__ == '__main__':
    unittest.main()