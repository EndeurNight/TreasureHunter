# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # 3 'Brick' widgets with 1D packing
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='FRAME') # use default 1D flow direction (= 'S')
  #win = Win(title='FRAME', flow='W') # change flow direction (= 'E','N' or 'W')
  #win = Win(title='FRAME', op=5) # add outer padding (in pixel units)
  # ----------------------------------------------------------------------------
  A, B, C = 'red', 'lime', 'blue'
  #A, B, C = '#FF0000', '#00FF00', '#0000FF'
  #A, B, C = '#F00', '#0F0', '#F0F'
  Brick(win, width=400, height=200, bg=A)
  Brick(win, width=400, height=200, bg=B)
  Brick(win, width=400, height=200, bg=C)
  # ----------------------------------------------------------------------------
  #properties()
  win.loop()
# ------------------------------------------------------------------------------
def properties():
  """view and edit some widget properties"""
  print(f"Number of widgets = {win.widgets}") # 1D flow -> int
  for n in (0,1,2): # loop over widgets and show their properties
    bg, width, height = win[n]['bg'], win[n]['width'], win[n]['height']
    print(f"* Properties for win[{n}] :")
    print(f"  bg={bg} width={width} height={height}")
  # ----------------------------------------------------------------------------
  #win[1]['bg'] = 'yellow' # edit widget property (use widget index)
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
