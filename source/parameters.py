import mathFunc

INFECTIOUS_PERIOD = 30# Number of days it takes for sick to become imune

GRID_SIDE_START = 100# Side of a the board (if it is a 500*500 board give 500)

EXPERIMENT_ITERATIONS = 100 #Number of iterations of the automata

EXPERIMENT_REPLICAS = 3# Times to run the same experiment

POPULATION_DENSITY = 0.05 #AVERAGE PEOPLE PER SQUARE
INITIAL_SICK_PCT = 1
INITIAL_IMUNE_PCT = 1
INITIAL_HEALTHY_PCT = 100 - (INITIAL_IMUNE_PCT + INITIAL_SICK_PCT)
HOST_DISTRIBUTION_START = {"healthy" : (INITIAL_HEALTHY_PCT/100) * POPULATION_DENSITY,
 "sick" : (INITIAL_SICK_PCT/100) * POPULATION_DENSITY, "imune" : (INITIAL_IMUNE_PCT/100) * POPULATION_DENSITY} #Density of distribution of initial state.

"""
Function to calculate the chance of a cell being infected by its surounding. The argument "x" is the amount of neighbors infected.
the result "y" is the probability you will be infected from 0 to 1
"""

CONTAGABILITY = 0.5

INDEPENDENT_SICKENNING_FACTOR = 0.01 

SICK_DENSITY_INFECTIVITY_FUNCTION = mathFunc.Linear(varDict = {'a' : CONTAGABILITY, 'b' : INDEPENDENT_SICKENNING_FACTOR})
