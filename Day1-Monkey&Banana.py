from collections import deque

# State: (monkey_pos, box_pos, on_box, has_banana)
start_state = ("door", "window", False, False)
goal_state  = ("middle", "middle", True, True)

locations = ["door", "window", "middle"]


def get_next_states(state):
    monkey_pos, box_pos, on_box, has_banana = state
    next_states = []

    if has_banana:
        return next_states

    # Walk
    for loc in locations:
        if loc != monkey_pos:
            next_states.append(((loc, box_pos, False, has_banana),
                                f"Monkey walks from {monkey_pos} to {loc}"))

    # Push Box
    if monkey_pos == box_pos and not on_box:
        for loc in locations:
            if loc != box_pos:
                next_states.append(((loc, loc, False, has_banana),
                                    f"Monkey pushes the box from {box_pos} to {loc}"))

    # Climb box
    if monkey_pos == box_pos and not on_box:
        next_states.append(((monkey_pos, box_pos, True, has_banana),
                            "Monkey climbs onto the box"))

    # Grasp banana
    if on_box and monkey_pos == "middle":
        next_states.append(((monkey_pos, box_pos, True, True),
                            "Monkey grasps the banana"))

    return next_states


def bfs_monkey_banana():
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state, action in get_next_states(state):
            queue.append((next_state, path + [action]))

    return None


solution = bfs_monkey_banana()

print("Monkey & Banana Problem Solution Steps:\n")
for step in solution:
    print("➡", step)
