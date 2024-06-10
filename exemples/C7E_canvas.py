# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "5.0" # move ball with mouse and destroy canvas items
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(dim=800):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='CANVAS', move=on_move, op=2, grow=False)
  win.images = ImageGrid('balls.png'); win.image = Image('ball.png')
  win.canvas = Canvas(win, width=dim, height=dim, bg='#000', cursor='none')
  # create player ball with its score item (initial position = out of canvas)
  win.ball = win.canvas.create_image(-dim, 0, image=win.image)
  win.text = win.canvas.create_text(-dim, 0, text=0, font='Arial 16')
  # ----------------------------------------------------------------------------
  win.dim, win.score, win.balls = dim, 0, {}; win.after(1000, tick); win.loop()
# ------------------------------------------------------------------------------
def tick():
  """generate a new random ball on canvas and recurse after 1000ms"""
  x, y, n = rr(32,win.dim-32), rr(32,win.dim-32), rr(6) # random pos and color
  ball = win.canvas.create_image(x, y, image=win.images[n]) # create new ball
  win.balls[ball] = n; win.after(500, tick) # store ball color in dictionary
# ------------------------------------------------------------------------------
def on_move(widget, code, mods):
  """callback function for all 'mouse move' events"""
  if widget != win.canvas: return # mouse is not on canvas
  x, y = code; widget.coords(win.ball, x, y); widget.coords(win.text, x, y)
  # check if the player ball is currently overlapping any color ball on canvas
  balls = widget.find_overlapping(x-8,y-8,x+8,y+8)[2:]
  if not balls: return # no overlapping color ball has been found
  ball = balls[-1]; widget.delete(ball) # get color ball and delete it on canvas
  # update score on player ball, depending on the color of the deleted ball
  win.score += win.balls[ball]; widget.itemconfig(win.text, text=win.score)
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
