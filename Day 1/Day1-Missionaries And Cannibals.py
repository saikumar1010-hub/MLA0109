from collections import deque

# Validate a state (no missionaries eaten)
def is_valid(M_left, C_left, M_right, C_right):
    # No negative values
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False

    # Left side unsafe
    if M_left > 0 and C_left > M_left:
        return False

    # Right side unsafe
    if M_right > 0 and C_right > M_right:
        return False

    return True


# Generate next possible states
def get_next_states(state):
    M_left, C_left, boat, M_right, C_right = state

    moves = [
        (1, 0),   # 1 missionary
        (2, 0),   # 2 missionaries
        (0, 1),   # 1 cannibal
        (0, 2),   # 2 cannibals
        (1, 1)    # 1 missionary + 1 cannibal
    ]

    next_states = []

    if boat == "left":
        # Move from LEFT → RIGHT
        for m, c in moves:
            new_state = (
                M_left - m,
                C_left - c,
                "right",
                M_right + m,
                C_right + c
            )

            if is_valid(new_state[0], new_state[1], new_state[3], new_state[4]):
                action = f"Boat takes {m} Missionary(s) & {c} Cannibal(s) from LEFT → RIGHT"
                next_states.append((new_state, action))

    else:
        # Move from RIGHT → LEFT
        for m, c in moves:
            new_state = (
                M_left + m,
                C_left + c,
                "left",
                M_right - m,
                C_right - c
            )

            if is_valid(new_state[0], new_state[1], new_state[3], new_state[4]):
                action = f"Boat takes {m} Missionary(s) & {c} Cannibal(s) from RIGHT → LEFT"
                next_states.append((new_state, action))

    return next_states


# BFS Search
def solve():
    start = (3, 3, "left", 0, 0)
    goal = (0, 0, "right", 3, 3)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state, action in get_next_states(state):
            queue.append((next_state, path + [action]))

    return None


# Run solution
solution = solve()

print("\nMissionaries & Cannibals Solution:\n")
for step in solution:
    print("➡", step)
