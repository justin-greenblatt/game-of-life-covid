from Graph import Graph
import pygame, sys
from pygame.locals import *
import settings
import gridFunc
import buttonFunctions
from buttonSettings import buttonGen
from copy import deepcopy as deepCopy
import cellSettings

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


#PYGAME SETTUP AND GENERATING MAIN GAME COMPONENTS
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
screen.fill(settings.BACKGROUND_COLOR)
pygame.display.set_caption("Justin Greenblatt's Complexity Generator")
clock = pygame.time.Clock()
gameDict = deepCopy(settings.PARAM_DICT)
gameButtons = buttonFunctions.buttonsCreate(buttonGen(gameDict))
matrix = gridFunc.gridCreate(*gameDict["gridDimensions"])
gameGraph = Graph(gameDict,settings.TEMP_GRAPH_DIR)
iterCount = 0
genCount = 0

#graphs = statsDisplay(settings.STATS_DICT)
if __name__ == "__main__":
    
    #GUI LOOP
    while True:

        x,y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.display.update()

        #SETUP MODE INSTRUCTIONS
        if gameDict["setupMode"]:
            gridFunc.gridInteract(screen, x, y, click, matrix)
            buttonFunctions.buttonsInteract(screen, x, y, click, gameButtons, gameDict)
            
            #screen.blit(image,(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT/5))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()    

        #AFTER RUN STARTS INSTRUCTIONS

        elif gameDict["runMode"]:

            gridFunc.gridIterate(screen,matrix, gameDict)
            gridFunc.gridAndGraphUpdate(screen, matrix, gameDict,gameGraph)
            #graphsUpdate(screen, graphs, settings.STATS_DICT, gameDict)
            gameGraph.plot(screen)
            clock.tick(gameDict["framesPerSecondRun"])
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()    
            iterCount += 1
            if iterCount >= gameDict["experimentIterations"]:
                matrix = gridFunc.gridCreate(*gameDict["gridDimensions"])
                genCount +=1
                iterCount = 0
                if genCount == gameDict["experimentReplicas"]:
                    gameGraph.lastPlot(screen)
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()   
                gameGraph.addGen()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()              

        #EXITING THE GAME

