def bfs():
  """
  [Pseudocode](https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode):

    procedure BFS(G, root) is
      let Q be a queue
      label root as explored
      Q.enqueue(root)
      while Q is not empty do
        v := Q.dequeue()
          if v is the goal then
            return v
          for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as explored then
              label w as explored
              Q.enqueue(w)
  """
  pass


def dfs():
  """
  [Pseudocode](https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode):

    procedure DFS(G, v) is
      label v as discovered
      for all directed edges from v to w that are in G.adjacentEdges(v) do
          if vertex w is not labeled as discovered then
              recursively call DFS(G, w)
  
  """
  pass