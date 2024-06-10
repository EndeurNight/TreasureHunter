# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # use sub-frames to get 2D packing
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  font1, font2 = 'Arial 14', 'Arial 32 bold' # define fonts used for widgets
  win = Win(title='FRAME', font=font1, op=2) # main window default flow='SE'
  # ----------------------------------------------------------------------------
  Button(win, text='OOOOOO', grow=False)
  # ----------------------------------------------------------------------------
  frame = Frame(win) # inner Frame with default flow='ES' (orthogonal flow)
  Button(frame, text='XXX\nXXX', grow=False)
  Button(frame, font=font2, text='YYY\nYYY') # use specific font for widget
  Button(frame, text='ZZZ\nZZZ', grow=False)
  # ----------------------------------------------------------------------------
  Button(win, text='IIIIII', grow=False)
  # ----------------------------------------------------------------------------
  #properties()
  win.loop()
# ------------------------------------------------------------------------------
def properties():
  """view and edit some widget properties"""
  print(f"Number of widgets for main window = {win.widgets}")
  print(f"Number of widgets for inner frame = {win[1].widgets}")
  text = win[0]['text']; print(f"Text for win[0] = {text!r}")
  text = win[2]['text']; print(f"Text for win[2] = {text!r}")
  text = win[1][0]['text']; print(f"Text for win[1][0] = {text!r}")
  text = win[1][2]['text']; print(f"Text for win[1][2] = {text!r}")
  # ----------------------------------------------------------------------------
  win[1][1]['text'] = '\u2660\u2663\u2665\u2666' # edit widget property
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
