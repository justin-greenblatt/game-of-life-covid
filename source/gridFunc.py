"""
Functions for interacting and initializing the cell Board.
"""
from collections import Counter
import pygame
from Cell import Cell
from random import random
import DistFunc
import cellSettings



def gridCreate(p_x, p_y, x_motor, y_motor, frame_width, frame_height, cols, rows, distFunction = DistFunc.DistFunc()):
    """
    Create board with given parameters (Names are weird and some parts dont make sense couse a snatched it from an
    older robotics project I had.)
    
    p_x - lop left corner x 
    p_y - lop left corner y
    x_motor - distance between cells on x
    y_motor - distance between cells on y
    frame_width - cell width
    frame_height - cell height
    cols - amount of columns in board 
    rows - amount of rows on board
    distFunction - distribution function for hosts on board.
    """
    distFunction.initialize(rows,cols)
    grid_color = [225,225,255]
    overlap_color = [180,180,210]
    block_matrix = []
    block_line = []
    overlap_x = frame_width - x_motor
    overlap_y = frame_height - y_motor
    pos_y = p_y

    for i in range(rows):
        pos_x = p_x
        for l in range(cols):
            
                 
            if l == 0 or l == (cols-1):
                draw_width = frame_width - overlap_x
            else:
                draw_width = frame_width - (2*overlap_x)
            if i == 0 or i == (rows - 1):
                draw_height = frame_height - overlap_y
            else:
                draw_height = frame_height - (2*overlap_y)
            
            if l != 0 and i != 0:
                block = Cell(grid_color,draw_width,draw_height,(pos_x - overlap_x),(pos_y - overlap_y),index_x = l,index_y = i)
            elif l != 0:
                block = Cell(grid_color,draw_width,draw_height,(pos_x - overlap_x),pos_y,index_x = l,index_y = i)
            elif i != 0:
                block = Cell(grid_color,draw_width,draw_height,pos_x,(pos_y - overlap_y),index_x = l,index_y = i)
            else:
                block = Cell(grid_color,draw_width,draw_height,pos_x,pos_y,index_x = l,index_y = i)
            block.rect.x = pos_x
            block.rect.y = pos_y
            
            distFunction.assign(block)
            block_line.append(block)
           
            if i != (rows-1):
                over  =  Cell(overlap_color,draw_width,overlap_y) 
                over.rect.x = pos_x 
                over.rect.y = pos_y + draw_height

            pos_x = pos_x + draw_width
            if l != (cols-1):
                if i != (rows-1):
                    over  =  Cell(overlap_color,overlap_x,(draw_height + overlap_y)) 
                    over.rect.x = pos_x 
                    over.rect.y = pos_y

                    pos_x = pos_x + overlap_x
                else:
                    over  =  Cell(overlap_color,overlap_x,draw_height) 
                    over.rect.x = pos_x 
                    over.rect.y = pos_y

                    pos_x = pos_x + overlap_x

        block_matrix.append(block_line)
        block_line = []
        pos_y = pos_y + draw_height + overlap_y
        
    return block_matrix



def gridAndGraphUpdate(screen, matrix, paramDict, graph, counterKey = "value", percentage = True):
    """
    Iterate over all cells, update them and draw them on screen
    """
    totalHosts = 0
    hostCounter = {}
    for k in cellSettings.HOST_DICT:
        hostCounter[k] = 0

    for i,line in enumerate(matrix):
        for j,s in enumerate(line):
            if s.host != None:
                totalHosts +=1
                hostCounter[s.host[counterKey]] += 1
            screen.blit(s.image, s.rect)
            s.cellUpdate()
    if percentage:
        for k in hostCounter:
            hostCounter[k] = (hostCounter[k] / totalHosts)*100
    graph.addIter(hostCounter)



def countTotalHosts(matrix):
    counter = 0
    for i,line in enumerate(matrix):
        for j,s in enumerate(line):
            if s.host != None:
                counter +=1
    return counter

def gridInteract(screen, x, y, click, matrix): 
        """
        Interact with cells through GUI. Check for clicks.
        """
        for i,line in enumerate(matrix):
            for j,s in enumerate(line):
                
                if s.rect.collidepoint(x,y):
                    if click[0] == True:
                        if s.host == None:
                            s.setHost(cellSettings.HOST_DICT[0])
                        else: 
                            s.setHost(cellSettings.HOST_DICT[(s.host["value"] + 1) % len(cellSettings.HOST_DICT)])
                    else:
                        s.paintDark()

                else:

                    s.paint()
                screen.blit(s.image, s.rect)
                


def gridIterate(screen, matrix, paramDict):
    """
    Iterate over cells in grid and calculate their next state. The calculations are done
    by an adjacency function (neighborhood function) encapsulating cell evaluation functions.
    All is explained in Settings.
    """
    for i,line in enumerate(matrix):
        for j,s in enumerate(line):
            paramDict["adjacencyFunction"].apply(i,j,matrix)