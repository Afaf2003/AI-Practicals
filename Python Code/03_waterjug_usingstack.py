class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None


def dfs(x, y, target):
    stack = []
    visited = set()
    start = Node(0, 0)
    stack.append(start)

    while stack:
        curr = stack.pop()

        if (curr.x == target and curr.y==0) or (curr.y == target and curr.x==0):
            visited.add((curr.x, curr.y))
            return curr

        if (curr.x, curr.y) in visited or (curr.x, curr,y) in stack:
            continue

        visited.add((curr.x, curr.y))

        if curr.x < x:
            nxt = Node(x, curr.y)
            nxt.parent = curr
            stack.append(nxt)

        if curr.x > 0:
            nxt = Node(0, curr.y)
            nxt.parent = curr
            stack.append(nxt)

        if curr.y < y:
            nxt = Node(curr.x, y)
            nxt.parent = curr
            stack.append(nxt)

        if curr.y > 0:
            nxt = Node(curr.x, 0)
            nxt.parent = curr
            stack.append(nxt)


        if curr.x + curr.y >= y and curr.x > 0:
            nxt = Node(curr.x - (y - curr.y), y)
            nxt.parent = curr
            stack.append(nxt)

        if curr.x + curr.y <= y and curr.x > 0:
            nxt = Node(0, curr.x + curr.y)
            nxt.parent = curr
            stack.append(nxt)

        if curr.x + curr.y <= x and curr.y > 0:
            nxt = Node(curr.x + curr.y, 0)
            nxt.parent = curr
            stack.append(nxt)

        if curr.x + curr.y >= x and curr.y > 0:
            nxt = Node(x, curr.x - (x - curr.y))
            nxt.parent = curr
            stack.append(nxt)

    return None



x = 5
y = 3
target = 1
result = dfs(x, y, target)

if result is None:
    print("No solution found")
else:

    path = []
    while result is not None:
        path.append((result.x, result.y))
        result = result.parent
    path.reverse()

    print("Solution found: ")
    print(path)
