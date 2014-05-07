# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, image, state, erase_number, Turns
    cards = range(8)+range(8)
    exposed = [False for i in range(16)]
    random.shuffle(cards)
    state = 0
    Turns = 0
    erase_number = list()

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, erase_number, exposed_number, Turns
    n = pos[0] // 50
    if exposed[n] == False:
        if erase_number:
            for i in erase_number:
                exposed[i] = False
        exposed[n] = True
        state += 1
    if state == 1:
        exposed_number = n
    if state == 2:
        if cards[n] != cards[exposed_number]:
            erase_number = [exposed_number, n]
        else:
            erase_number = []
        state = 0
        Turns += 1
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(16):
        canvas.draw_text(str(cards[n]), (50* n,85), 100, 'White')
        if exposed[n] == False:
            canvas.draw_polygon([(0 + n * 50, 0), (0 + n * 50, 100), (50 + n * 50, 100), (50 + n * 50, 0)], 3, "Black", "Green")
    label.set_text('Turns = '+str(Turns))
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


# Always remember to review the grading rubric
