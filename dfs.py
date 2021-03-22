# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:35:31 2021

@author: Amol
"""

graph = {
'1' : ['2','3'],
'2':['4','1'],
'3':['1','4','6','7','8'],
'4':['3','5','6','7'],
'5':['4'],
'6':['3','4','7'],
'7':['3','4','6'],
'8':['2','3','9','10'],
'9':['8'],
'10':['8']
}

visited = []
stack = []


def dfs(graph,s):
    stack.append(s)
    visited.append(s)

    while stack:
        s = stack.pop()
        print(s,end=" ")
        for adjv in graph[s]:
            #print(adjv,end=" ")
            if adjv not in visited:
                #print("in queue",adjv)
                stack.append(adjv)
                visited.append(adjv)


dfs(graph,'1')
