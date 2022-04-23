import pygame

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height,x_pos = None, y_pos = None, text = None,value = 0, font_type = 'ubuntumono', font_size = 20, text_color = [0,0,0], text_x = 5, text_y = 5, direction = 0, index_x = None, index_y = None):
        """
        Basic GUI block with optional text
        """
        super().__init__()
 
        self.size = [width,height]
        self.image = pygame.Surface(self.size)
        self.image.fill(color)
        self.color = color
        self.index_y = index_y
        self.index_x = index_x
        self.x = x_pos
        self.y = y_pos
        self.text_x = text_x
        self.text_y = text_y
        self.text = text
        self.font_type = font_type
        self.font_size = font_size
        self.text_color = text_color
        self.rect = self.image.get_rect()
        self.value = value
        self.nextValue = value
        self.counter = 0
        self.counted = False

    def update(self, txt):
        self.text = txt
        self.image.fill(self.color)
        self.textsurface = self.font.render(self.text, False, self.text_color)
        self.image.blit(self.textsurface,(self.text_x, self.text_y))

    def change_text(self, data_pos):
        data_pos = data_pos + self.diection
        
        return data_pos