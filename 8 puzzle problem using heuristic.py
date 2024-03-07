import heapq
import copy

def isValid(x,y):
    return 0 <= x < 3 and 0 <= y < 3
 
def findSpace(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j

def getChildren(state):
    children=[]
    for dy,dx in [(0,-1),(0,1),(-1,0),(1,0)] :
        x,y = findSpace(state)
        new_x,new_y = x+dx,y+dy
        if isValid(new_x,new_y):
            new_state = copy.deepcopy(state)
            new_state[x][y],new_state[new_x][new_y] = new_state[new_x][new_y],new_state[x][y]
            children.append(new_state)
    return children
     


def heuristic(current):
    cost = 0
    for i in range(3):
        for j in range(3):
            if current[i][j] != 0 and current[i][j] != goal_state[i][j]:
                cost+=1
    return cost

def printPath(path):
    for row in path:
        print(" ".join(map(str,row)))
    print()

def solve(initial_state,goal_state):
    visited = set()
    queue = [(heuristic(initial_state), initial_state,[])]

    while queue:
        _,current_state,path = heapq.heappop(queue)
        
        if current_state == goal_state:
            for i, steps in enumerate(path):
                print(f"Step {i+1}:")
                printPath(steps)
            return True
        visited.add(tuple(map(tuple,current_state)))
        for children in getChildren(current_state):
            if tuple(map(tuple,children)) not in visited:
                h = heuristic(children)
                heapq.heappush(queue,(h,children,path+[children]))

    print ('Solution Not found')
    return False


if __name__ == '__main__':
    initial_state = [
        [4, 1, 3],
        [7, 2, 5],
        [0, 8, 6]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solve(initial_state,goal_state)