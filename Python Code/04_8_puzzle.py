goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]


def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                misplaced =misplaced+ 1
    return misplaced


def simple_search(initial_state):
    frontier = [(heuristic(initial_state), initial_state)]
    explored = set()
    parents = {str(initial_state): None}

    while frontier:

        frontier.sort()
        current_state = frontier.pop(0)[1]
        explored.add(str(current_state))

        if current_state == goal_state:

            path = [current_state]
            while parents[str(current_state)] is not None:
                current_state = parents[str(current_state)]
                path.append(current_state)
            return path[::-1]

        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    x, y = i, j

        next_states = []
        if x > 0:
            next_states.append((x-1, y))
        if x < 2:
            next_states.append((x+1, y))
        if y > 0:
            next_states.append((x, y-1))
        if y < 2:
            next_states.append((x, y+1))

        for state in next_states:
            new_state = [row[:] for row in current_state]
            i, j = state
            new_state[x][y], new_state[i][j] = new_state[i][j], new_state[x][y]

            if str(new_state) not in explored:
                frontier.append((heuristic(new_state), new_state))
                parents[str(new_state)] = current_state

    return None


initial_state = [[1, 2, 3], [8, 6, 0], [7, 5, 4]]


solution = simple_search(initial_state)


if solution is not None:
    print("Steps to reach the goal state:")
    for i, state in enumerate(solution):
        print("Step", i+1, ":")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
