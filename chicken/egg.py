
import random as rand
import turtle as trtl
import time

##################
### Game setup ###
##################

wn = trtl.Screen()
wn.addshape("chicken.gif")
wn.addshape("button.gif")
wn.bgpic("grass.gif")

# Score Writer
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-200, -180)
score_writer.pendown()

# Upgrade Button
button = trtl.Turtle()
button.speed(0)
button.shape("button.gif")
button.penup()
button.setposition(-170, 180)

# Points per click
score_rate = 1
upgrade_cost = (score_rate*2)**2

rate = trtl.Turtle()
rate.speed(0)
rate.penup()
rate.hideturtle()
rate.setposition(-200, -220)
rate.pendown()
rate.write("Eggs per click: " + str(score_rate))

next = trtl.Turtle()
next.speed(0)
next.penup()
next.hideturtle()
next.setposition(-220, 200)
next.pendown()
next.write("Next upgrade: " + str(upgrade_cost) + " eggs")

# Chicken
egg = trtl.Turtle()
score = 0
egg.shape("chicken.gif")
egg.speed(0)
egg.penup()

font_setup = ("Arial", "15", "normal")

score_writer.write(str(score) + " eggs", font = font_setup)

# Points text
p = trtl.Turtle()
p.hideturtle()
p.speed(3)



######################
### Game functions ###
######################

def eg_click(x, y):
  update_score()
  change_position()
  point()

def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 130)
  egg.hideturtle()
  egg.setposition(new_xpos, new_ypos)
  egg.showturtle()

def update_score():
  score_writer.clear()
  global score
  score += score_rate
  score_writer.write(str(score) + " eggs", font = font_setup)

def point():
  p.clear()
  p.penup()
  p.setposition(egg.xcor()+7, egg.ycor()+20)
  p.pendown()
  p.write("+"+str(score_rate))
  p.penup()

def button_click(x, y):
  upgrade() 

def upgrade():
  global score_rate
  global score
  global upgrade_cost
  if score >= upgrade_cost:
    score_rate += 1
    rate.clear()
    rate.write("Eggs per click: " + str(score_rate))
    score -= upgrade_cost
    score_writer.clear()
    score_writer.write(str(score) + " eggs", font = font_setup)
    upgrade_cost = (score_rate*2)**2

    next.clear()
    next.write("Next upgrade: " + str(upgrade_cost) + " eggs")

button.onclick(button_click)
egg.onclick(eg_click)

wn.mainloop()