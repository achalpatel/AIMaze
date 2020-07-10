import numpy as np

class Board:
    temp_arr=[]
    matrix=None
    file=None
    row_size=None
    col_size=None
    number_matrix=None
    final_matrix=None

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
        # print(self.number_matrix)
    
    def getElementFromMatrix(self, m, n):
        try:
            return self.matrix[m][n]    
        except IndexError:
            return None
        
    
    def initFinalMat(self):
        self.final_matrix=np.zeros((self.col_size*self.row_size, self.col_size*self.row_size))

    # def addValues(self):
    #     for i in range(0, self.row_size):
    #         for j in range(0, self.col_size):
                


b = Board("smallMaze.lay")
b.readFile()
b.createNumberedMatrix()
b.initFinalMat()
print("Element at (0,-1): ",b.getElementFromMatrix(1,1))