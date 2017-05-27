# implementation of card game - Memory

import simplegui
import random
cards = [1, 2, 3, 4, 5, 6, 7, 8] * 2
exposed = [[False] * 16]
deck = [50, 100]
x_pos = 50
y_pos = 60
x = 0
y = 100
card_width = 50
card_one = []
card_two = []
count = 0
# helper function to initialize globals
def new_game():
    global state, exposed, card_one, card_two, count
    label.set_text("Turns = 0")
    state = 0
    count = 0
    exposed = [False]*16
    card_one = []
    card_two = []
    random.shuffle(cards)
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, cards, card_one, card_two, count
    click = int(pos[0] // 50)
    if count <= 11:
        if exposed[click] == False:
            if state == 0:
                exposed[click] = True
                card_one = int(click)
                count += 1
                msg = "Turns = " + str(count)  
                label.set_text(msg)
                state = 1
            elif state == 1:
                exposed[click] = True
                card_two = int(click)
                state = 2
            else:
                if cards[card_one] != cards[card_two]:
                    exposed[card_one] = False
                    exposed[card_two] = False
                exposed[click] = True
                card_one = int(click)
                count += 1
                msg = "Turns = " + str(count)  
                label.set_text(msg)
                state = 1
def draw(canvas):
    for i in range(len(exposed)):
        if exposed[i] is True:
            canvas.draw_text(str(cards[i]), (17 + i * x_pos, y_pos), 36, 'White')   
        else:
            x = (25+ card_width * i)
            canvas.draw_line([x, 2], [x, 98], 48, 'Green')
 
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



