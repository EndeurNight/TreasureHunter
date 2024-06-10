# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # animate scrolling sprites on Canvas
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(width=900, height=500):
  """main program of the "canvas" module"""
  global win
  win = Win(title='CANVAS', grow=False)
  win.canvas = Canvas(win, width=width, height=height, bg='#000')
  win.width, win.height, win.sprites = width, height, [] # store attributes
  win.images = ImageGrid('smileys.png') # load grid of 6 smiley images (RGBA)
  win.step, win.counter = 0, 0 # initialize step counter and sprite counter
  win.after(1000, tick); win.loop() # wait 1000ms and launch animation
# ------------------------------------------------------------------------------
def tick():
  """move all canvas items and make recursive function call after 10ms"""
  if win.counter == 200: return win.exit() # close window after 200 sprites
  if win.step == 0: # create new sprite when step counter drops to zero
    win.step = max(5, 50-win.counter); win.counter += 1 # update both counters
    # select random image, position and velocity for new sprite
    image = win.images[rr(6)]; w, h = image.width()//2, image.height()//2
    x, y, vx, vy = rr(win.width), -h, 0.1*rr(10), 1.0
    if 2*x > win.width: vx = -vx # reverse vx when sprite starts on the right
    item = win.canvas.create_image(x, y, image=image) # add image to canvas
    win.sprites.append([item, x, y, w, h, vx, vy]) # store sprite parameters
  item, x, y, w, h, vx, vy = win.sprites[0] # get parameters for eldest sprite
  if y-h > win.height: # delete eldest sprite when it goes out of screen
    win.canvas.delete(item); win.sprites.pop(0)
  win.step -= 1; speed = 1+win.counter/5 # set speed according to sprite counter
  for sprite in win.sprites: # loop over remaining sprites
    item, x, y, w, h, vx, vy = sprite # get parameters for current sprite
    x, y = x + vx*speed, y + vy*speed # compute new position for sprite
    win.canvas.coords(item, x, y) # update item coordinates on canvas
    sprite[1:3] = x, y # update sprite parameters
  win.canvas.after(10, tick) # call 'tick' again after 10ms
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
