# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # use multi-state Label widgets for grid cells
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(rows=8, cols=16):
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='TOGGLE', bg='#000', op=4, fold=cols)
  # ----------------------------------------------------------------------------
  images = ImageGrid('balls.gif') # load grid of 6 color balls (R,G,B,C,M,Y)
  for loop in range(rows*cols): # loop over grid cells (nb of cells = rows*cols)
    # create Brick with 6 different states : one for each color ball
    Brick(win, image=images, state=loop) # initial state = color cycling
  # ----------------------------------------------------------------------------
  win.after(2000, tick); win.loop() # wait 2000 ms then start animation
# ------------------------------------------------------------------------------
def tick():
  """update function for widget animation"""
  rows, cols = win.widgets # get number of rows/cols for the grid of widgets
  states = win[0][0].states # get number of states for each grid cell
  row, col = rr(rows), rr(cols) # select random position
  win[row][col].state = rr(states) # set selected widget to random state
  win.after(20, tick) # launch 'tick' again after 20 ms
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
