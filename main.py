# --------------------------------------------------------------------------------
# Assignment 1
# Name - Achal Patel
# Student Id - 026598245
# --------------------------------------------------------------------------------
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from patel_achal_assignment1 import Board

# Provide the arguments (filename, obstacle character, free space character, starting point character,
# goal point character)
b = Board("verySmallMaze.lay","%"," ", "P", ".")
b.readFile()
b.createNumberedMatrix()
b.initFinalMat()
b.addValues()
b.printFinalMatrix()