# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # create 3 color circles as moving sprites
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main(width=640, height=480):
  """main program of the "canvas" module"""
  global win
  win = Win(title='CANVAS', grow=False)
  win.canvas = Canvas(win, width=width, height=height)
  win.width, win.height, win.sprites = width, height, []
  # ----------------------------------------------------------------------------
  colors = ('#F00','#0F0','#00F','#000')
  dx, dy = width/4, height/4 # set initial distance between neighboring sprites
  w = h = min(width, height)/8 # set dimension for all sprites
  for n in range(3): # create 3 sprites (= color disks) on canvas
    x, y, vx, vy = dx+n*dx, dy+n*dy, 3-n, n+1 # initial position and velocity
    item = win.canvas.create_oval(x-w, y-h, x+w, y+h, width=5,
      outline=colors[3], fill=colors[n]) # add item (= color circle) to canvas
    win.sprites.append([item, x, y, w, h, vx, vy]) # store sprite parameters
  # ----------------------------------------------------------------------------
  win.after(1000, tick) # start animation after 1000ms
  win.loop()
# ------------------------------------------------------------------------------
def tick():
  """move all canvas items and make recursive function call after 10ms"""
  for sprite in win.sprites: # loop over sprites
    item, x, y, w, h, vx, vy = sprite # get sprite parameters
    x, y = x+vx, y+vy # compute new position for sprite (add current velocity)
    if x-w < 0 or x+w > win.width:  vx = -vx # horizontal bounce (reverse vx)
    if y-h < 0 or y+h > win.height: vy = -vy # vertical bounce (reverse vy)
    win.canvas.coords(item, x-w, y-h, x+w, y+h) # update item coords on canvas
    sprite[1:] = x, y, w, h, vx, vy # update sprite parameters
  win.canvas.after(10, tick) # call 'tick' again after 10ms
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
