from statistics import mean, variance
import matplotlib.pyplot as plt
import settings
import cellSettings
import pygame
import settings

class Graph():
    def __init__(self, gameDict, tempPlotDir, celltypes = cellSettings.HOST_DICT, graphFlavor = None):
        self.celltypes = celltypes
        self.statsDict = {}
        self.statsDict[0] = dict({k:[] for k in celltypes})
        self.gameDict = gameDict
        self.graphFlavor = graphFlavor
        self.tempPlotDir = tempPlotDir
        self.background = self.rgba(settings.BACKGROUND_COLOR)
        self.title = "Board Size: " + str(self.gameDict["gridSide"]) + "   Infectious period: " + str(self.gameDict["infectiousPeriod"]) + "   Contagability: " + str(self.gameDict["contagability"]) + "   Population Density: " + str(self.gameDict["populationDensity"])
        
        self.dir = self.tempPlotDir + "Bs" + str(self.gameDict["gridSide"]) + "Ip" + str(self.gameDict["infectiousPeriod"]) + "C" + str(self.gameDict["contagability"]) + "pD" + str(self.gameDict["populationDensity"]) + ".png"
    
    def graphColor(self,n, alpha = 1):
        colors =  list([c/255 for c in cellSettings.HOST_DICT[n]["color"]])
        colors.append(alpha)
        return tuple(colors)

    def rgba(self, rgb, alpha = 1):
        colors =  list([c/255 for c in rgb])
        colors.append(alpha)
        return tuple(colors)

    def plot(self, screen):

        fig = plt.figure()
        ax = plt.subplot(111)
        
        for g in self.statsDict:
        
            for k in self.statsDict[g]:
                ax.plot(range(len(self.statsDict[g][k])), self.statsDict[g][k],
                 color = self.graphColor(k, 0.3), linewidth= 1.0)
        
        plt.title(self.title, fontsize=10)
        plt.xticks(range(0, round(self.gameDict["experimentIterations"]) + 1, round(self.gameDict["experimentIterations"]/10)))
        plt.yticks(range(0, 101, 10))
        ax.set_facecolor(self.background)
        fig.savefig(self.dir, facecolor= self.background)
        image = pygame.image.load(self.dir)
        screen.blit(image,(round(settings.SCREEN_WIDTH/2), round(settings.SCREEN_HEIGHT / 5)))
        
    def addGen(self):

        self.statsDict[len(self.statsDict)] = dict({k:[] for k in self.celltypes})

    def addIter(self, counter):
        for h in counter:
            self.statsDict[len(self.statsDict) -1][h].append(counter[h])

    def lastPlot(self, screen):

        fig = plt.figure()
        ax = plt.subplot(111)
        
        for g in self.statsDict:
        
            for k in self.statsDict[g]:
                ax.plot(range(len(self.statsDict[g][k])), self.statsDict[g][k],
                 color = self.graphColor(k, 0.2), linewidth= 1.0)
        
        means = []
        for k in self.celltypes:
            means.append([])
            for t in range(self.gameDict["experimentIterations"]):
                w = []    
                for r in range(self.gameDict["experimentReplicas"]):
                    w.append(self.statsDict[r][k][t])
                means[k].append(mean(w))
            
            ax.plot(range(self.gameDict["experimentIterations"]), means[k],
                 color = self.graphColor(k), linewidth = 7.0)
        

        plt.title(self.title, fontsize=10)
        plt.xticks(range(0, round(self.gameDict["experimentIterations"]) + 1, round(self.gameDict["experimentIterations"]/10)))
        plt.yticks(range(0, 101, 10))
        ax.set_facecolor(self.background)
        fig.savefig(self.dir, facecolor= self.background)
        image = pygame.image.load(self.dir)
        
        screen.blit(image,(round(settings.SCREEN_WIDTH/2), round(settings.SCREEN_HEIGHT / 5)))
        pygame.display.update()


    
