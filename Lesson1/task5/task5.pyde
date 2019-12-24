pixels2D = [ [0, 250, 235, 201], 
             [100, 150, 30, 250],
             [0, 250, 235, 201],
             [100, 150, 30, 250] ]
pixelcolor = [ "255,0,0",
               "0,255,0",
               "0,0,255" ]
pixelcolor1 = "255,0,0"
size_kv = 200
x = len(pixels2D)*size_kv
y = len(pixels2D[0])*size_kv
start_x = 0
start_y = 0
def setup():
    size(x, y)
    background(255, 255, 255)
    noLoop() # draw() выполнится только один раз
def draw():
    global start_x
    global start_y
    global size_kv
    color = 0
    color_index = 0
    for row in range(len(pixels2D)):
        start_x = 0
        color = 0
        color_index = color_index+1
        for col in range(len(pixels2D[0])):
            random_color = random(0, 255)
            fill(random_color)
            color = color+1
            if color == color_index:
                 fill(pixelcolor1)
            rect(start_x, start_y, start_x+size_kv, start_y+size_kv)
            start_x = start_x + size_kv
        start_y = start_y + size_kv
