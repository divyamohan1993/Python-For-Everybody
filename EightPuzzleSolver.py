class EightPuzzleSolver:
    def __init__(self, initial_state):
        # Store the initial state of the puzzle
        self.initial_state = initial_state
        
        # The goal state represents the solved 8-puzzle configuration
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, ' ']]
        
        # Determine the position of the blank space (' ') in the initial state
        self.blank_position = self.find_blank_space(initial_state)

    def find_blank_space(self, current_state):
        # Iterate over the 3x3 grid to locate the blank space
        for row in range(3):
            for col in range(3):
                if current_state[row][col] == ' ':
                    # Return the (row, col) of the blank space
                    return row, col

    def is_goal_state(self, current_state):
        # Check if the current state matches the goal state
        return current_state == self.goal_state

    def get_possible_moves(self, blank_position):
        # List of valid moves for the blank space (up, down, left, right)
        possible_moves = []
        row, col = blank_position

        # Check if moving the blank space up is possible
        if row > 0: 
            possible_moves.append((-1, 0))  # Move blank space up
        
        # Check if moving the blank space down is possible
        if row < 2: 
            possible_moves.append((1, 0))   # Move blank space down
        
        # Check if moving the blank space left is possible
        if col > 0: 
            possible_moves.append((0, -1))  # Move blank space left
        
        # Check if moving the blank space right is possible
        if col < 2: 
            possible_moves.append((0, 1))   # Move blank space right

        # Return the list of possible moves
        return possible_moves

    def apply_move(self, current_state, move, blank_position):
        # Unpack the blank space's current position
        row, col = blank_position
        
        # Calculate new position of the blank space after applying the move
        new_row, new_col = row + move[0], col + move[1]

        # Create a deep copy of the current state to apply the move
        new_state = [row[:] for row in current_state]
        
        # Swap the blank space with the adjacent tile in the direction of the move
        new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
        
        # Return the new state of the puzzle and the updated blank space position
        return new_state, (new_row, new_col)

    def solve(self):
        # Use a queue to explore states (BFS approach) and track moves
        from collections import deque
        state_queue = deque([(self.initial_state, self.blank_position, [])])
        
        # Set to keep track of visited states to avoid revisiting
        visited_states = set()

        # Continue exploring while there are states in the queue
        while state_queue:
            # Dequeue the front element (current state, blank position, moves)
            current_state, blank_position, move_sequence = state_queue.popleft()

            # Check if the current state is the goal state
            if self.is_goal_state(current_state):
                return move_sequence  # Return the sequence of moves that solve the puzzle

            # Mark the current state as visited by converting the list to tuple
            visited_states.add(tuple(map(tuple, current_state)))

            # Explore all possible moves for the blank space
            for move in self.get_possible_moves(blank_position):
                # Apply the move and get the new state and blank space position
                new_state, new_blank_position = self.apply_move(current_state, move, blank_position)

                # If the new state hasn't been visited, add it to the queue
                if tuple(map(tuple, new_state)) not in visited_states:
                    state_queue.append((new_state, new_blank_position, move_sequence + [move]))

        # If no solution was found, return None
        return None

# Define the initial configuration of the 8-puzzle
initial_configuration = [
    [1, 2, 3],
    [4, ' ', 6],
    [7, 5, 8]
]

# Create an instance of the EightPuzzleSolver with the initial configuration
puzzle_solver = EightPuzzleSolver(initial_configuration)

# Attempt to solve the puzzle and retrieve the sequence of moves, if any
solution_moves = puzzle_solver.solve()

# Print the solution if it exists, otherwise inform that no solution was found
if solution_moves:
    print("Solution found! Moves:", solution_moves)
else:
    print("No solution exists.")
