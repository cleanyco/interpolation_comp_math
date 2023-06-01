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


def choose_function(number_of_function):
    return FUNCTIONS[number_of_function]

def print_functions():
    for i in range(len(FUNCTIONS)):
        print(str(i+1) + '. ' + str(FUNCTIONS[i].__str__()))
