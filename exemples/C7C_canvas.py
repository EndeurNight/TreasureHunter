# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # create 6 images as moving sprites
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main(width=640, height=480):
  """main program of the "canvas" module"""
  global win
  win = Win(title='CANVAS', grow=False)
  win.canvas = Canvas(win, width=width, height=height, bg='#000')
  win.width, win.height, win.sprites = width, height, [] # store attributes
  win.images = ImageGrid('smileys.png') # extract images from image grid
  # ----------------------------------------------------------------------------
  dx, dy = width/7, height/7 # initial distance between neighboring sprites
  for n in range(6): # create 6 sprites (= images) on canvas
    # define dimension, initial position and initial velocity for each sprite
    x, y, vx, vy = dx+n*dx, dy+n*dy, 3-n, n-2 # initial position and velocity
    image = win.images[n]; w, h = image.width()//2, image.height()//2
    item = win.canvas.create_image(x, y, image=image) # add sprite to canvas
    win.sprites.append([item, x, y, w, h, vx, vy]) # store sprite parameters
  # ----------------------------------------------------------------------------
  win.after(1000, tick) # start animation after 1000ms
  win.loop()
# ------------------------------------------------------------------------------
def tick():
  """move all canvas items and make recursive function call after 10ms"""
  for sprite in win.sprites:
    item, x, y, w, h, vx, vy = sprite # get sprite parameters
    x, y = x+vx, y+vy # compute new position for sprite (add current velocity)
    if x-w+6 < 0 or x+w-6 > win.width: vx = -vx # horizontal bounce (reverse vx)
    if y-h+6 < 0 or y+h-6 > win.height: vy = -vy # vertical bounce (reverse vy)
    win.canvas.coords(item, x, y) # update item coordinates on canvas
    sprite[1:] = x, y, w, h, vx, vy # update sprite parameters
  win.canvas.after(10, tick) # recursive call of 'tick' after 10ms
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
