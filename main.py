import numpy as np
import time

sizeMatrix = 15

def matrixUpdater(matrix):
    newMatrix = np.zeros((sizeMatrix,sizeMatrix)) #make matrix for next generation
    for i in range(sizeMatrix):
        for j in range(sizeMatrix):     #iterates through the matrix
        
            neighbors = np.array([[i-1,j-1],[i-1, j],[i-1, j+1], 
                                  [i,j-1]  ,         [i, j+1], 
                                  [i+1,j-1],[i+1, j],[i+1, j+1]]) # gets positions of neighbor cells
            
            liveNeighbors = 0   # amount of live neighbors
            for k in neighbors:
                    if k[0] in range(sizeMatrix) and k[1] in range(sizeMatrix):
                        if matrix[k[0]][k[1]] == 1:
                            liveNeighbors += 1
            
            if matrix[i][j] == 0:   # dead cell
                if liveNeighbors == 3:
                    newMatrix[i][j] = 1 # become live cell
                    
            else:                   # live cell
                if liveNeighbors < 2:
                    newMatrix[i][j] = 0  # dies of underpopulation
                elif liveNeighbors <= 3:
                    newMatrix[i][j] = 1  # thrives
                else:
                    newMatrix[i][j] = 0  # dies of overpopulation
    np.copyto(matrix, newMatrix)
                
def printGeneration(matrix):
    res = np.empty((sizeMatrix, sizeMatrix),dtype=str)
    for i in range(sizeMatrix):
        for j in range(sizeMatrix):
            if matrix[i][j] == 0:
                res[i][j] = '.'
            else:
                res[i][j] = '#'
    return res


matrix = np.zeros((sizeMatrix,sizeMatrix))

matrix[2][1] = 1
matrix[2][2] = 1
matrix[1][2] = 1
matrix[1][3] = 1
matrix[0][1] = 1

matrix[10][1] = 1
matrix[10][2] = 1
matrix[10][3] = 1

matrix[1][10] = 1
matrix[1][11] = 1
matrix[1][12] = 1
matrix[2][9] = 1
matrix[2][10] = 1
matrix[2][11] = 1

res = printGeneration(matrix)
print(res)

while(True):
    time.sleep(.25)
    matrixUpdater(matrix)
    res = printGeneration(matrix)
    print(res)


