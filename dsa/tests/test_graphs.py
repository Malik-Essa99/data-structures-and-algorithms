import pytest 
from collections import deque
from dsa.graph import Graph,business_trip

@pytest.mark.skip(reason="Done")
def test_add_vertex():
    graph = Graph()
    v1 = graph.add_vertix("A")
    assert v1 in graph.get_vertices()
@pytest.mark.skip(reason="Done")
def test_add_edge():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    graph.add_edge(v1, v2, 5)
    neighbors = graph.get_neighbors(v1)
    assert len(neighbors) == 1
    assert neighbors[0].vertix == v2
    assert neighbors[0].weight == 5
    
@pytest.mark.skip(reason="Done")
def test_get_vertices():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert v1 in vertices
    assert v2 in vertices

@pytest.mark.skip(reason="Done")
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
    
@pytest.mark.skip(reason="Done")
def test_size():
    graph = Graph()
    v1 = graph.add_vertix("A")
    v2 = graph.add_vertix("B")
    assert graph.size() == 2
    v3 = graph.add_vertix("C")
    assert graph.size() == 3

@pytest.mark.skip(reason="Done")
def test_single_vertex_edge():
    graph = Graph()
    v1 = graph.add_vertix("A")
    assert graph.size() == 1
    graph.add_edge(v1, v1)
    neighbors = graph.get_neighbors(v1)
    assert len(neighbors) == 2 
    assert neighbors[0].vertix == v1


######################### buisness trip #########################

@pytest.mark.skip(reason="Done")
def test_cases():
    g = Graph()
    Pandora = g.add_vertix('Pandora')
    Metroville = g.add_vertix('Metroville')
    Arendelle = g.add_vertix('Arendelle')
    Naboo = g.add_vertix('Naboo')
    Monstropolis = g.add_vertix('Monstropolis')
    Narnia = g.add_vertix('Narnia')
    
    g.add_edge(Metroville,Pandora,82)
    g.add_edge(Metroville,Arendelle,99)
    g.add_edge(Metroville,Narnia,37)
    g.add_edge(Metroville,Naboo,26)
    g.add_edge(Metroville,Monstropolis,105)
    g.add_edge(Pandora,Arendelle,150)
    g.add_edge(Arendelle,Monstropolis,42)
    g.add_edge(Naboo,Monstropolis,73)
    g.add_edge(Narnia,Naboo,250)
    
    assert business_trip(g,["Metroville", "Pandora"]) == 82
    assert business_trip(g,["Arendelle","Monstropolis", "Naboo"]) == 115
    assert business_trip(g,["Naboo", "Pandora"]) == None
    assert business_trip(g,["Narnia", "Arendelle", "Naboo"]) == None
    
def test_depth_first_traversal():
    graph = Graph()
    a = graph.add_vertix('A')
    b = graph.add_vertix('B')
    e = graph.add_vertix('E')
    c = graph.add_vertix('C')
    d = graph.add_vertix('D')
    e = graph.add_vertix('E')
    f = graph.add_vertix('F')
    g = graph.add_vertix('G')
    h = graph.add_vertix('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,d)
    graph.add_edge(b,c)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(f,h)
    graph.add_edge(c,g)
    
    assert graph.depth_first(a) == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']