from collections import deque
from math import gcd

def is_solvable(jug1_cap, jug2_cap, target):
    return target <= max(jug1_cap, jug2_cap) and target % gcd(jug1_cap, jug2_cap) == 0

def get_next_states(state, jug1_cap, jug2_cap):
    x, y = state
    states = []

    states.append(((jug1_cap, y), "Fill Jug1"))
    states.append(((x, jug2_cap), "Fill Jug2"))
    states.append(((0, y), "Empty Jug1"))
    states.append(((x, 0), "Empty Jug2"))

    pour = min(x, jug2_cap - y)
    states.append(((x - pour, y + pour), f"Pour J1 → J2 ({pour}L)"))

    pour = min(y, jug1_cap - x)
    states.append(((x + pour, y - pour), f"Pour J2 → J1 ({pour}L)"))

    return states

def solve_water_jug(jug1_cap, jug2_cap, target):
    if not is_solvable(jug1_cap, jug2_cap, target):
        return None

    start = (0, 0)
    queue = deque([start])
    parent = {start: (None, None)}
    visited = {start}

    while queue:
        state = queue.popleft()
        x, y = state

        if x == target or y == target:
            path = []
            while state:
                prev, action = parent[state]
                path.append((state, action))
                state = prev
            return list(reversed(path))

        for new_state, action in get_next_states(state, jug1_cap, jug2_cap):
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = (state, action)
                queue.append(new_state)

    return None

def print_table(path):
    print("\nSTEPS TO SOLVE WATER JUG PROBLEM\n")
    print("{:<5} {:<10} {:<10} {}".format("Step", "Jug1", "Jug2", "Action"))
    print("-" * 40)

    for i, (state, action) in enumerate(path):
        x, y = state
        action = action if action else "Start"
        print("{:<5} {:<10} {:<10} {}".format(i, x, y, action))

if __name__ == "__main__":
    jug1 = 4
    jug2 = 3
    target = 2

    path = solve_water_jug(jug1, jug2, target)

    if path:
        print_table(path)
    else:
        print("No solution possible!")

