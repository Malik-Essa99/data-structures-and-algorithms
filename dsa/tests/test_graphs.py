import pytest 
from collections import deque
from dsa.graph import Graph

def test_add_vertex():
    graph = Graph()
    v1 = graph.add_vertix("A")
    assert v1 in graph.get_vertices()

def test_add_edge():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    graph.add_edge(v1, v2, 5)
    neighbors = graph.get_neighbors(v1)
    assert len(neighbors) == 1
    assert neighbors[0].vertix == v2
    assert neighbors[0].weight == 5

def test_get_vertices():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert v1 in vertices
    assert v2 in vertices

def test_get_neighbors():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    v3 = graph.add_vertix("C")
    graph.add_edge(v1, v2, 5)
    graph.add_edge(v1, v3, 7)
    neighbors = graph.get_neighbors(v1)
    assert len(neighbors) == 2
    assert neighbors[0].vertix == v2
    assert neighbors[0].weight == 5
    assert neighbors[1].vertix == v3
    assert neighbors[1].weight == 7

def test_size():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    assert graph.size() == 2
    v3 = graph.add_vertix("C")
    assert graph.size() == 3

def test_single_vertex_edge():
    graph = Graph()
    v1 = graph.add_vertix("A")
    assert graph.size() == 1
    graph.add_edge(v1, v1)
    neighbors = graph.get_neighbors(v1)
    assert len(neighbors) == 1  
    assert neighbors[0].vertix == v1


######################### buisness trip #########################
#                       still wokring on it                     #
######################### buisness trip #########################