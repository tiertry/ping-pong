from pygame import *

win_width = 700
win_height = 500
main_win = display.set_mode((win_width, win_height))

back = (255, 222, 111)
main_win.fill(back)

game = True 
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        main_win.fill(back)
        display.update()
        time.delay(50)