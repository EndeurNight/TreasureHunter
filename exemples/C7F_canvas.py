# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "6.0" # draw lines and disks according to mouse position
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import choice
# ------------------------------------------------------------------------------
def main(dim=400):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='CANVAS', click=on_click, op=2, grow=False)
  win.canvas = Canvas(win, width=2*dim, height=2*dim)
  win.canvas.create_oval(dim-20, dim-20, dim+20, dim+20, fill='#000')
  win.x = win.y = dim; win.loop() # set initial position and start event loop
# ------------------------------------------------------------------------------
def on_click(widget, code, mods):
  """callback function for all 'mouse click' events"""
  if widget != win.canvas: return # mouse click is not on canvas
  # get current mouse position, relative to top left corner of canvas
  x = widget.winfo_pointerx() - widget.winfo_rootx()
  y = widget.winfo_pointery() - widget.winfo_rooty()
  widths, colors = (1,3,5,7,9), ('#F00','#0F0','#00F','#0FF','#F0F','#FF0')
  # create line between previous and current mouse position (use random width)
  line = win.canvas.create_line(win.x, win.y, x, y, width=choice(widths))
  widget.tag_lower(line) # put new line UNDER all existing items
  # create oval centered at current mouse position (use random fill color)
  oval = win.canvas.create_oval(x-20, y-20, x+20, y+20, fill=choice(colors)) 
  widget.tag_raise(oval) # put new oval OVER all existing items
  win.x, win.y = x, y # store current coordinates for next click
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
