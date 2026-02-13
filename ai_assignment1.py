# used AI to come up with the code and to determine which data values to use for what

# 0 = open path
# 1 = wall
maze = [
  [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
]

# start and end points of the maze
start = (0, 0)
goal = (9, 9)

rows = len(maze)
cols = len(maze[0])

# Possible moves: right, down, left, up
# Preference of the order of movement: right, down, left, up
    # However because the code utilizes a stack it is handled in the opposite order which means: up, left, down, right
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(position, visited):
    r, c = position

    # Check boundaries
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    # Check wall
    if maze[r][c] != 0:
        return False

    # Check visited
    if position in visited:
        return False

    return True


def dfs(start, goal):
    stack = [start]          # DFS stack
    visited = set()          # Visited states
    parent = {}              # To reconstruct path

    while stack:
        current = stack.pop()

        # upon reaching the goal, returns the path it used to get there
        if current == goal:
            return reconstruct_path(parent, start, goal)

        # marks any newly visited points as having been visited
        if current not in visited:
            visited.add(current)

            # goes through the possible moves
            for move in moves:
                next_pos = (current[0] + move[0], current[1] + move[1])

                # if selected move is valid then it will continue onto the next point
                if is_valid(next_pos, visited):
                    stack.append(next_pos)
                    parent[next_pos] = current

    return None

#after finding the goal this function returns the path it took to get there
def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()
    return path

# runs code
path = dfs(start, goal)

if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")