WIDTH = 720
HEIGHT = 720

import time,random,datetime

squaresize = 60
player = Actor("monopolyhat_45x45")
player.pos = 90,90

squares = {
"GO":[1,1,(0,255,255)],
"FREE":[10,10,(255,255,0)],
"JAIL":[10,1,(255,0,255)]
}

currentpos = 0

boardpos = []

for i in range(10):
    boardpos.append([90 + squaresize * i,90])
for i in range(10):
    boardpos.append([630,90 + squaresize * i])
for i in range(10):
    boardpos.append([630 - squaresize * i,630])
for i in range(10):
    boardpos.append([90,630 - squaresize * i])

print(boardpos)
thetime = 0

def draw():
    screen.fill((127,127,127))
    for s in squares:
        box = Rect((squares[s][0]*squaresize,squares[s][1]*squaresize,squaresize,squaresize))
        screen.draw.filled_rect(box,squares[s][2])
        screen.draw.text(s,(squares[s][0]*squaresize,squares[s][1]*squaresize))
    player.draw()

def move():
    global currentpos
    player.pos = boardpos[(currentpos+random.randint(1,6)+random.randint(1,6))%40]

def update():
    global thetime
    thetime += 1
    if thetime % 120 == 0:
        move()