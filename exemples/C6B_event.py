from ezTK import *


# ------------------------------------------------------------------------------
def main(rows=10, cols=12):
  """create the main window and pack the widgets"""
  # create window and set global callbacks for 'click' and 'inout' events
  global win
  win = Win(title='Treasure Hunter', click=on_click, inout=on_inout, op=5)
  Label(win, height=2, border=2, grow=False); grid = Frame(win, fold=cols)
  colors = ('#00F','#0F0','#F00','#0FF','#F0F','#FF0') # colors for grid cells
  for loop in range(rows*cols):
    Brick(grid, width=64, height=64, border=3, bg=colors)
  # ----------------------------------------------------------------------------
  win.label, win.grid = win[0], win[1]; win.loop()
# ------------------------------------------------------------------------------
def on_click(widget, code, mods):
  """callback function for all 'mouse click' events"""
  #print(widget, code, mods, widget.master, widget.index)
  if widget.master != win.grid or widget.index is None:
    return # nothing to do (mouse click is not on a grid cell)
  display('click', widget.index, code, mods)
  if   code == 'LMB': widget.state += 1 # increment state for left click
  elif code == 'RMB': widget.state -= 1 # decrement state for right click
  elif code == 'MMB': reset() # reset grid state for middle click
# ------------------------------------------------------------------------------
def on_inout(widget, code, mods):
  """callback function for all 'mouse in' or 'mouse out' events"""
  #print(widget, code, mods, widget.master, widget.index)
  if widget.master != win.grid or widget.index is None:
    return # nothing to do (mouse in/out is not on a grid cell)
  display('inout', widget.index, code, mods) # display event parameters
  if code == 1: widget['bg'] = '#FFF' # 'mouse in' event --> white background
  else: widget.state += 0 # 'mouse out' event --> restore background
# ------------------------------------------------------------------------------
def reset():
  """reset initial windows state"""
  rows, cols = win.grid.widgets # get size for grid of widgets
  for loop in range(rows*cols): # loop over grid cells
    row, col = loop // cols, loop % cols # get coords by Euclidian division
    win.grid[row][col].state = 0 # reset state for each cell
# ------------------------------------------------------------------------------
def display(event, index, code, mods):
  """display event parameters"""
  text = f"Event = '{event}'  Index = {index}  Code = {code}  Mods = {mods}"
  win.label['text'] = text # show event parameters on label widget
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
