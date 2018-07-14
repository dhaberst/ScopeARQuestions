# ScopeARQuestions
These are the solutions to the provided questions in /docs.
# Usage
## Tests
[![Build Status](https://travis-ci.org/dhaberst/ScopeARQuestions.svg?branch=master)](https://travis-ci.org/dhaberst/ScopeARQuestions)

If tests need to be run individually the following commands can be run:
```bash
python part1.spec.py
python part2.spec.py
```
Otherwise sit back and enjoy CI :smiley:
## Problems
### part1.py &lt;height&gt;
This program prints out a tree of *'s given height as an argument.
```bash
python part1.py 8
```
### part2.py &lt;height&gt;
This program prints out an x of *'s given height as an argument.
```bash
python part2.py 5
```
# Assumptions
For part2, since we need to print an 'X' we cannot have an even height without the X looking weird. In this case I chose to round down to the nearest odd number i.e 6 -> 5.
# Resources
## Python Docs
- [Unit Testing](https://docs.python.org/3.6/library/unittest.html)
## Stack Overflow
- [Better way to test string outputs](https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python)
- [Test if str is integer](https://stackoverflow.com/questions/4228757/python-test-if-an-argument-is-an-integer)
- [Unittest assert exit returns](https://stackoverflow.com/questions/15672151/is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit)
