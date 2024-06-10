# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # perform animation by manual editing of widget properties
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='TOGGLE', border=2, fold=5) # fold every 5 widgets
  # ----------------------------------------------------------------------------
  for loop in range(25) : # loop over grid cells (5x5)
    Brick(win, height=64, width=64, bg='#00F', border=2) # create a blue Brick
  # ----------------------------------------------------------------------------
  win.after(2000, tick) # launch 'tick' to start animation after 2000 ms
  win.loop()
# ------------------------------------------------------------------------------
def tick():
  """update function for widget animation"""
  # toggle the background color of the widget located at coordinates (2,2)
  win[2][2]['bg'] = '#F00' if win[2][2]['bg'] == '#00F' else '#00F'
  win.after(500, tick) # launch 'tick' again after 500 ms
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
