from Block import Block
from copy import deepcopy

class Cell(Block):
    """
    The class representing a cell of the board
    """
    def __init__(self, color, width, height,x_pos = None, y_pos = None, text = None,value = 0, font_type = 'ubuntumono', font_size = 20,
     text_color = [0,0,0], text_x = 5, text_y = 5, direction = 0, index_x = None, index_y = None):
        """
        Pass graphic elements to super and add fields that are specific to a board cell, such as host, local (environment), and
        transform functions.
        """

        super().__init__(color, width, height, x_pos, y_pos, text, value, font_type, 
                         font_size, text_color, text, text_y, direction, index_x, index_y)
 
        self.local =  {"value" : 0, "color" : [255, 248, 220]}
        self.host = None
        self.nextHost = None
        self.deleteOldHost = False
        self.transformFunctions = []



    def setLocal(self, newLocal):
        """
        Input: Dictionary
        create new instance from template dictionary and set it to local.
        Usualy you would give on of the templates at cellSettings.LOCAL_DICT
        """
        self.local = deepcopy(newLocal)



    def setHost(self, newHost):
        """
        Input: Dictionary
        create new instance from template dictionary and set it to host.
        Usualy you would give on of the templates at cellSettings.HOST_DICT
        """
        self.host = deepcopy(newHost)
        self.nextHost = self.host



    def cellUpdate(self):
        """
        Important function for the whole program. After all cells have calculated their 
        next step. They need to modify themselfs. They can not do this right after the 
        calculation as this would go against the rules of the Game of life. They must
        switch states after all cells have done their calculations.In this function
        The cell takes care of its graphical representation as executes any modifications
        to its host. After that it sends the host to another cell.
        """
        
        self.paint()#Gui Graphics
        
        #Execute any transformations to HOST or LOCAL
        for f in self.transformFunctions:
            f.transform(self)
        self.transformFunctions.clear()

        #Accept next host.
        self.host = self.nextHost


    def getColor(self):
        """
        Return the color to paint the cell giving priority to the host
        color above local color.
        """
        if self.host != None:
            return self.host["color"]
        elif self.local != None:
            return self.local["color"]
        return (40,40,40)# Default cell color. Though all cell should ate least have local atribute set


    def paint(self):
        """
        GUI function for painting
        """
        self.image.fill(self.getColor())
 

    def paintDark(self):
        """
        Paint a darker version of the color. Used when cursor is above cell
        """
        c = self.getColor()
        self.image.fill((max(0, c[0] - 50),
                         max(0, c[1] - 50),
                         max(0, c[2] - 50)))


    def getIndex(self):
        """
        Used for debuging
        """
        return (self.index_x, self.index_y)