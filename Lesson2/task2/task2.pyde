angle = 0
offset = 150
step = 100
speed = 0.07
num = 20
def setup():
    size(800, 300)
    fill(0)
    noStroke()
def draw():
    
    plus = [0, 0.4, 0.5, 0.7, 0.9, 1.1, 1.4, 1.5]
    background(255, 255, 255)
    global angle 
    
    def coord_y(triger):
        y_mass = []
        if triger == 1:
            for z in range(100, width, 100):
                y_mass.append(offset + sin(angle+plus[(z/100)-1]) * step)
        if triger == 2:
            for b in range(100, width, 100):
                y_mass.append(offset + cos(angle+plus[(b/100)-1]) * step)
        return(y_mass)
    c_y = coord_y(1)
    s_y = coord_y(2)
    def create(mas):
        fill(random(0,255),random(0,255),random(0,255))
        for x in range(100, width, 100):
            ellipse(x, mas[(x/100)-1], 20, 20)
    create(s_y)
    create(c_y) 
    angle = angle + speed
