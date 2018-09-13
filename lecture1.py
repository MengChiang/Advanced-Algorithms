import numpy as np

def GCD(num1, num2):
    times = 0
    while num2 != 0:
        times += 1
        print("indexative {0}: {1}, {2}".format(times, num1, num2))
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    print("GCD = ", num1)
    return num1

def Nearest_Neighbor_Tour(points, start):

    result = []
    cost = 0

    index = 0
    times = 1

    while (times < len(points)):
        index += 1
        if times == 1:
            init_point = points[start]
            result.append(start)

        idx = start+index
        if idx < len(points):
            result.append(idx)
            visit_point = points[idx]

            cost += abs(init_point - visit_point)
            init_point = visit_point
            times += 1

        idx = start-index
        if idx >= 0:
            result.append(idx)
            visit_point = points[idx]

            cost += abs(init_point - visit_point)
            init_point = visit_point
            times += 1

    return (result, cost)

# def Exhaustive(points):
#     n = len(points)

#     return (result, cost)

def getlist(length):
    result_list = []
    


