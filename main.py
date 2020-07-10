import numpy as np

class Board:
    temp_arr=[]
    matrix=None
    file=None
    row_size=None
    col_size=None
    number_matrix=None

    def __init__(self, file):
        super().__init__()
        self.file=file

    def readFile(self):
        f = open(self.file, "r")
        for line in f:
            temp = []
            for i in line:
                if(i!="\n"):
                    temp.append(i)    
            self.temp_arr.append(temp)

        self.matrix = np.array(self.temp_arr)
        print(self.matrix)
    

    def createNumberedMatrix(self):
        self.row_size=self.matrix.shape[0]
        self.col_size=self.matrix.shape[1]
        low_x=1
        t=[]
        for i in range(0, self.row_size):
            high_x=low_x+self.col_size
            temp=list(range(low_x,high_x))
            t.append(temp)
            low_x=high_x

        self.number_matrix=np.array(t)
        print(self.number_matrix)
    
    def getElementFromMatrix(self, m, n):
        return self.matrix[m][n]
    
    

b = Board("smallMaze.lay")
b.readFile()
b.createNumberedMatrix()
print("Element at (0,2): ",b.getElementFromMatrix(0,2))