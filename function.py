class Function:
    def __init__(self, expr):
        self.__expr = expr

    def __call__(self, x):
        return eval(self.__expr)

    def __str__(self):
        return self.__expr


FUNCTIONS = [
    Function('2 * x**2 - 8 * x + 1'),
    Function('np.sqrt(x) / 2'),
    Function('np.sin(x)')
]


# def choose_function():
    # TODO complete