# ==============================================================================
"""EVENT : demo program for keyboard and mouse event handlers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # check mouse events (move)
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  # create window and set global callback for 'move' event
  global win; win = Win(title='EVENT', op=5, move=on_move)
  Label(win, height=2, border=2, grow=False)
  Brick(win, width=1000, height=500, bg='#00F', border=2)
  # ----------------------------------------------------------------------------
  win.label, win.brick = win[0], win[1]; win.loop()
# ------------------------------------------------------------------------------
def on_move(widget, code, mods):
  """callback function for all 'mouse move' events"""
  # display event parameters, only when 'win.brick' is the active widget
  if widget == win.brick: display('move', code, mods)
# ------------------------------------------------------------------------------
def display(event, code, mods):
  """display event parameters"""
  text = f"Event = '{event}'  Code = {code}  Mods = {mods}"
  win.label['text'] = text # show event parameters on label widget
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
