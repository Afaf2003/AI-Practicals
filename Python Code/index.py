def water_jug_problem(x,y,z):
    stack = []
    visited = set()
    stack.append((0,0))

    while len(stack) > 0:
        currentstate = stack.pop()
        if currentstate in visited:
            continue
        visited.add(currentstate)
        if z in currentstate:
            print(visited)
            print(currentstate)
            break
        xstate, ystate = currentstate
        stack.append((x,xstate))
        stack.append((ystate,y))
        stack.append(())





