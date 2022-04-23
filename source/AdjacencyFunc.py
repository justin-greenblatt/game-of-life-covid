"""
Adjacency functions return the neighborhood on wich the cell function 
makes its calculations. It also calls the cell functions that are 
reliant on this particular form of partition. As in many other 
classes in this program it uses decorators to call by recursion 
other possible neighboohood functions you desire to apply.

"""


class AdjacencyFunc():
    
    def __init__(self, cellFunction, AdjDecorator = None):
        self.AdjDecorator = AdjDecorator
        self.cellFunction = cellFunction
    
    def apply(self, i, j, matrix):
        """
        Apply cell functions that are attatched to this partition function
        and possible other partition function using decorator method.
        """
        if self.AdjDecorator != None:
            self.AdjDecorator.apply(i,j,matrix)
        self.cellFunction.apply(*self.adjMatrix(i,j,matrix))


class SoloCell(AdjacencyFunc):
    """
    No neighborhood
    """
    def adjMatrix(self, i, j, matrix):
        
        return (([matrix[i][j]], matrix[i][j]))



class AdjacencyRec(AdjacencyFunc):
    """
    Partition the matrix into a rectangle around the cell of interest.
    """
    def __init__(self, cellFunction, distance = None, up = 1, down = 1, left = 1, right = 1, wrapAround = True, AdjDecorator = None):
        super().__init__(cellFunction, AdjDecorator)
        
        self.wrapAround = wrapAround
        if distance != None:
            self.up = up
            self.down = down
            self.left = left
            self.right = right

        else:
            self.up = distance
            self.down = distance
            self.left = distance
            self.right = distance
    


    def adjMatrix(self, i, j, matrix):
        
        """
        Input: Cell Matrix
        and i,j coordinates of focus cell
        return neighborhood of (i,j) and (i,j) itself
        """

        adjMatrix = []
        m = len(matrix[0])
        n = len(matrix)
        
        if self.wrapAround:
            startRow = (i - self.up) % n
            endRow = (i + self.down + 1) % n
            startCol = (j - self.left) % m
            endCol = (j + self.right + 1) % m

            if startRow < endRow:
                rowSlice = matrix[startRow:endRow]
            else:
                rowSlice = matrix[startRow:] + matrix[:endRow]
            

            if startCol < endCol:
                adjMatrix = [r[startCol:endCol] for r in rowSlice] 
            else:
                adjMatrix = [r[startCol:] + r[:endCol] for r in rowSlice]

        else:
            rowSlice = matrix[max(0, i - self.up):min(n, i + self.down)]
            adjMatrix = [r[max(0, j - self.left):min(m, j + self.right)] for r in rowSlice]

        return (adjMatrix, matrix[i][j])

