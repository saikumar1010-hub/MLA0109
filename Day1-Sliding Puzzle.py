import heapq

# Goal state
goal_state = "123456780"   # 0 represents the blank tile

# Find Manhattan Distance (heuristic)
def manhattan(state):
    distance = 0
    for i, value in enumerate(state):
        if value != "0":
            target = int(value) - 1
            distance += abs(i // 3 - target // 3) + abs(i % 3 - target % 3)
    return distance

# Get next possible states by sliding the blank tile
def get_neighbors(state):
    neighbors = []
    zero = state.index("0")   # find blank

    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

    for move in moves[zero]:
        lst = list(state)
        lst[zero], lst[move] = lst[move], lst[zero]
        neighbors.append("".join(lst))

    return neighbors

# A* Search
def solve_puzzle(start_state):
    pq = []
    heapq.heappush(pq, (manhattan(start_state), 0, start_state, []))
    visited = set()

    while pq:
        est, cost, state, path = heapq.heappop(pq)

        if state == goal_state:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for nxt in get_neighbors(state):
            if nxt not in visited:
                heapq.heappush(
                    pq,
                    (cost + 1 + manhattan(nxt), cost + 1, nxt, path + [state])
                )

    return None


# Example Start State (change it as you want)
start = "724506831"

solution = solve_puzzle(start)

print("\nSliding Puzzle Solution:\n")
if solution:
    step_no = 0
    for state in solution:
        print(f"Step {step_no}:")
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
        step_no += 1
else:
    print("No solution exists for this puzzle.")

