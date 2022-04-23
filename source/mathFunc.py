from math import e


class MathFunc():
    """
    Mathematical function class for calculating probability functions used in
    cell Transformation or distribution. Uses decorators to build more complicated
    expressions. (IIIIIIIIIIIHHHHHAAAAAAAAAA   LOVE ME SOME DECORATORS!!!!!!!!!!)
    """

    def __init__(self, varDict = None, mathFuncDecorator = None):
        """
        variable dictionary for evaluation.
        """
        self.var = varDict
        self.mathFuncDecorator = mathFuncDecorator

    def evaluate(self, x):
        #evaluate based on X
        if self.mathFuncDecorator != None:
            result = self.calc(self.mathFuncDecorator.calc(x))
        else:
            result = self.calc(x)
        return result


class Linear(MathFunc):
    #function with the basic ax + b formulation.
    def calc(self, x):
        return (self.var['a']*x) + self.var['b']

class Sigmoid(MathFunc):
    #A sigmoid function ssssssssssssssssssss
    def calc(self, x):
        return 1/(1 + e ** (-1 * x))