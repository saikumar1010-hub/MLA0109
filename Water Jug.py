from collections import deque

# State is (x, y) where:
# x = amount in Jug1
# y = amount in Jug2

def water_jug(jug1, jug2, target):

    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        # If solution reached
        if x == target or y == target:
            return path + [(x, y)]

        if (x, y) in visited:
            continue

        visited.add((x, y))

        next_states = []

        # 1. Fill Jug1
        next_states.append(((jug1, y), "Fill Jug1"))

        # 2. Fill Jug2
        next_states.append(((x, jug2), "Fill Jug2"))

        # 3. Empty Jug1
        next_states.append(((0, y), "Empty Jug1"))

        # 4. Empty Jug2
        next_states.append(((x, 0), "Empty Jug2"))

        # 5. Pour Jug1 -> Jug2
        transfer = min(x, jug2 - y)
        next_states.append(((x - transfer, y + transfer), "Pour Jug1 → Jug2"))

        # 6. Pour Jug2 -> Jug1
        transfer = min(y, jug1 - x)
        next_states.append(((x + transfer, y - transfer), "Pour Jug2 → Jug1"))

        # Explore all next states
        for (nx, ny), action in next_states:
            queue.append(((nx, ny), path + [(x, y, action)]))

    return None


# Run the program
jug1 = 4
jug2 = 3
target = 2

solution = water_jug(jug1, jug2, target)

print("\nWater Jug Problem Solution:\n")
if solution:
    for step in solution:
        if len(step) == 3:
            print(f"At ({step[0]}, {step[1]}) -> {step[2]}")
        else:
            print(f"Reached target: {step}")
else:
    print("No solution found.")
