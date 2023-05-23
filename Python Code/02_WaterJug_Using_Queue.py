from queue import Queue


def water_jug_problem(x, y, z):

    visited = set()
    q = Queue()

    q.put((0, 0))

    while not q.empty():

        curr_state = q.get()

        if curr_state in visited:
            continue
        a, b = curr_state
        if (a == z and b == 0) or (a == 0 and b == z):
            print(visited)
            print(curr_state)
            break

        visited.add(curr_state)

        x_state, y_state = curr_state

        q.put((x, y_state))

        q.put((x_state, y))

        q.put((0, y_state))

        q.put((x_state, 0))

        q.put((max(0, x_state - (y - y_state)), min(y, y_state + x_state)))

        q.put((min(x, x_state + y_state), max(0, y_state - (x - x_state))))


water_jug_problem(5, 3, 1)
