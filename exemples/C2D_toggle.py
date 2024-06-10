# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # combine several properties in multi-state widgets
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(rows=5, cols=7):
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  bg = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0','#000','#FFF')
  fg = ('#FFF','#000') # number of states may be different for each property
  text = ('RED','GREEN','BLUE','CYAN','MAGENTA','YELLOW','BLACK','WHITE')
  win = Win(title='TOGGLE', font='Arial 16 bold', bg='#000', fold=cols, op=2)
  # ----------------------------------------------------------------------------
  for loop in range(rows*cols): # loop over grid (number of cells = rows*cols)
    Label(win, text=text, height=3, width=9, bg=bg, fg=fg, state=loop)
  # ----------------------------------------------------------------------------
  win.after(2000, tick); win.loop()
# ------------------------------------------------------------------------------
def tick():
  """update function for widget animation"""
  rows, cols = win.widgets # get number of rows/cols for the grid of widgets
  states = win[0][0].states # get number of states for each grid cell
  row, col = rr(rows), rr(cols) # select random position
  win[row][col].state = rr(states) # set random widget to random state
  win.after(20, tick) # launch 'tick' again after 20 ms
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
