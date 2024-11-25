CHARS = [' ', '.',  '*',  '#', '@',]
class Screen:



    def __init__(self, w, h):
        self.pixels = [[0 for i in range(h)] for j in range(w)]
        #print(self.pixels)
        self.h = h
        self.w = w

    def clear(self):
        self.pixels = [[0 for i in range(self.h)] for j in range(self.w)]
        

    def __str__(self):
        string = ''
        
        for y in range(self.h):
            for x in range(self.w):
                string += self.pixel_to_str(self.pixels[x][y])
                string += ' '
            string += '\n'

        return string
    
    def draw_pixel(self, pos, val):
        if len(pos) != 2:
            return
        x = pos[0]
        y = pos[1]
        if x < self.w and y < self.h and x >= 0 and y >= 0:
            self.pixels[x][y] = val

    def draw_circle(self, pos, radius, val):
        for i in range(-radius, radius+1):
            for j in range(-radius, radius+1):
                if i ** 2 + j ** 2 <  radius ** 2:
                    curr_pixel = [pos[0] + i, pos[1] + j]
                    self.draw_pixel(curr_pixel, val)


    
    def pixel_to_str(self, value):
        return str(CHARS[value+1])