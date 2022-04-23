import pygame
from Block import Block

class Button(Block):
    """
    Button class for the Gui Panel. Activates events in the game.
    """
    def __init__(self, color, width, height,x_pos = None, y_pos = None, switch = None, text = None,value = 0, font_type = 'ubuntumono', font_size = 20, text_color = [0,0,0], text_x = 5, text_y = 5, direction = 0, index_x = None, index_y = None):

        super().__init__(color, width, height,x_pos, y_pos, text, value, font_type, font_size, text_color, text_x, text_y, direction, index_x, index_y)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.switch = switch

    def onClick(self):

    	if self.switch != None:
    	    self.switch.apply()

