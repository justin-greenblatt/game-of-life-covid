from Block import Block

def createButtons(buttonParams):
    
    buttons = []
    for b in buttonParams:
    	block = Block(b["color"], b["width"], b["height"], b["x"], b["y"])
        buttons.append(block)
    return buttons

def interactButtons(screen, x, y, click, buttons, CELL_COLORS):

	for s in buttons:
	            
	    if s.rect.collidepoint(x,y):
	        
	        if click[0] == True:

	            s.image.fill(min(s.color[0] + 30, 255), min(s.color[1] + 30, 255), min(s.color[2] + 30, 255))
	        
	        else:

	            s.image.fill(max(0,s.color[0] - 100), max(0,s.color[1] - 100), max(0,s.color[2] - 100))
	    else:
	        s.image.fill(s.color)
	    screen.blit(s.image, s.rect)


