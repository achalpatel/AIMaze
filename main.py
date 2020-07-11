import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

class Board:
    matrix=None
    file=None
    row_size=None
    col_size=None
    number_matrix=None
    final_matrix=None

    def __init__(self, file, char_obs, char_free, char_start, char_end):
        super().__init__()
        self.file=file
        self.char_obstacle=char_obs
        self.char_freeway=char_free
        self.char_start=char_start
        self.char_end=char_end

    def readFile(self):
        temp_arr=[]
        f = open(self.file, "r")
        for line in f:
            temp = []
            for i in line:
                if(i!="\n"):
                    temp.append(i)    
            temp_arr.append(temp)

        self.matrix = np.array(temp_arr)
        print(self.matrix)
    

    def createNumberedMatrix(self):
        self.row_size=self.matrix.shape[0]
        self.col_size=self.matrix.shape[1]
        low_x=0
        t=[]
        for i in range(0, self.row_size):
            high_x=low_x+self.col_size
            temp=list(range(low_x,high_x))
            t.append(temp)
            low_x=high_x

        self.number_matrix=np.array(t)
        print(self.number_matrix)
    
    def getElementFromMatrix(self, m, n):
        try:
            return self.matrix[m][n]    
        except IndexError:
            return None
        
    
    def initFinalMat(self):
        self.final_matrix=np.zeros((self.col_size*self.row_size, self.col_size*self.row_size))

    def addValues(self):
        for i in range(0, self.row_size):
            for j in range(0, self.col_size):
                num = self.number_matrix[i][j]
                char = self.matrix[i][j]
                if(char!=self.char_obstacle):
                    if(i-1>=0 and self.matrix[i-1][j]!=self.char_obstacle):                       
                       self.final_matrix[num][self.number_matrix[i-1][j]] = 1
                    if(i+1<=self.row_size-1 and self.matrix[i+1][j]!=self.char_obstacle):                       
                       self.final_matrix[num][self.number_matrix[i+1][j]] = 1
                    if(j-1>=0 and self.matrix[i][j-1]!=self.char_obstacle):                       
                       self.final_matrix[num][self.number_matrix[i][j-1]] = 1
                    if(j+1<=self.col_size-1 and self.matrix[i][j+1]!=self.char_obstacle):                       
                       self.final_matrix[num][self.number_matrix[i][j+1]] = 1

    def printFinalMatrix(self):
        for i in range(0, self.final_matrix.shape[0]):
            print("index = ",i, self.final_matrix[i])
    

    def getStartPos(self):
        for i in range(0,self.row_size):
            for j in range(0, self.col_size):
                if(self.matrix[i][j]==self.char_start):
                    return (i,j)

    def getEndPos(self):
        for i in range(0,self.row_size):
            for j in range(0, self.col_size):
                if(self.matrix[i][j]==self.char_end):
                    return (i,j)
        
    # Testing purpose
    def getOnesPos(self):
        l=[]
        for i in range(0, self.final_matrix.shape[0]):
            for j in range(0, self.final_matrix.shape[1]):
                if(self.final_matrix[i][j]==1):
                    l.append((i,j))
        return np.array(l)
    
    # Testing purpose
    def readAnswerMatrix(self, file):
        f = open(file, 'r')
        arr=[]
        for line in f:
            temp=[]
            for i in line:
                if(i!="\n" and i!="\t"):
                    temp.append(i)
                td=list(temp)
            arr.append(td)
        ans_arr=np.array(arr)
        ones_list=[]
        for i in range(0,ans_arr.shape[0]):
            for j in range(0, ans_arr.shape[1]):
                if(ans_arr[i][j]=='1'):
                    ones_list.append((i,j))
        # print(np.array(ones_list))
        return ones_list


b = Board("smallMaze.lay","%"," ", "P", ".")
b.readFile()
b.createNumberedMatrix()
b.initFinalMat()
b.addValues()
# b.printFinalMatrix()
# start_ind = b.getStartPos()
# end_ind = b.getEndPos()
# print("start:", start_ind)
# print("end ",end_ind)
b.readAnswerMatrix("smallMatrix.txt")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
b.getOnesPos()

