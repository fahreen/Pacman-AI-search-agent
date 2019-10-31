# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


# node class created to represent nodes
class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_path_cost(self):
        return self.path_cost


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    "*** YOUR CODE HERE ***"
    # create initial node, with statrt state
    # create Node(state, parent, action, path_cost)
    node = Node(problem.getStartState(), None, [], 0)
    # use stack as frontier/fringe
    frontier = util.Stack()
    # push initial node onto stack
    frontier.push(node)
    # explored will keep track nodes that have been explored
    explored = set()
    while True:
        # if no candidates for expansion, return failure
        if frontier.isEmpty():
            return None
        # choose leaf node for expansion (top of stack) and add it to explored
        node = frontier.pop()
        # check if node to be exapanded is in goal state
        if problem.isGoalState(node.get_state()):
            return node.get_action()
        # skip expansion if this node has already been explored
        if node.get_state() not in explored:
            explored.add(node.get_state())
            children = problem.getSuccessors(node.get_state())
            # Expand node, pushing all the children onto the frontier
            for element in children:
                a = node.get_action()
                b = [element[1]]
                child = Node(element[0], node, a + b, element[2])
                frontier.push(child)
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # create initial node, with statrt state
    # create Node(state, parent, action, path_cost )
    node = Node(problem.getStartState(), None, [], 0)
    # use queue as frontier/fringe
    frontier = util.Queue()
    frontier.push(node)
    explored = set()
    while True:
        # if no candidates for expansion, return failure
        if frontier.isEmpty():
            return None
        # choose leaf node for expansion (top of stack) and add it to explored
        node = frontier.pop()
        if problem.isGoalState(node.get_state()):
            return node.get_action()
        if node.get_state() not in explored:
            explored.add(node.get_state())
            children = problem.getSuccessors(node.get_state())
            for element in children:
                a = node.get_action()
                b = [element[1]]
                child = Node(element[0], node, a + b, element[2])
                frontier.push(child)
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # create Node(state, parent, action, path_cost )
    node = Node(problem.getStartState(), None, [], 0)
    # use priority queue as frontier/fringe
    frontier = util.PriorityQueue()
    # priority of initial node should be zero
    frontier.push(node, 0)
    explored = set()
    while True:
        # if no candidates for expansion, return failiure
        if frontier.isEmpty():
            return None
        # choose leaf node for expansion (top of stack) and add it to explored
        node = frontier.pop()
        if problem.isGoalState(node.get_state()):
            return node.get_action()
        if node.get_state() not in explored:
            explored.add(node.get_state())
            children = problem.getSuccessors(node.get_state())
            for element in children:
                a = node.get_action()
                b = [element[1]]
                fullPath = a + b
                childCost = element[2]
                fullCost = childCost + node.get_path_cost()
                # use path_cost as priority for priority queue
                child = Node(element[0], node, fullPath, fullCost)
                frontier.push(child, fullCost)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node of least total cost first."""
    # create Node(state, parent, action, path_cost )
    node = Node(problem.getStartState(), None, [], 0)
    # use priority queue as frontier/fringe
    frontier = util.PriorityQueue()
    # priority of initial node should be zero
    frontier.push(node, 0)
    explored = set()
    while True:
        # if no candidates for expansion, return failiure
        if frontier.isEmpty():
            return None
        # choose leaf node for expansion (top of stack) and add it to explored
        node = frontier.pop()
        if problem.isGoalState(node.get_state()):
            return node.get_action()

        if node.get_state() not in explored:
            explored.add(node.get_state())
            children = problem.getSuccessors(node.get_state())
            for element in children:
                a = node.get_action()
                b = [element[1]]
                fullPath = a + b
                childCost = element[2]
                fullCost = childCost + node.get_path_cost()
                # use path_cost + heuristic as priority for priority queue
                child = Node(element[0], node, fullPath, fullCost)
                frontier.push(child, (heuristic(child.get_state(), problem) + fullCost))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
