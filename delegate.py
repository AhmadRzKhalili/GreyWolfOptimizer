"""
as the duty of implementor:
    1) prepare your code in initialize method.
    2) cleanup after your code in terminate method.
    3) replace entry point of your algorithm in native_process method
    4) you must return a 1D array which is your proposed sequence of nodes for traveling through and an integer as
       total path cost of proposed path (permutation).

    exp:
        input :
            np.array([
                [0, 5, 4, 10],
                [5, 0, 8, 5],
                [4, 8, 0, 3],
                [10, 5, 3, 0]
            ])

        output:
            ([0, 1, 3, 2] , 17)

    *** input of your code will be a 2D numpy array where each index represents edge connecting nodes i and j.
    *** if two nodes do not have a edge connecting them directly, corresponding index will be set to -1.
"""
# from .exact.dynamic_programming import solve_tsp_dynamic_programming
from .optimizer import GW_Optimizer
from .Graph import Graph

def native_id():
    # return your project name, team name or some unique id
    return "Grey Wolf"


def initialize():
    # setup initialization code in here
    # this method is called only once at the beginning benchmark
    return


def terminate():
    # setup cleanup code in here
    # this method is called only once at the end of benchmark
    return


def convert_input(raw_input):
    return raw_input


def convert_output(native_output):
    native_output = (list(native_output[0]), native_output[1])
    return native_output


def native_process(data):
    
    graph = Graph(data)
    
    max_itter = int(input("Maximum number of itterations: "))
    wolf_num = int(input("Number of wolves: "))
    optimizer = GW_Optimizer(graph, max_itter, wolf_num)
    # optimizer = GW_Optimizer(graph, 50, 100)

    output = convert_output(optimizer.optimize())

    return output
