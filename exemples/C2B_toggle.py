# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # use multi-state Brick widgets as grid cells
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(rows=8, cols=16):
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='TOGGLE', op=4, fold=cols) # fold every 'cols' widgets
  # ----------------------------------------------------------------------------
  colors = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0') # define color set
  for loop in range(rows*cols): # loop over grid cells (nb of cells = rows*cols)
    # create Brick with 6 different states : one for each background color
    Brick(win, height=64, width=64, border=2, bg=colors, state=2) # 2 <=> blue
  # ----------------------------------------------------------------------------
  win.after(3000, tick); win.loop() # wait 3000 ms then start animation
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
