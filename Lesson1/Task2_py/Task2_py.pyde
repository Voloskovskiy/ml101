#def setup():
#    size(1000, 1000)
#    background(0, 255, 0)
#def draw():
#    line(4, 100, 900, 100)
#    stroke(10, 21, 200)
#    line(10, 4, 34, 65)
#    fill(255, 190, 100)
#    triangle(500, 500, 900, 900, 100, 900)
#    arc(200, 700, 280, 280, PI, TWO_PI)
#print('Task1 done')
#rect(x, y, x_length, y_length) # прямоугольник  
#ellipse(x_center, y_center, radius_1, radius_2) # эллипс 
#triangle(x1, y2, x2, y2, x3, y3) # треугольник
#arc(479, 300, 280, 280, PI, TWO_PI) # арка

def setup():
    size(1000, 1000)
    background(255)
def draw():
    x = width
    y = height
    fill(0, 0, 0)
    rect(10, 10, x-20, y-20)
    
    fill(0, 255, 0)
    stroke(255, 255, 255)
    strokeWeight(5)
    rect(350, 400, 300, 150, 30)
    fill(255, 255, 255)
    ellipse(500, 475, 100, 100)
    line(350, 475, 650, 475)
    fill(0, 255, 0)
    rect(370, 550, 50, 50)
    rect(580, 550, 50, 50)
    
    quad(365, 600, 420, 600, 425, 670, 350, 670)
    quad(580, 600, 635, 600, 650, 670, 575, 670)
    
    quad(350, 670, 425, 670, 425, 685, 340, 685)
    quad(575, 670, 650, 670, 660, 685, 575, 685)
    
    
    arc(500, 395, 250, 190, PI, TWO_PI)
    fill(255, 255, 255)
    ellipse(430, 360, 40, 40)
    ellipse(570, 360, 40, 40)
    
    fill(0, 255, 0)
    arc(348, 495, 130, 130, radians(180), radians(270))
    arc(653, 495, 130, 130, radians(270), radians(360))
    
    rect(300, 495, 30, 40)
    rect(670, 495, 30, 40)
    
    quad(300, 535, 330, 535, 335, 565, 290, 565 )
    quad(670, 535, 700, 535, 710, 565, 665, 565 )
    
    arc(340, 568, 100, 70, radians(90), radians(180))
    arc(660, 568, 100, 70, 0, radians(90))
    
    
    
    
    
    
