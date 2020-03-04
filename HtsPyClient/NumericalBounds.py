class NumericalBounds:
    def __init__(self, lowerFail: float, lowerWarn: float, upperWarn: float, upperFail: float):
        self.lowerFail = lowerFail
        self.lowerWarn = lowerWarn
        self.upperWarn = upperWarn
        self.upperFail = upperFail