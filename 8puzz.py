import heapq

# Define the goal state
goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

# Define the possible moves
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Helper function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x, y = divmod(i, 3)
            gx, gy = divmod(state[i] - 1, 3)
            distance += abs(x - gx) + abs(y - gy)
    return distance

# A* search algorithm
def solve_puzzle(initial_state):
    open_set = [(manhattan_distance(initial_state), 0, initial_state)]
    closed_set = set()
    
    while open_set:
        _, cost, current_state = heapq.heappop(open_set)
        if current_state == goal_state:
            return cost
        
        if current_state in closed_set:
            continue
        
        closed_set.add(current_state)
        
        # Find the index of the empty tile
        empty_tile_index = current_state.index(0)
        empty_tile_x, empty_tile_y = divmod(empty_tile_index, 3)
        
        for dx, dy in moves:
            new_x, new_y = empty_tile_x + dx, empty_tile_y + dy
            
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_state = list(current_state)
                new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
                new_state = tuple(new_state)
                
                if new_state not in closed_set:
                    heapq.heappush(open_set, (cost + 1 + manhattan_distance(new_state), cost + 1, new_state))

    return -1  # No solution found

# Example usage:
initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
steps = solve_puzzle(initial_state)

if steps >= 0:
    print(f"Minimum number of steps to solve the puzzle: {steps}")
else:
    print("No solution found.")
