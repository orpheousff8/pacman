# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  start = problem.getStartState()
  stack = util.Stack()
  visited = []
  parentMap = {}


  if problem.isGoalState(problem.getStartState()):
    curr = (problem.getStartState(), None)
  else:
    stack.push(start)

  while not stack.isEmpty():
    parent = stack.pop()
    if parent in visited:
      continue
    if problem.isGoalState(parent):
      curr = (parent, None)
      break #solution found no need further search
    visited.append(parent)
    children = problem.getSuccessors(parent)
    for child in children:
      stack.push(child[0])
      if not parentMap.has_key(child[0]):
        parentMap[child[0]] = (parent, child[1])

  action = util.Stack()
  while (curr[0] != None):
    #print curr
    action.push(curr[1])
    if curr[0] == problem.getStartState():
      break
    curr = parentMap[curr[0]]

  instruction = []
  from game import Directions
  while not action.isEmpty():
    a = action.pop()
    if a == "North":
      instruction.append(Directions.NORTH)
    elif a == "South":
      instruction.append(Directions.SOUTH)
    elif a == "East":
      instruction.append(Directions.EAST)
    elif a == "West":
      instruction.append(Directions.WEST)
  
  return instruction

  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  start = problem.getStartState()
  queue = util.Queue()
  visited = []
  parentMap = {}


  if problem.isGoalState(problem.getStartState()):
    curr = (problem.getStartState(), None)
  else:
    queue.push(start)

  while not queue.isEmpty():
    parent = queue.pop()
    if parent in visited:
      continue
    if problem.isGoalState(parent):
      curr = (parent, None)
      break #solution found with minimum hop no need further search
    visited.append(parent)
    children = problem.getSuccessors(parent)
    for child in children:
      queue.push(child[0])
      if not parentMap.has_key(child[0]):
        parentMap[child[0]] = (parent, child[1])

  action = util.Stack()
  while (curr[0] != None):
    action.push(curr[1])
    if curr[0] == problem.getStartState():
      break
    curr = parentMap[curr[0]]

  instruction = []
  from game import Directions
  while not action.isEmpty():
    a = action.pop()
    if a == "North":
      instruction.append(Directions.NORTH)
    elif a == "South":
      instruction.append(Directions.SOUTH)
    elif a == "East":
      instruction.append(Directions.EAST)
    elif a == "West":
      instruction.append(Directions.WEST)

  return instruction
  #util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  start = problem.getStartState()
  PrioQueue = util.PriorityQueue()
  visited = []
  parentMap = {}

  if problem.isGoalState(problem.getStartState()):
    curr = (problem.getStartState(), None)
  else:
    PrioQueue.push(start, 0)

  while not PrioQueue.isEmpty():
    parent = PrioQueue.pop()
    if parent in visited:
      continue
    if problem.isGoalState(parent):
      curr = (parent, None)
      #no break as we want the minimum cost
    visited.append(parent)
    children = problem.getSuccessors(parent)
    for child in children:
      #manhattanDistance is a aprroxed summ of distance.
      PrioQueue.push(child[0], util.manhattanDistance(problem.getStartState(), child[0]))
      if not parentMap.has_key(child[0]):
        parentMap[child[0]] = (parent, child[1])

  action = util.Stack()
  while (curr[0] != None):
    action.push(curr[1])
    if curr[0] == problem.getStartState():
      break
    curr = parentMap[curr[0]]

  instruction = []
  from game import Directions
  while not action.isEmpty():
    a = action.pop()
    if a == "North":
      instruction.append(Directions.NORTH)
    elif a == "South":
      instruction.append(Directions.SOUTH)
    elif a == "East":
      instruction.append(Directions.EAST)
    elif a == "West":
      instruction.append(Directions.WEST)

  return instruction
  #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  start = problem.getStartState()
  prioQueue = util.PriorityQueue()
  visited = []
  parentMap = {}

  if problem.isGoalState(problem.getStartState()):
    curr = (problem.getStartState(), None)
  else:
      prioQueue.push(start, 0)

  while not prioQueue.isEmpty():
    parent = prioQueue.pop()
    if parent in visited:
      continue
    if problem.isGoalState(parent):
      curr = (parent, None)
      #no break
    visited.append(parent)
    children = problem.getSuccessors(parent)
    for child in children:
      prioQueue.push(child[0], util.manhattanDistance(problem.getStartState(), child[0])
                     + util.manhattanDistance(child[0], (1, 1)))
      if not parentMap.has_key(child[0]):
        parentMap[child[0]] = (parent, child[1])

  action = util.Stack()
  while (curr[0] != None):
    action.push(curr[1])
    if curr[0] == problem.getStartState():
      break
    curr = parentMap[curr[0]]

  instruction = []
  from game import Directions
  while not action.isEmpty():
    a = action.pop()
    if a == "North":
      instruction.append(Directions.NORTH)
    elif a == "South":
      instruction.append(Directions.SOUTH)
    elif a == "East":
      instruction.append(Directions.EAST)
    elif a == "West":
      instruction.append(Directions.WEST)

  return instruction
  #util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
