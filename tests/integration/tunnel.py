'''
This is a small utility code that makes the path located 2 directories up from the current file 
    which simply makes Quick available to tests that import this file.
'''


# this bit of code allows us to import Quick while being in a different directory that 
#    Quick is contained in
import sys
sys.path.append('../../.')
