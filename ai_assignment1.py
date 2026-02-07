# used AI to come up with the code and to determine which data values to use for what

# 0 = open path
# 1 = wall
maze = [
  [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
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
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(position, visited):
    r, c = position

    # Check boundaries
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    # Check wall
    if maze[r][c] == 1:
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

        if current == goal:
            return reconstruct_path(parent, start, goal)

        if current not in visited:
            visited.add(current)

            for move in moves:
                next_pos = (current[0] + move[0], current[1] + move[1])

                if is_valid(next_pos, visited):
                    stack.append(next_pos)
                    parent[next_pos] = current

    return None


def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()
    return path


path = dfs(start, goal)

if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")