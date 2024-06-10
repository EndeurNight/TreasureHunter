# ==============================================================================
"""EVENT : demo program for keyboard and mouse event handlers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # use arrow keys to control cursor movement
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main(rows=9, cols=9, size=64):
  """create the main window and pack the widgets"""
  global win; win = Win(title='EVENT', fold=cols, key=on_key, grow=False)
  colors = ('#00F','#0F0','#F00') # define color set for board cells
  # ----------------------------------------------------------------------------
  for loop in range(rows*cols): # create all grid cells
    Brick(win, height=size, width=size, border=2, bg=colors)
  # ----------------------------------------------------------------------------
  # put cursor (= green cell) at the center of the grid
  win.cursor = win[rows//2][cols//2]; win.cursor.state = 1
  # put some walls (= red cells) near the corners of the grid
  walls = ((0,0),(1,0),(0,1),(-1,-1),(-2,-1),(-1,-2),(-1,0),(0,-1))
  for row,col in walls: win[row][col].state = 2
  # ----------------------------------------------------------------------------
  win.loop()
# ------------------------------------------------------------------------------
def on_key(widget, code, mods):
  """callback function for all 'key' events"""
  moves = {'Up':(-1,0), 'Down':(1,0), 'Right':(0,1), 'Left':(0,-1)}
  if code not in moves: return # nothing to do if key is not an arrow key
  rows, cols = win.widgets # get total number of rows and cols
  row, col = win.cursor.index # get current cursor position
  drow, dcol = moves[code] # get displacement vector
  # compute new position for cursor by using modulo to get automatic cycling
  row, col = (row + drow) % rows, (col + dcol) % cols
  if win[row][col].state == 2: return # cursor blocked by red square
  win.cursor.state = 0; win.cursor = win[row][col]; win.cursor.state = 1 # move
# ==============================================================================
if __name__ == '__main__':
  main() # create window with default parameters
  #main(32,32,24) # try alternative set of parameters
# ==============================================================================
