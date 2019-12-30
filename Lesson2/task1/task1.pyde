def setup():
    size(360, 360)
    noFill()
    frameRate(3)

def draw():
    background(255, 255, 255)
    for y in range(50, width - 50, 50):
        for x in range(50, height - 50, 50):
            fill(random(0,255),random(0,255),random(0,255))
            line(x,y,y,x)
            line(width-y,x,width-x,y) 
            ellipse(x+5,y-5,10,10)
            
        
            
