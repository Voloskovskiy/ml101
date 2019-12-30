angle = 0.0
speed = 0.005

def setup():
   size(1000, 1000)
   fill(0)
   noStroke()
   frameRate(1.5)
def fig(el, i, j):
        if el == 1:
            ellipse(i, j, 30, 30)
        if el == 2:
            rect(i-15, j-15, 30, 30)
        if el == 3:
            arc(i, j, 30, 30, PI, TWO_PI)
def draw():   
    background(0, 0, 0)
    global angle
    

    for i in range(100, width, 100):
        for j in range(100, height, 100):
            fill(random(0,255),random(0,255),random(0,255))
            el = random(1,4)
            fig(int(el), i, j)
            
def mousePressed():
    x = mouseX/100
    y = mouseY/100
    
    for i in range(100, width, 100):
        for j in range(100, height, 100):
            fill(random(0,255),random(0,255),random(0,255))
            el = random(1,4)
            fig(int(el), i+x, j+y)
    
