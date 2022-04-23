import cellSettings
from random import random

"""
A class for assgning hosts to cells on the creation of the Board
At the moment it uses a dictionary of frequncys of distribution 
of the different types of hosts from cellSettings.HOST_DISTRIBUTION_START
"""

class DistFunc():
    def __init__(self, 
                 hostDistribution = cellSettings.HOST_DISTRIBUTION_START, 
                 localDistribution = cellSettings.LOCAL_DISTRIBUTION_START, 
                 hostDict = cellSettings.HOST_DICT, localDict = cellSettings.LOCAL_DICT):
        self.localDistribution = localDistribution
        self.hostDistribution = hostDistribution
        self.hostDict = hostDict
        self.localDict = localDict

    def initialize(self, r, c):
        return

    def assign(self, block):
        """
        Recieve a Cell and assign a host depending on probabilities
        described by cellSettings.HOST_DISTRIBUTION_START
        """
        for k in self.hostDistribution:
            r = random()
            if r < self.hostDistribution[k]:
                block.setHost(self.hostDict[k])
