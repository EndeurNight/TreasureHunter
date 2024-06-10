# ==============================================================================
"""WIN : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # creation and destruction of static frames
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  win = Win(title='FRAMES', op=2)
  top = Frame(win) # create top frame to store the 3 Buttons
  Button(top, text='BRICK',  width=8, command=on_brick)
  Button(top, text='GRID',   width=8, command=on_grid)
  Button(top, text='SCALES', width=8, command=on_scales)
  Button(top, text='RESET',  width=8, command=on_reset)
  win.loop()
# ------------------------------------------------------------------------------
def on_reset():
  """on_reset window configuration by deleting bottom frame"""
  if win.widgets > 1: del win[1] # clear bottom frame if it exists
# ------------------------------------------------------------------------------
def on_brick():
  """create the brick configuration on the bottom frame"""
  on_reset(); Brick(win, width=500, height=300, bg='blue') # single Brick
# ------------------------------------------------------------------------------
def on_grid():
  """create the grid configuration on the bottom frame"""
  on_reset(); frame = Frame(win, fold=10) # create new frame to store the grid
  colors = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0')
  for loop in range(100): # create a 10x10 grid of Brick widgets
    Brick(frame, height=40, width=40, border=2, bg=colors, state=loop)
# ------------------------------------------------------------------------------
def on_scales():
  """create the scales configuration on the bottom frame"""
  on_reset(); frame = Frame(win, fold=2) # create new frame to store the scales
  for char in 'ABCDEF': # loop over chars to create specific Label/Scale pairs
    Label(frame, text=f"Value of {char} :", width=10, anchor='SE', grow=False)
    Scale(frame, scale=(0,99))
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
