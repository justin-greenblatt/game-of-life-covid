"""
Class to be passed to a cell function. The Transform function if applied is enquede and
applid to the host later in the next iteration.
"""

class TransformToTemplate():
    """
    Use another host template to modify this host.
    """
    def __init__(self, templateDict):
        self.templateDict = templateDict

    def transform(self, modifyCell):
        for k in self.templateDict:
            modifyCell.host[k] = self.templateDict[k]