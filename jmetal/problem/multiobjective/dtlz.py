from math import pi, cos, sin

from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution

"""
.. module:: `dtlz`
   :platform: Unix, Windows
   :synopsis: DTLZ problem family of multi-objective problems.

.. moduleauthor:: Antonio J. Nebro <antonio@lcc.uma.es>
"""


class DTLZ1(FloatProblem):
    """ Problem DTLZ1
    .. note:: Unconstrained problem. The default number of variables and objectives are, respectively, 7 and 3.
    .. note:: Continuous problem having a linear Pareto front
    """

    def __init__(self, number_of_variables: int = 7, number_of_objectives = 3):
        """Constructor
        :param number_of_variables: number of decision variables of the problem
        """
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        g = 0.0
        k = self.number_of_variables - self.number_of_objectives + 1
        for i in range (self.number_of_variables - k, self.number_of_variables):
            g += (solution.variables[i] - 0.5) * (solution.variables[i] - 0.5) - \
                 cos(20.0 * pi * (solution.variables[i] - 0.5))

        g = 100 * (k + g)
        for i in range(self.number_of_objectives):
            solution.objectives[i] = (1.0 + g) * 0.5

        for i in range(self.number_of_objectives):
            for j in range(self.number_of_objectives - (i + 1)):
                solution.objectives[i] *= solution.variables[j]

            if i != 0:
                aux = self.number_of_objectives - (i + 1)
                solution.objectives[i] *= 1 - solution.variables[aux]

    def get_name(self):
        return "DTLZ1"


class DTLZ2(FloatProblem):
    """ Problem DTLZ2
    .. note:: Unconstrained problem. The default number of variables and objectives are, respectively, 12 and 3.
    .. note:: Continuous problem having a convex Pareto front
    """

    def __init__(self, number_of_variables: int = 12, number_of_objectives = 3):
        """Constructor
        :param number_of_variables: number of decision variables of the problem
        """
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        g = 0.0
        k = self.number_of_variables - self.number_of_objectives + 1

        for i in range (self.number_of_variables - k, self.number_of_variables):
            g += (solution.variables[i] - 0.5) * (solution.variables[i] - 0.5)

        for i in range(self.number_of_objectives):
            solution.objectives[i] = 1.0 + g

        for i in range(self.number_of_objectives):
            for j in range(self.number_of_objectives - (i + 1)):
                solution.objectives[i] *= cos(solution.variables[j]) * pi
            if i != 0:
                aux = self.number_of_objectives - (i + 1)
                solution.objectives[i] *= sin(solution.variables[aux] * 0.5 * pi)

    def get_name(self):
        return "DTLZ2"


class DTLZ3(FloatProblem):
    """ Problem DTLZ3
    .. note:: Unconstrained problem. The default number of variables and objectives are, respectively, 12 and 3.
    .. note:: Continuous problem having a convex Pareto front
    """

    def __init__(self, number_of_variables: int = 12, number_of_objectives = 3):
        """Constructor
        :param number_of_variables: number of decision variables of the problem
        """
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        g = 0.0
        k = self.number_of_variables - self.number_of_objectives + 1

        for i in range (self.number_of_variables - k, self.number_of_variables):
            g += (solution.variables[i] - 0.5) * (solution.variables[i] - 0.5) - \
                 cos(20.0 * pi * (solution.variables[i] - 0.5))

        g = 100.0 * (k + g)
        for i in range(self.number_of_objectives):
            solution.objectives[i] = 1.0 + g

        for i in range(self.number_of_objectives):
            for j in range(self.number_of_objectives - (i + 1)):
                solution.objectives[i] *= cos(solution.variables[j]) * 0.5 * pi
            if i != 0:
                aux = self.number_of_objectives - (i + 1)
                solution.objectives[i] *= sin(solution.variables[aux] * 0.5 * pi)

    def get_name(self):
        return "DTLZ3"


class DTLZ4(FloatProblem):
    """ Problem DTLZ4
    .. note:: Unconstrained problem. The default number of variables and objectives are, respectively, 12 and 3.
    .. note:: Continuous problem having a convex Pareto front
    """

    def __init__(self, number_of_variables: int = 12, number_of_objectives = 3):
        """Constructor
        :param number_of_variables: number of decision variables of the problem
        """
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        g = 0.0
        k = self.number_of_variables - self.number_of_objectives + 1

        for i in range (self.number_of_variables - k, self.number_of_variables):
            g += (solution.variables[i] - 0.5) * (solution.variables[i] - 0.5)

        for i in range(self.number_of_objectives):
            solution.objectives[i] = 1.0 + g

        alpha = 100.0
        for i in range(self.number_of_objectives):
            for j in range(self.number_of_objectives - (i + 1)):
                solution.objectives[i] *= cos(pow(solution.variables[j], alpha) * (pi / 2.0))
            if i != 0:
                aux = self.number_of_objectives - (i + 1)
                solution.objectives[i] *= sin(solution.variables[aux] * (pi / 2.0))

    def get_name(self):
        return "DTLZ4"


class DTLZ5(FloatProblem):
    """ Problem DTLZ5
    .. note:: Unconstrained problem. The default number of variables and objectives are, respectively, 12 and 3.
    .. note:: Continuous problem having a convex Pareto front
    """

    def __init__(self, number_of_variables: int = 12, number_of_objectives = 3):
        """Constructor
        :param number_of_variables: number of decision variables of the problem
        """
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        g = 0.0
        k = self.number_of_variables - self.number_of_objectives + 1

        for i in range (self.number_of_variables - k, self.number_of_variables):
            g += (solution.variables[i] - 0.5) * (solution.variables[i] - 0.5)

        t = pi /(4.0 * (1.0 + g))
        theta = [] * (self.number_of_objectives - 1)
        theta[0] = solution.variables[0] * pi / 2.0

        for i in range(self.number_of_objectives - 1):
            theta[i] = t * (1.0 + 2.0 * g * solution.objectives[i])

        for i in range(self.number_of_objectives):
            solution.objectives[i] = 1.0 + g

        for i in range(self.number_of_objectives):
            for j in range(self.number_of_objectives - (i + 1)):
                solution.objectives[i] *= cos(theta[j])
            if i != 0:
                aux = self.number_of_objectives - (i + 1)
                solution.objectives[i] *= sin(theta[aux])

    def get_name(self):
        return "DTLZ5"


class DTLZ6(FloatProblem):
    """ Problem DTLZ6
    .. note:: Unconstrained problem. The default number of variables and objectives are, respectively, 12 and 3.
    .. note:: Continuous problem having a convex Pareto front
    """

    def __init__(self, number_of_variables: int = 12, number_of_objectives = 3):
        """Constructor
        :param number_of_variables: number of decision variables of the problem
        """
        self.number_of_variables = number_of_variables
        self.number_of_objectives = number_of_objectives
        self.number_of_constraints = 0

        self.lower_bound = self.number_of_variables * [0.0]
        self.upper_bound = self.number_of_variables * [1.0]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        g = 0.0
        k = self.number_of_variables - self.number_of_objectives + 1

        for i in range (self.number_of_variables - k, self.number_of_variables):
            g += pow(solution.variables[i], 0.1)

        t = pi /(4.0 * (1.0 + g))
        theta = [] * (self.number_of_objectives - 1)
        theta[0] = solution.variables[0] * pi / 2.0

        for i in range(self.number_of_objectives - 1):
            theta[i] = t * (1.0 + 2.0 * g * solution.objectives[i])

        for i in range(self.number_of_objectives):
            solution.objectives[i] = 1.0 + g

        for i in range(self.number_of_objectives):
            for j in range(self.number_of_objectives - (i + 1)):
                solution.objectives[i] *= cos(theta[j])
            if i != 0:
                aux = self.number_of_objectives - (i + 1)
                solution.objectives[i] *= sin(theta[aux])

    def get_name(self):
        return "DTLZ6"