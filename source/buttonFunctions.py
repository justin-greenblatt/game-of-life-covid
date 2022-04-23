from Block import Block
from Button import Button

"""
Functions for creating and interacting with buttons from the panel.
"""


def buttonsCreate(buttonParams):
    """
    Transform a dictionary with button parameters destribed in Settings
    to Button objects and return a list of buttons
    """

    buttons = []
    for b in buttonParams.values():
        block = Button(b["color"], b["width"], b["height"], b["x"], b["y"], b["switch"],
                text = b["text"], text_x = b["text_x"], text_y = b["text_y"])
        block.rect.x = b['x']
        block.rect.y = b['y']
        buttons.append(block)
    return buttons

def buttonsInteract(screen, x, y, click, buttons, CELL_COLORS):
    
    """
    Iterate over buttons and identify if the mouse is interacting with them
    x,y are mouse coordinates. Click is a boolean indicating mouse clicks.
    """
    for s in buttons:
                
        if s.rect.collidepoint(x,y):
            
            if click[0] == True:

                s.image.fill((min(s.color[0] + 30, 255), min(s.color[1] + 30, 255), min(s.color[2] + 30, 255)))
                s.onClick()
            else:

                s.image.fill((max(0,s.color[0] - 100), max(0,s.color[1] - 100), max(0,s.color[2] - 100)))
        else:
            s.image.fill(s.color)
        s.textsurface = s.font.render(s.text, False, s.text_color)
        s.image.blit(s.textsurface,(s.text_x, s.text_y))

        screen.blit(s.image, s.rect)