import parameters
"""
Deffinitions of the default Cell types and their main atributes.
All cells have local non mobie enviromental states defined in 
LOCAL_DICT. The second form of atribute a cell can have is a
living host. Thes can move from cell to cell. The default states
for a host are defined in HOST_DICT.

The default initial distribution of these host types as of the 
local types are set in HOST_DISTRIBUTION_START and 
LOCAL_DISTRIBUTION_START. No cells should be left without a 
local cell.
"""


LOCAL_DICT = {"value" : 0,
                   "color" : (244,164,96)}#(255,222,173)}
#(255,228,181)}#[255, 248, 220]}


HOST_DICT = {0 : {"value" : 0,
                  "counter" : 0,
                  "color" : [50, 250, 50]},

             1 : {"value"  : 1,
                 "counter" : 0,
                 "color"   : [250, 50, 50]},

             2 : { "value" : 2,
                 "counter" : 0,
                   "color" : [50, 50, 255]}}


HOST_DISTRIBUTION_START = {0 : parameters.HOST_DISTRIBUTION_START["healthy"],
                           1 : parameters.HOST_DISTRIBUTION_START["sick"],
                           2 : parameters.HOST_DISTRIBUTION_START["imune"]}
LOCAL_DISTRIBUTION_START = {0 : 1}