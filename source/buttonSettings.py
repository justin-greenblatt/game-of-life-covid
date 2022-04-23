"""
Buttons definitions.
"""


from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from Switch import Switch


def buttonGen(gameDict):
    """
    Generate buttons based on screen settings.
    """
    
    lineHeight = 30
    buttons = {

           "startButton" : {"color" : (60,179,113), 
                            "width": SCREEN_WIDTH/2 - 125,
                            "height": SCREEN_HEIGHT/6,
                            "x" : SCREEN_HEIGHT + 20, 
                            "y" : 20,
                            "text_x" : SCREEN_WIDTH/4 - 100,
                            "text_y" : SCREEN_HEIGHT/13,
                            "text": "START",
                            "switch" : Switch(gameDict, "setupMode" ,False,
                                           Switch(gameDict, "runMode" ,True))}}
    return buttons
"""
"Button3" :      {"color" : (200,250,180), 
                "width": SCREEN_WIDTH /40,
                "height": SCREEN_HEIGHT / 20,
                "x" : SCREEN_HEIGHT + (10 + (SCREEN_WIDTH /20))*2, 
                "y" : lineHeight + (SCREEN_HEIGHT / 10),
                "switch" : None,
                "text": "v",
                "text_x" : 7,
                "text_y" : 5},

"Button4" :      {"color" : (200,250,180),
                "width": SCREEN_WIDTH /20,
                "height": SCREEN_HEIGHT / 20,
                "x" : SCREEN_HEIGHT + (30 + (SCREEN_WIDTH /20))*3, 
                "y" : lineHeight + (SCREEN_HEIGHT / 10),
                "switch" : None,
                "text": "^",
                "text_x" : 5,
                "text_y" : 5},

"Button5" :      {"color" : (200,250,180), 
                "width": SCREEN_WIDTH /20,
                "height": SCREEN_HEIGHT / 20 ,
                "x" : SCREEN_HEIGHT + (30 + (SCREEN_WIDTH /20))*4, 
                "y" : lineHeight + (SCREEN_HEIGHT / 10),
                "switch" : None,
                "text": "^",
                "text_x" : 5,
                "text_y" : 5,},

"Button6" :      {"color" : (200,250,180), 
                "width": SCREEN_WIDTH /20,
                "height": SCREEN_HEIGHT / 20 ,
                "x" : SCREEN_HEIGHT + (30 + (SCREEN_WIDTH /20))*5, 
                "y" : lineHeight + (SCREEN_HEIGHT / 10),
                "switch" : None,
                "text": "^",
                "text_x" : 5,
                "text_y" : 5}}
return buttons
"""