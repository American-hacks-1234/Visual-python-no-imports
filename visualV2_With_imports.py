import time
import sys

def clear_previous_outputs(lines_to_clear):
    """Clears a specified number of previous lines from the console."""
    for _ in range(lines_to_clear):
        sys.stdout.write('\033[1A') # Move cursor up one line
        sys.stdout.write('\033[K')  # Clear line from cursor to the end
    sys.stdout.flush()
r = "\033[31m"  # Red r
w = "\033[0m"  # White (Reset) w
b = "\033[34m"  # Blue b
g = "\033[32m"  # Green g
p = "\033[35m"  # Purple p
G = "\033[2m"   # Grey G

# 5x6 grid (5 width, 6 height)
grid = [
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w]
]

def clear_grid():  
    """Reset all grid cells to white"""

    for row in grid:
        for i in range(len(row)):
            row[i] = w

def render_frame():
    time.sleep(0.5)
    clear_previous_outputs(10)
    """Render the current frame to terminal"""
    for row in grid:
        print("".join(f"{color}███" for color in row) + w)

def set_cell(x, y, color):
    """Set a specific cell to a color
    x = column (0-7)
    y = row (0-6)
    color = color code (r, w, b, g, p, G)
    """
    if 0 <= y < 6 and 0 <= x < 7:
        grid[y][x] = color
    else:
        print(f"Error: coordinates out of bounds (x: 0-7, y: 0-6)")

def test_colors():
    """Test all available colors"""
    print(f'{w}Testing colors...')
    print(f"{r}Red{w} {g}Green{w} {b}Blue{w} {p}Purple{w} {G}Grey{w}")

def test_reset():
    test_colors()
    render_frame()
    clear_previous_outputs(10)
    print("==Testing Done==\n")
    time.sleep(0.75)
    clear_previous_outputs(10)
    print(f"{r}==Testing Done==\n")
    time.sleep(0.75)
    clear_previous_outputs(10)
    print(f"{g}==Testing Done==\n")
    time.sleep(0.75)
    clear_previous_outputs(10)
    print(f"{b}==Testing Done==\n")
    
    clear_grid()
    render_frame()

if __name__ == "__main__":
  test_reset()
