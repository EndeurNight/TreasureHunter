# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # 24 'Label' widgets with 2D packing
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  # 2D packing is obtained by defining property 'fold' for window
  win = Win(title='FRAME', fold=6) # default 2D flow direction (= 'E' then 'S')
  #win = Win(title='FRAME', fold=3, flow='NE') # pack N then E, fold every 3
  #win = Win(title='FRAME', fold=12, flow='WN') # pack W then N, fold every 12
  # ----------------------------------------------------------------------------
  for loop in range(24): Label(win, text=loop, width=4, height=2, border=1)
  # ----------------------------------------------------------------------------
  #properties()
  win.loop()
# ------------------------------------------------------------------------------
def properties():
  """view and edit some widget properties"""
  print(f"Number of widgets = {win.widgets}") # 2D flow -> (int, int)
  rows, cols = win.widgets # number of rows, number of cols
  for row in range(rows): # loop over widgets and show 'text' properties
    for col in range(cols):
      widget = win[row][col] # get current widget
      text, bg, fg = widget['text'], widget['bg'], widget['fg']
      width, height = widget['width'], widget['height']
      print(f"* Properties for win[{row}][{col}] :")
      print(f"  text={text} bg={bg} fg={fg} width={width} height={height}")
  # ----------------------------------------------------------------------------
  #win[2][1]['bg'] = 'red' # edit widget properties (use widget coordinates)
  #win[1][4]['bg'] = 'blue'; win[1][4]['fg'] = 'white'
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
