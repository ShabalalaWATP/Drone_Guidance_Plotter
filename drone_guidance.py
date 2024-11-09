# Drone route plotting program
# Plots routes on a 12x12 grid based on input files

import sys
import os.path

def read_route_file(filename):
    # Reads the route file and returns coordinates and directions
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Clean up the data
            data = [line.strip() for line in lines if line.strip()]
            
            # Get starting position and list of directions
            start_x = int(data[0])
            start_y = int(data[1])
            directions = data[2:]
            
            return start_x, start_y, directions
    except FileNotFoundError:
        print("File not found")
        return None
    except (ValueError, IndexError):
        print("Invalid file format")
        return None

def validate_and_plot_route(start_x, start_y, directions):
    # Creates and checks the route, returns the grid and path if valid
    # Set up empty grid
    grid = [['.'] * 12 for _ in range(12)]
    
    # Convert to 0-based indexing for calculations
    current_x = start_x - 1
    current_y = 12 - start_y  # Flip Y coordinate for display
    
    # Check starting position is on grid
    if not (0 <= current_x < 12 and 0 <= current_y < 12):
        return None, None
    
    # Keep track of path
    path = [(start_x, start_y)]
    grid[current_y][current_x] = 'S'  # Mark start
    
    # Movement lookup
    moves = {
        'N': (0, -1),  # Up
        'S': (0, 1),   # Down
        'E': (1, 0),   # Right
        'W': (-1, 0)   # Left
    }
    
    # Plot the route
    last_pos = None
    for direction in directions:
        if direction not in moves:
            return None, None
            
        dx, dy = moves[direction]
        current_x += dx
        current_y += dy
        
        # Make sure we're still on the grid
        if not (0 <= current_x < 12 and 0 <= current_y < 12):
            return None, None
            
        # Add to path (converting back to 1-based coordinates)
        path.append((current_x + 1, 12 - current_y))
        
        # Mark the route on grid
        if last_pos:
            grid[last_pos[1]][last_pos[0]] = '+'
        last_pos = (current_x, current_y)
    
    # Mark where we ended up
    if last_pos:
        grid[last_pos[1]][last_pos[0]] = 'E'
    
    return grid, path

def display_grid(grid):
    # Shows the grid with numbers and formatting
    # Print column numbers
    print("   ", end="")
    for i in range(1, 13):
        print(f"{i:2}", end=" ")
    print("\n   " + "-" * 36)
    
    # Print rows with numbers
    for i, row in enumerate(grid):
        print(f"{12-i:2}|", end=" ")
        print(" ".join(row))

def main():
    # Main program loop
    while True:
        filename = input("\nEnter the next route instructions file, or enter STOP to finish: ")
        if filename.upper() == "STOP":
            break
            
        # Try to plot the route
        result = read_route_file(filename)
        if result is None:
            continue
            
        start_x, start_y, directions = result
        
        grid, path = validate_and_plot_route(start_x, start_y, directions)
        
        if grid is None:
            print("Error: The route is outside of the grid")
        else:
            print("\nRoute coordinates:")
            for x, y in path:
                print(f"({x},{y})")
            
            print("\nRoute plot:")
            display_grid(grid)

if __name__ == "__main__":
    main()