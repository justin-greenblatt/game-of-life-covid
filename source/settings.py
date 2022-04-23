"""
Main settings defining functions to be applied on the cells of the matrix.
And more importantly the size of the matrix and screen.
"""


from gridDimensions import genGridDimensions
from AdjacencyFunc import AdjacencyRec, SoloCell
import cellFunc
from mathFunc import Sigmoid, Linear
import cellSettings
from TransformFunc import TransformToTemplate
import parameters
import os

BACKGROUND_COLOR = [255, 255, 230]
FRAMES_PER_SECOND_SETUP = 60
FRAMES_PER_SECOND_RUN = 20
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300
GRID_SIDE_START = parameters.GRID_SIDE_START
EXPERIMENT_ITERATIONS = parameters.EXPERIMENT_ITERATIONS
EXPERIMENT_REPLICAS = parameters.EXPERIMENT_REPLICAS
TEMP_GRAPH_DIR = os.getcwd() +"/"
PRINT_GRAPH = os. path. realpath(__file__)
INFECTIOUS_PERIOD = parameters.INFECTIOUS_PERIOD
"""
This must have a partitioning function (AdjFunction) with or without decorators encapsulating a
cell evaluation function (CellFunc) that also may have decorators.
""" 
START_CELL_FUNCTIONS =  AdjacencyRec(cellFunction = cellFunc.CounterTransform(
	                            	    transformFrom = 1,
	                            	    transformFunc = TransformToTemplate(cellSettings.HOST_DICT[2]),
	                            	    increment = 1,
	                            	    countTarget = parameters.INFECTIOUS_PERIOD,
	                            	    cFDecorator = cellFunc.StepRandom(
	  	                        	movingTypes = [0,1,2],
	  	                        	cFDecorator = cellFunc.FreqProbTransform(
	  	                        	    transformFrom = 0,
	  	                        	    transformFunc = TransformToTemplate(cellSettings.HOST_DICT[1]), 
	  	                        	    typeOfNeighbor = 1, 
	  	                        	    probabilityFunction = parameters.SICK_DENSITY_INFECTIVITY_FUNCTION))),
                                    distance = 1,
                                    wrapAround = True)


#Dictionary of starting parameters later to be deepcopied and become gameDict in Main.
PARAM_DICT = {"setupMode" : True,
              "runMode" : False,     
              "gridSide" : GRID_SIDE_START,
              "gridSizeMax": 500,
              "gridSizeMin" : 20,
              "gridDimensions" : genGridDimensions(SCREEN_HEIGHT,GRID_SIDE_START),
              "adjacencyFunction" : START_CELL_FUNCTIONS,
              "framesPerSecondRun" : FRAMES_PER_SECOND_RUN,
              "framesPerSecondSetup" : FRAMES_PER_SECOND_SETUP,
              "experimentReplicas" : EXPERIMENT_REPLICAS,
              "experimentIterations" : EXPERIMENT_ITERATIONS,
              "graphMaxY" : round(sum(list(cellSettings.HOST_DISTRIBUTION_START.values()))*(GRID_SIDE_START**2)*1.5),
              "infectiousPeriod" : parameters.INFECTIOUS_PERIOD,     
              "contagability" : parameters.CONTAGABILITY,
              "populationDensity" : parameters.POPULATION_DENSITY
             }
