import turtle as t
import random as r


wn = t.Screen()
wn.bgcolor("steel blue")

# adding all the variables

deck = [(1, "Ace of Heart"), (2, "2 of Heart"), (3, "3 of Heart"), (4, "4 of Heart"), (5, "5 of Heart"),
        (6, "6 of Heart"), (7, "7 of Heart"), (8, "8 of Heart"), (9, "9 of Heart"), (10, "10 of Heart"),
        (10, "Jack of Heart"), (10, "Queen of Heart"), (10, "King of Heart"),
        (1, "Ace of Diamond"), (2, "2 of Diamond"), (3, "3 of Diamond"), (4, "4 of Diamond"),
        (5, "5 of Diamond"), (6, "6 of Diamond"), (7, "7 of Diamond"), (8, "8 of Diamond"),
        (9, "9 of Diamond"), (10, "10 of Diamond"), (10, "Jack of Diamond"),
        (10, "Queen of Diamond"), (10, "King of Diamond"), (1, "Ace of Spade"), (2, "2 of Spade"),
        (3, "3 of Spade"), (4, "4 of Spade"), (5, "5 of Spade"),
        (6, "6 of Spade"), (7, "7 of Spade"), (8, "8 of Spade"), (9, "9 of Spade"), (10, "10 of Spade"),
        (10, "Jack of Spade"), (10, "Queen of Spade"), (10, "King of Spade"),
        (1, "Ace of Club"), (2, "2 of Club"), (3, "3 of Club"), (4, "4 of Club"),
        (5, "5 of Club"), (6, "6 of Club"), (7, "7 of Club"), (8, "8 of Club"),
        (9, "9 of Club"), (10, "10 of Club"), (10, "Jack of Club"),
        (10, "Queen of Club"), (10, "King of Club")]
r.shuffle(deck)

dealer_count = 0
player_count = 0
dealer_turns = 0
player_turns = 0
player_xpos = -220
dealer_xpos = -220
player_ypos = 180
dealer_ypos = -180
count = 0
true = True
card = 0
num = 0
drawn = ''

# creation of all the turtles

t.penup()
t.color('sky blue')
t.hideturtle()
t.goto(-40, 180)
t.write('Player', font=('Arial', 30, 'normal'))
t.goto(-40, 140)
t.write('Score', font=('Arial', 30, 'normal'))
t.goto(-40, -140)
t.write('Dealer', font=('Arial', 30, 'normal'))
t.goto(-40, -180)
t.write('Score', font=('Arial', 30, 'normal'))

ht1 = t.Turtle()
ht1.color('sky blue')
ht1.hideturtle()
ht1.penup()

ht1.goto(-65, -50)
ht1.write('Hit', font=('Arial', 20, 'normal'))
ht1.goto(35, -50)
ht1.write('Stand', font=('Arial', 20, 'normal'))

player_s = t.Turtle()
player_s.color('sky blue')
player_s.hideturtle()
player_s.penup()

dealer_s = t.Turtle()
dealer_s.color('sky blue')
dealer_s.hideturtle()
dealer_s.penup()

hit = t.Turtle()
hit.color('sky blue')
hit.shape('circle')
hit.turtlesize(1)
hit.hideturtle()
hit.penup()
hit.goto(-50, 0)

stand = t.Turtle()
stand.color('sky blue')
stand.shape('circle')
stand.turtlesize(1)
stand.hideturtle()
stand.penup()
stand.goto(70, 0)

eleven = t.Turtle()
eleven.color('sky blue')
eleven.shape('circle')
eleven.turtlesize(1)
eleven.hideturtle()
eleven.penup()
eleven.goto(-50, 0)

one = t.Turtle()
one.color('sky blue')
one.shape('circle')
one.turtlesize(1)
one.hideturtle()
one.penup()
one.goto(50, 0)

player_t = t.Turtle()
player_t.color('sky blue')
player_t.penup()
player_t.hideturtle()
player_t.goto(player_xpos, player_ypos)

dealer_t = t.Turtle()
dealer_t.color('sky blue')
dealer_t.penup()
dealer_t.hideturtle()
dealer_t.goto(dealer_xpos, dealer_ypos)

card_t = t.Turtle()
card_t.color('sky blue')
card_t.penup()
card_t.hideturtle()
card_t.goto(dealer_xpos, dealer_ypos)

yes = t.Turtle()
yes.color('sky blue')
yes.shape('circle')
yes.turtlesize(1)
yes.hideturtle()
yes.penup()
yes.goto(-50, 280)

no = t.Turtle()
no.color('sky blue')
no.shape('circle')
no.turtlesize(1)
no.hideturtle()
no.penup()
no.goto(70, 280)

# allows user to pick 11 or 1 for an ace

# herherherhehrehrherhehrherhehrheh

def ace():
    global count
    stand.hideturtle()
    hit.hideturtle()
    ht1.clear()
    ht1.goto(-100,20)
    ht1.write("An ace was drawn", font=("Arial", 20, "normal"))
    ht1.goto(-65, -50)
    ht1.write('11', font=('Arial', 20, 'normal'))
    ht1.goto(35, -50)
    ht1.write('1', font=('Arial', 20, 'normal'))
    eleven.showturtle()
    one.showturtle()
    while True:
        eleven.onclick(eleven_touched)
        one.onclick(one_touched)
        if count == 1:
            break
    count = 0
    after_ace()

# resets back to hit and stand after value of ace was selected

def after_ace():
    ht1.clear()
    ht1.goto(-65, -50)
    ht1.write('Hit', font=('Arial', 20, 'normal'))
    ht1.goto(35, -50)
    ht1.write('Stand', font=('Arial', 20, 'normal'))
    eleven.hideturtle()
    one.hideturtle()
    stand.showturtle()
    hit.showturtle()

# adds eleven to player_count

def eleven_touched(x,y):
    global player_count, count
    player_count += 11
    count = 1

# adds one to player_count

def one_touched(x,y):
    global player_count, count
    player_count += 1
    count = 1

# this is the part where the dealer draws their cards

def dealer():
    global card, dealer_turns, dealer_count, dealer_xpos, dealer_ypos, num, drawn

    num, drawn = deck.pop(0)

    # part that changes scores the games

    if num == 1:
        if dealer_count + 11 <= 21:
            dealer_count += 11
        else:
            dealer_count += num
    else:
        if num > 10:
            dealer_count += 10
        else:
            dealer_count += num

    dealer_t.goto(dealer_xpos, dealer_ypos)

    """Checks if the first card is drawn and hides it from the player's view"""

    if dealer_turns == 0:
        card = drawn
        card_t.write('Card', font=('Arial', 15, 'normal'))
    else:
        dealer_t.write(drawn, font=('Arial', 15, 'normal'))

    """Moves the turtle to the correct position to then write the next card"""

    dealer_turns += 1
    dealer_xpos += 350
    if dealer_turns % 2 == 0:
        dealer_xpos = -220
        dealer_ypos += 40


# part that adds cards to player

def player():
    global player_turns, player_count, player_xpos, player_ypos, num, drawn

    num, drawn = deck.pop(0)

    # part that scores the game

    if num == 1:
        if player_count - 11 <= 21:
            ace()
        else:
            player_count += num
    else:
        if num > 10:
            player_count += 10
        else:
            player_count += num

    """Moves the turtle to the correct position to then write the next card"""

    player_t.goto(player_xpos, player_ypos)
    player_t.write(drawn, font=('Arial', 15, 'normal'))
    player_s.clear()
    player_s.goto(-10, 110)
    player_s.write(player_count, font=('Arial', 20, 'normal'))
    player_turns += 1
    player_xpos += 350
    if player_turns % 2 == 0:
        player_xpos = -220
        player_ypos -= 40


# when hitting it looks if a player has hit 21 or gone over 21

def hit_touch(x, y):
    global true
    player()
    if player_count > 21:
        t.goto(-130, 0)
        t.write('You Lost', font=('Arial', 50, 'normal'))
        dealer_s.goto(-10, 110)
        dealer_s.write(player_count, font=('Arial', 20, 'normal'))
        dealer_s.clear()
        dealer_s.goto(-10, -210)
        dealer_s.write(dealer_count, font=('Arial', 20, 'normal'))
        card_t.clear()
        card_t.write(card, font=('Arial', 15, 'normal'))
        true = False
        restart()
    elif dealer_count == 21 and player_count == 21:
        t.goto(-100, 0)
        t.write('Tie', font=('Arial', 50, 'normal'))
        true = False
        restart()
    elif player_count == 21:
        t.goto(-120, 0)
        t.write('You Won', font=('Arial', 50, 'normal'))
        dealer_s.goto(-10, 110)
        dealer_s.write(player_count, font=('Arial', 20, 'normal'))
        dealer_s.clear()
        dealer_s.goto(-10, -210)
        dealer_s.write(dealer_count, font=('Arial', 20, 'normal'))
        card_t.clear()
        card_t.write(card, font=('Arial', 15, 'normal'))
        true = False
        restart()


# checks if dealer_count is higher than the player_count and does not go over 21

def stand_touch(x, y):
    global dealer_count, true
    while dealer_count <= player_count != 21:
        dealer()
        dealer_s.clear()
        dealer_s.goto(-10, -210)
        dealer_s.write(dealer_count, font=('Arial', 20, 'normal'))
    dealer_s.clear()
    dealer_s.goto(-10, -210)
    dealer_s.write(dealer_count, font=('Arial', 20, 'normal'))
    if dealer_count > 21:
        t.goto(-120, 0)
        t.write('You Won', font=('Arial', 50, 'normal'))
        card_t.clear()
        card_t.write(card, font=('Arial', 15, 'normal'))
        true = False
        restart()
    elif 21 >= dealer_count > player_count:
        t.goto(-130, 0)
        t.write('You Lost', font=('Arial', 50, 'normal'))
        card_t.clear()
        card_t.write(card, font=('Arial', 15, 'normal'))
        true = False
        restart()
    elif dealer_count < 21 and dealer_count < player_count:
        t.goto(-120, 0)
        t.write('You Won', font=('Arial', 50, 'normal'))
        card_t.clear()
        card_t.write(card, font=('Arial', 15, 'normal'))
        true = False
        restart()
    elif dealer_count == 21 and player_count == 21:
        t.goto(-100, 0)
        t.write('Tie', font=('Arial', 50, 'normal'))
        card_t.clear()
        card_t.write(card, font=('Arial', 15, 'normal'))
        true = False
        restart()

# asking the user if they want to play again or end the game

def restart():
    hit.hideturtle()
    stand.hideturtle()
    ht1.clear()
    t.goto(-150,300)
    t.write("Do you want to play again?", font=("Arial", 20, "normal"))
    yes.showturtle()
    no.showturtle()
    t.goto(-75,230)
    t.write("YES", font=("Arial", 20, "normal"))
    t.goto(52.5, 230)
    t.write("NO", font=("Arial", 20, "normal"))

# when touched will reset the game

def yes_touched(x,y):
    global true, dealer_count, player_count, dealer_turns, player_turns, player_xpos, dealer_xpos, player_ypos, dealer_ypos, deck

    deck = [(1, "Ace of Heart"), (2, "2 of Heart"), (3, "3 of Heart"), (4, "4 of Heart"), (5, "5 of Heart"),
            (6, "6 of Heart"), (7, "7 of Heart"), (8, "8 of Heart"), (9, "9 of Heart"), (10, "10 of Heart"),
            (10, "Jack of Heart"), (10, "Queen of Heart"), (10, "King of Heart"),
            (1, "Ace of Diamond"), (2, "2 of Diamond"), (3, "3 of Diamond"), (4, "4 of Diamond"),
            (5, "5 of Diamond"), (6, "6 of Diamond"), (7, "7 of Diamond"), (8, "8 of Diamond"),
            (9, "9 of Diamond"), (10, "10 of Diamond"), (10, "Jack of Diamond"),
            (10, "Queen of Diamond"), (10, "King of Diamond"), (1, "Ace of Spade"), (2, "2 of Spade"),
            (3, "3 of Spade"), (4, "4 of Spade"), (5, "5 of Spade"),
            (6, "6 of Spade"), (7, "7 of Spade"), (8, "8 of Spade"), (9, "9 of Spade"), (10, "10 of Spade"),
            (10, "Jack of Spade"), (10, "Queen of Spade"), (10, "King of Spade"),
            (1, "Ace of Club"), (2, "2 of Club"), (3, "3 of Club"), (4, "4 of Club"),
            (5, "5 of Club"), (6, "6 of Club"), (7, "7 of Club"), (8, "8 of Club"),
            (9, "9 of Club"), (10, "10 of Club"), (10, "Jack of Club"),
            (10, "Queen of Club"), (10, "King of Club")]
    r.shuffle(deck)

    dealer_count = 0
    player_count = 0
    dealer_turns = 0
    player_turns = 0
    player_xpos = -220
    dealer_xpos = -220
    player_ypos = 180
    dealer_ypos = -180
    t.hideturtle()
    hit.hideturtle()
    stand.hideturtle()
    yes.hideturtle()
    no.hideturtle()
    t.clear()
    player_s.clear()
    dealer_s.clear()
    player_t.clear()
    dealer_t.clear()
    ht1.clear()
    hit.clear()
    stand.clear()
    card_t.clear()
    t.penup()
    t.goto(-40, 180)
    t.write('Player', font=('Arial', 30, 'normal'))
    t.goto(-40, 140)
    t.write('Score', font=('Arial', 30, 'normal'))
    t.goto(-40, -140)
    t.write('Dealer', font=('Arial', 30, 'normal'))
    t.goto(-40, -180)
    t.write('Score', font=('Arial', 30, 'normal'))
    ht1.goto(-65, -50)
    ht1.write('Hit', font=('Arial', 20, 'normal'))
    ht1.goto(35, -50)
    ht1.write('Stand', font=('Arial', 20, 'normal'))
    true = True
    start()


# ends the game

def no_touched(x,y):
    wn.bye()


# while loop that keeps the game running for some reason


def start():
    global true
    while true:
        if dealer_turns < 2:
            dealer()
        if player_turns < 2:
            player()
            if player_count > 21:
                t.goto(-130, 0)
                t.write('You Lost', font=('Arial', 50, 'normal'))
                dealer_s.goto(-10, 110)
                dealer_s.write(player_count, font=('Arial', 20, 'normal'))
                dealer_s.clear()
                dealer_s.goto(-10, -210)
                dealer_s.write(dealer_count, font=('Arial', 20, 'normal'))
                card_t.clear()
                card_t.write(card, font=('Arial', 15, 'normal'))
                true = False
                restart()
            elif dealer_count == 21 and player_count == 21:
                t.goto(-100, 0)
                t.write('Tie', font=('Arial', 50, 'normal'))
                true = False
                restart()
            elif player_count == 21:
                t.goto(-120, 0)
                t.write('You Won', font=('Arial', 50, 'normal'))
                dealer_s.goto(-10, 110)
                dealer_s.write(player_count, font=('Arial', 20, 'normal'))
                dealer_s.clear()
                dealer_s.goto(-10, -210)
                dealer_s.write(dealer_count, font=('Arial', 20, 'normal'))
                card_t.clear()
                card_t.write(card, font=('Arial', 15, 'normal'))
                true = False
                restart()
        if player_turns == 2 and true != False:
            hit.showturtle()
            stand.showturtle()
        hit.onclick(hit_touch)
        stand.onclick(stand_touch)
        yes.onclick(yes_touched)
        no.onclick(no_touched)

start()
wn.mainloop()
