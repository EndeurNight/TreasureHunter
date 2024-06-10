# ==============================================================================
"""WIN : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # toggle between two different master windows
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def config(rows=8, cols=8):
  """create the config window and pack the widgets"""
  global win
  win = Win(title='CONFIG', fold=2, op=2, grow=False) # config window
  # ----------------------------------------------------------------------------
  Label(win, text='Number of rows :', width=13, anchor='SW', grow=False)
  win.rowscale = Scale(win, scale=(1,12), length=200, flow='W', state=rows)
  Label(win, text='Number of cols :', width=13, anchor='SW', grow=False)
  win.colscale = Scale(win, scale=(1,12), length=200, flow='W', state=cols)
  Button(win, text='NEW GRID', command=grid)
  # ----------------------------------------------------------------------------
  win.loop()
# ------------------------------------------------------------------------------
def grid():
  """create the grid window and pack the widgets"""
  global win
  rows, cols = win.rowscale.state, win.colscale.state # get grid size
  win.exit() # exit config window (only after having read state of scales)
  win = Win(title='GRID', bg='#000', fold=cols, op=2, grow=False) # grid window
  images = ImageGrid('balls.gif') # load grid of 6 color balls (R,G,B,C,M,Y)
  for loop in range(rows*cols): Brick(win, image=images, state=loop)
  # ----------------------------------------------------------------------------
  win.loop(); config(rows, cols) # relaunch 'config' when grid window is closed
# ==============================================================================
if __name__ == "__main__":
  config()
# ==============================================================================
