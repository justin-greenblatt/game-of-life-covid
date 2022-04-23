"""
These functions recieve the AjacencyMatrix (or Partition of the matrix relative to each cell)
and calculates the next step for the cell Host. It give the cell a Transform function to be 
executed before the next iteration or set a nextCell for it to migrate. All cell functions 
Use a decorator pattern for combining different cellFunctions. The decorator recieves the 
same partition as its given to its 'father' object.
"""

from random import random, randint
from copy import copy

class CellFunc:
    """
    Base class for cell functions describing decorator functionality.
    """
    def __init__(self, cFDecorator = None):
        #self.statsDict = statsSettings.STATS_DICT      
        self.cFDecorator = cFDecorator

    def apply(self, adjMatrix, focusCell):
        """
        Recieve board/Matrix partition. The cell that is to be 
        evaluated. Recirsively call decorator.
        """
        if self.cFDecorator != None:
            self.cFDecorator.apply(adjMatrix, focusCell)
        self.calcNextValue(adjMatrix, focusCell)

class CounterTransform(CellFunc):
    """
    Utilize a counter of the host to activate a transform Function.
    This function ignores the partition and focuses on the counter
    atribute of the host. 
    """
    def __init__(self, 
                 transformFrom,
                 transformFunc, 
                 increment, 
                 countTarget,
                 cFDecorator = None):

        super().__init__(cFDecorator)
        self.transformFrom = transformFrom
        self.transformFunc = transformFunc
        self.increment = increment
        self.countTarget = countTarget
    
    def calcNextValue(self, adjMatrix, focusCell):
        """
        Increment the counter of the host or activate transform
        function if counter has reached target.
        """
        if focusCell.host != None and not focusCell.deleteOldHost:
            if focusCell.host["value"] == self.transformFrom:
                if focusCell.host["counter"] >= self.countTarget:
                    focusCell.transformFunctions.append(self.transformFunc)
                else:
                    focusCell.host["counter"] += self.increment
            

class StepRandom(CellFunc):
    """
    Choose a cell in the adjMatrix/Partition of Board/CellNeighborhood to 
    move the cell host to on next Turn. It randomly moves the host to cells
    that are in this partition and that do not have hosts and that are not 
    expecting any hosts on the next turn. This assures no collisions will
    occur. 
    """
    def __init__(self, movingTypes = range(1,200000), cFDecorator = None):
        """
        Recieve arguments of parent class CellFunc as well as a list of 
        types of hosts on board that are defined as mobile.
        """
        super().__init__(cFDecorator)
        self.movingTypes = movingTypes
    
    def calcNextValue(self, adjMatrix, focusCell, hostDictKey = "value"):
        """
        Recieves hostDictKey that is the key of the host atribute for comparisson with the movingTypes list.
        focusCell is the cell to calculate its movement.AdjMatrix is the focusCell neighborhood calculated by
        the AdjFunction (AdjacencyFunction). The function now searches for empty cells in this neighborhood 
        (EMPTY IN THIS ITERATION AND NEXT ITERATION) and randomly assigns the host to one of the cells that 
        pass this condition. There is also the equal chance of the cell not moving and continuing in its cell. 
        """
        if focusCell.host != None: #check if the cell is not empty

            #Check if the host is in moving types.
            if (focusCell.host[hostDictKey] in self.movingTypes) and (not focusCell.deleteOldHost):
                #filter for free cells in neighborhood
                freeAdjacentCells = [a for b in adjMatrix for a in b if (a.host == None and a.nextHost == None)]
                nFree = len(freeAdjacentCells)
                
                #if there are any free cells
                if nFree > 0:
                    #randomly select freecell (considering the possibililty of staying stationary)
                    r = randint(-1,nFree - 1)
                    #if the random integer is equal to -1 than stay stationary. If it is larger MOVE
                    if r >= 0:
                        #Choose next cell to move to.
                        nextCell = freeAdjacentCells[r]
                        #move host to next cell
                        nextCell.nextHost = focusCell.host
                        #this next cell is empty.
                        focusCell.nextHost = None
                    else:
                        #Stay stationary.
                        focusCell.nextHost = focusCell.host
                else:
                    #there are no cells to available in your neighborhood. Stay stationary.
                    focusCell.nextHost = focusCell.host



class FreqProbTransform(CellFunc):
    """
    Use a frequency based function that returns a probability for cell to transform.
    """
    def __init__(self,
                 transformFrom,
                 transformFunc,
                 typeOfNeighbor,
                 probabilityFunction,
                 cFDecorator = None):

        super().__init__(cFDecorator)

        self.transformFunc = transformFunc
        self.transformFrom = transformFrom
        self.typeOfNeighbor = typeOfNeighbor
        self.func = probabilityFunction
    
    def calcNextValue(self, adjMatrix, focusCell):
        """
        Evaluate probability function and use that probability to assign transformation to the cell in focus.
        """
        if focusCell.host != None:
            
            if focusCell.host["value"] == self.transformFrom:              
                
                typeCount = len([a for b in adjMatrix for a in [c for c in b if c.host != None] if a.host["value"] == self.typeOfNeighbor])
                
                if random() < self.func.evaluate(typeCount):
                    focusCell.transformFunctions.append(self.transformFunc)


class TransformIfEqual(CellFunc):
    """
    NEEDS TO BE UPDATED!!!!!! TO CELL HOST SYSTEM
    Transfrom if amount of neighbors of a specific type is equal to a specific number. 
    """
    def __init__(self, transfromTo,
                       transformFrom,
                       typeOfNeighbor,
                       amountOfNeighbors,
                       transfomProbability = 1,
                       cFDecorator = None):

        super().__init__(cFDecorator)
        self.transfromTo = transfromTo
        self.transformFrom = transformFrom 
        self.typeOfNeighbor = typeOfNeighbor
        self.amountOfNeighbors = amountOfNeighbors
        self.transfomProbability = transfomProbability

    def calcNextValue(self, adjMatrix, focusCell):

        if focusCell.value == self.transformFrom:
                
            if len(list([a for b in adjMatrix for a in b if a.value == self.typeOfNeighbor])) == self.amountOfNeighbors:                    
                if random() <= self.transfomProbability:
                    focusCell.nextValue = self.transfromTo

class TransformIfMoreThan(TransformIfEqual):
    """
    NEEDS TO BE UPDATED!!!!!! TO CELL HOST SYSTEM
    Transfrom if amount of neighbors of a specific type IS LARGER THAN a specific number. 
    """
    def calcNextValue(self, adjMatrix, focusCell):

        if focusCell.value == self.transformFrom:
                
            if len(list([a for b in adjMatrix for a in b if a.value == self.typeOfNeighbor])) > self.amountOfNeighbors:                    
                if random() <= self.transfomProbability:
                    focusCell.nextValue = self.transfromTo

class TransformIfLessThan(TransformIfEqual):
    """
    NEEDS TO BE UPDATED!!!!!! TO CELL HOST SYSTEM
    Transfrom if amount of neighbors of a specific type IS LESS THAN a specific number. 
    """
    def calcNextValue(self, adjMatrix, focusCell):

        if focusCell.value == self.transformFrom:
                
            if len(list([a for b in adjMatrix for a in b if a.value == self.typeOfNeighbor])) < self.amountOfNeighbors:                    
                if random() <= self.transfomProbability:
                    focusCell.nextValue = self.transfromTo

class TransformIfInInterval(TransformIfEqual):
    """
    NEEDS TO BE UPDATED!!!!!! TO CELL HOST SYSTEM
    Transfrom if amount of neighbors of a specific type IN THE INTERVAL defined by two specific numbers. 
    """
    def calcNextValue(self, adjMatrix, focusCell):

        if focusCell.value == self.transformFrom:
                
            typeCount = len(list([a for b in adjMatrix for a in b if a.value == self.typeOfNeighbor]))

            if typeCount >= self.amountOfNeighbors[0] and typeCount <= self.amountOfNeighbors[1]:                    
                if random() <= self.transfomProbability:
                    focusCell.nextValue = self.transfromTo
           
class TransformIfNotInInterval(TransformIfEqual):
    """
    NEEDS TO BE UPDATED!!!!!! TO CELL HOST SYSTEM
    Transfrom if amount of neighbors of a specific type OUT OF THE INVERVAL of two specific number. 
    """
    def calcNextValue(self, adjMatrix, focusCell):

        if focusCell.value == self.transformFrom:
                
            typeCount = len(list([a for b in adjMatrix for a in b if a.value == self.typeOfNeighbor]))

            if typeCount < self.amountOfNeighbors[0] and typeCount > self.amountOfNeighbors[1]:                    
                if random() <= self.transfomProbability:
                    focusCell.nextValue = self.transfromTo
