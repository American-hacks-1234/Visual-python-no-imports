#PASTE BELOW ALL THE V2 code

def Example_30_second_video():
    """Creates a 30 second non-repeating animated video"""
    clear_grid()
    render_frame()
    
    # Stage 1: Spiral explosion from center (0-7 seconds)
    for frame in range(14):
        clear_grid()
        center_x, center_y = 3, 2
        radius = frame * 0.5
        
        for y in range(6):
            for x in range(7):
                dist = ((x - center_x)**2 + (y - center_y)**2)**0.5
                if abs(dist - radius) < 1:
                    color = r if frame % 3 == 0 else (g if frame % 3 == 1 else b)
                    set_cell(x, y, color)
        
        render_frame()
    
    # Stage 2: Rain effect from top (7-15 seconds)
    for frame in range(16):
        clear_grid()
        for y in range(6):
            if (frame - y) >= 0 and (frame - y) < 6:
                for x in range(7):
                    if (frame + x) % 3 == 0:
                        set_cell(x, y, p)
                    elif (frame + x) % 3 == 1:
                        set_cell(x, y, b)
        render_frame()
    
    # Stage 3: Converging checkerboard (15-23 seconds)
    for frame in range(16):
        clear_grid()
        intensity = frame / 15
        
        for y in range(6):
            for x in range(7):
                dist_from_edge = min(x, y, 6 - x, 5 - y)
                if dist_from_edge < intensity * 3:
                    color = g if (x + y) % 2 == 0 else r
                    set_cell(x, y, color)
        
        render_frame()
    
    # Stage 4: Pulsing finale (23-30 seconds)
    for frame in range(14):
        clear_grid()
        pulse = abs(7 - frame % 14) / 7
        
        for y in range(6):
            for x in range(7):
                if (x + y) % 2 == 0:
                    set_cell(x, y, b if pulse > 0.5 else g)
                else:
                    set_cell(x, y, r if pulse > 0.5 else p)
        
        render_frame()
    
    print(f"{g} 30 Second Animation Complete!")

if __name__ == "__main__":
    Example_30_second_video()
