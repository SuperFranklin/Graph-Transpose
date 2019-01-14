'''
Created on Jan 14, 2019

@author: franek
'''

graph = {0: set([1, 7]),
         1: set([0, 2, 3]),
         2: set([4]),
         3: set([2]),
         4: set([3]),
         5: set([3]),
         6: set([7]),
         7: set([])}


def transpose(graph):
    result = dict()
    for v in graph.keys():
        for child in graph[v]:
            if child in result.keys():
                result[child].add(v)
            else:
                result[child] = {v}   
    return result


print( transpose(graph) )