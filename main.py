from time import sleep
from screen import Screen
import numpy as np
import os 

TAKE_INPUT = False
FRAME_TIME = 1/60
WIDTH = 120
HEIGHT = 60
def main():
    output = Screen(WIDTH, HEIGHT)
    pos = np.array([15., 15.])
    radius = 10
    v = np.array([50., -50.])
    a =  np.array([0., 80])
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pos)
        print(radius)
        render_pos = pos.astype(int)
        print(render_pos)
        output.clear()
        output.draw_circle(render_pos, radius, 3)
        print(output)
        if TAKE_INPUT:
            action  = input(":")
            if action == 'w':
                pos[1] -= 1
            if action == 'a':
                pos[0] -= 1

            if action == 's':
                pos[1] += 1
            
            if action == 'd':
                pos[0] += 1

            if action == 'q':
                radius += 1
            
            if action == 'e':
                radius -= 1
        else:
            if pos[0] + radius > WIDTH or pos[0]- radius < 0:
                v[0] = v[0] * -(1 + 0.5 * FRAME_TIME)
            
            if pos[1] + radius > HEIGHT or pos[1] - radius < 0:
                v[1] = v[1] * -(1 + 0.5 * FRAME_TIME)

            v += a * FRAME_TIME
            pos += v * FRAME_TIME

            v= v * (1 - 0.01*FRAME_TIME)
            
            
            sleep(FRAME_TIME)
    return

if __name__ == "__main__":
    main()