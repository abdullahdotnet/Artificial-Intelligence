class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        return str(self.state)


class solvePuzzle:
    def __init__(self, initialState):
        self.initalState = Node(initialState)
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.possibleMoves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }

    def solve(self):
        if not self.isSolvable(self.initalState.state):
            print("Pizzle cannot be solved")
            return None

        for limit in range(100): 
            result = self.depthLimitedSearch(self.initalState, limit)
            if result:
                return result

        print("No solution found.")
        return None
    
    def isSolvable(self, state):
        inversions = sum(1 for i in range(len(state)) for j in range(i + 1, len(state)) if state[j] and state[i] and state[i] > state[j])
        return inversions % 2 == 0
    
    def depthLimitedSearch(self, node, depth):
        visited = set()
        stack = [node]

        while stack:
            currentNode = stack.pop()
            visited.add(str(currentNode.state))

            if currentNode.state == self.goal_state:
                return self.solution(currentNode)

            if currentNode.depth < depth:
                successors = self.generateSuccessor(currentNode)
                successors = [successor for successor in successors if str(successor) not in visited]
                stack.extend(successors)

    

    def generateSuccessor(self, node):
        successors = []
        index = node.state.index(0)
        for move in self.possibleMoves[index]:
            newState = node.state[:]
            newState[index], newState[move] = newState[move], newState[index]
            successors.append(Node(newState, node, move))
        return successors

    def solution(self, node):
        solution_steps = []
        while node:
            solution_steps.append(node.state)
            node = node.parent
        return solution_steps[::-1]
    

if __name__ == "__main__":
    print("Enter the initial state from 0 to 8")
    initalState = list(map(int, input().split()))
    puzzle_solver = solvePuzzle(initalState)
    result = puzzle_solver.solve()

    if result:
        print("Solution:")
        for state in result:
            print(state,"\n")
