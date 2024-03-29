from collections import deque 

class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)

class Vertix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertix, weight=0):
        self.weight = weight
        self.vertix = vertix

class Graph:

    def __init__(self):
        self.__adj_list = {}
      
    def add_vertix(self,value):
      vertix = Vertix(value)
      self.__adj_list[vertix] = []
      return vertix

    def add_edge(self, start_vertix, end_vertix, weight=0):
        if start_vertix not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertix not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertix, weight)
        edge2 = Edge(start_vertix, weight)
        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)

    def get_vertices(self):
      return self.__adj_list.keys()
    
    def size(self):
      return len(self.__adj_list)
  
    def get_neighbors(self,vertix):
      return self.__adj_list.get(vertix, [])
  
    def breadth_first(self,start_vertix):
        result = []
        visted = set()
        q = Queue()
        q.enqueue(start_vertix)
        visted.add(start_vertix)
        while len(q):
            current_vertix = q.dequeue()
            result.append(current_vertix.value)
            neighbors = self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)
        return result
    
    def depth_first(self, start_vertex):
        result = []
        visited = set()
        stack = [start_vertex]
        visited.add(start_vertex)

        while len(stack):
            current_vertex = stack.pop()
            result.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)

            for edge in reversed(neighbors):
                neighbor = edge.vertix
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        return result

def business_trip(graph,cities):
    '''
    args: graph, array
    returns cost if trip is possible
    '''
    start_city = cities.pop(0)
    vertixes  = graph.get_vertices()
    start_vertix = None
    
    for vertex in vertixes:
        if vertex.value == start_city:
            start_vertix = vertex
    
    total_cost = 0
    current_vertix = start_vertix

    while cities:
        next_city = cities.pop(0)
        neighbors = graph.get_neighbors(current_vertix)
        check = False

        for neighbor in neighbors:
            
            if neighbor.vertix.value == next_city:
                check = True
                total_cost += neighbor.weight
                current_vertix = neighbor.vertix

        if not check:
            return None
        # if next_city != current_vertix.value:
        #     return "False"
    

    return total_cost

if __name__ == "__main__":
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
    
    # Pandora = g.add_vertix('Pandora')
    # Metroville = g.add_vertix('Metroville')
    # Arendelle = g.add_vertix('Arendelle')
    # Naboo = g.add_vertix('Naboo')
    # Monstropolis = g.add_vertix('Monstropolis')
    # Narnia = g.add_vertix('Narnia')
    
    # g.add_edge(Metroville,Pandora,82)
    # g.add_edge(Metroville,Arendelle,99)
    # g.add_edge(Metroville,Narnia,37)
    # g.add_edge(Metroville,Naboo,26)
    # g.add_edge(Metroville,Monstropolis,105)
    # g.add_edge(Pandora,Arendelle,150)
    # g.add_edge(Arendelle,Monstropolis,42)
    # g.add_edge(Naboo,Monstropolis,73)
    # g.add_edge(Narnia,Naboo,250)
    
    
    # print(g.breadth_first(Pandora))
    
    # print(g.breadth_first(Pandora))
    print(graph.depth_first(a))
    # print(graph.breadth_first(a))

    # print(business_trip(g,["Narnia", "Arendelle", "Naboo"]))
    # print(business_trip(g,["Narnia", "Arendelle", "Naboo"]))

    
    
