
def kahn_sort():
  """
  [Pseducode](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm):

  L ← Empty list that will contain the sorted elements
  S ← Set of all nodes with no incoming edge

  while S is not empty do
      remove a node n from S
      add n to L
      for each node m with an edge e from n to m do
          remove edge e from the graph
          if m has no other incoming edges then
              insert m into S

  if graph has edges then
      return error   (graph has at least one cycle)
  else 
      return L   (a topologically sorted order)
  """
  pass

def dfs_sort():
  """
  [Pseducode](https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search):

  L ← Empty list that will contain the sorted nodes
  while exists nodes without a permanent mark do
      select an unmarked node n
      visit(n)

  function visit(node n)
      if n has a permanent mark then
          return
      if n has a temporary mark then
          stop   (not a DAG)

      mark n with a temporary mark

      for each node m with an edge from n to m do
          visit(m)

      remove temporary mark from n
      mark n with a permanent mark
      add n to head of L
  """
  pass