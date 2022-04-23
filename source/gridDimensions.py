from math import floor, ceil

def genGridDimensions(screenHeight, gridSide):

    gridDimensions = (ceil((screenHeight - (floor(max(1,(screenHeight - 20)/gridSide))*gridSide))/2),
    
	     ceil((screenHeight - (floor(max(1,(screenHeight - 20)/gridSide))*gridSide))/2),
	     floor(max(1,((screenHeight - 20)/gridSide)-1)),
	     floor(max(1,((screenHeight - 20)/gridSide)-1)),
	     floor(max(0,(screenHeight - 20)/gridSide)),
	     floor(max(0,(screenHeight - 20)/gridSide)),
	     gridSide, gridSide)

    return gridDimensions