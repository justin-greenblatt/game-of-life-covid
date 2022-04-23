class AdjacencyRec:

    def__init__(i, j, matrix, distance = 1, wrapAround = True):

        self.i = i
        self.j = j
        self.matrix = matrix
        self.m = len(matrix[0])
        self.n = len(matrix)
        self.adjMatrix = []
        self.adjCellArray = []
        self.cell = matrix[i % n][j % m]
        
        if wrapAround:
            for line,a in enumerate(range((i - distance) % n, (i + distance + 1) % n)):
        	    self.adjMatrix.append([])
                for b in range((j - distance) % n, (j + distance + 1) % n)
                    self.adjCellArray.append[matrix[a][b]]
                    self.adjMatrix[line].append(append[matrix[a][b]])

        else:
            for line,a in enumerate(range((i - distance), (i + distance + 1))):
        	    self.adjMatrix.append([])
                for b in range((j - distance), (j + distance + 1))
                    self.adjCellArray.append[matrix[a][b]]
                    self.adjMatrix[line].append(append[matrix[a][b]])


    def getCells(self):
    	return self.adjCellArray

    def getAdjMatrix(self):
    	return self.adjMatrix