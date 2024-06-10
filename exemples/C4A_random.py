# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # use Scale widgets to define range for random values
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(minval=0, maxval=99):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5); scale = (minval, maxval)
  # ----------------------------------------------------------------------------
  frame = Frame(win, op=0, grow=False)
  Label(frame, text='MIN :', anchor='SE', grow=False)
  Scale(frame, scale=scale, state=minval, command=on_scale)
  Label(frame, text='MAX :', anchor='SE', grow=False)
  Scale(frame, scale=scale, state=maxval, command=on_scale)
  Button(win, text='RANDOM', command=on_random, grow=False)
  Label(win, font='Arial 72 bold', width=3, border=2)
  # ----------------------------------------------------------------------------
  # set friendly names for all widgets used in callbacks
  win.label, win.minscale, win.maxscale = win[2], frame[1], frame[3]
  win.min, win.max = minval, maxval; win.loop()
# ------------------------------------------------------------------------------
def on_scale():
  """callback function for both 'MIN' and 'MAX' scales"""
  minval, maxval = win.minscale.state, win.maxscale.state # get scale values
  if maxval < win.min: minval = win.minscale.state = maxval # copy max to min
  if minval > win.max: maxval = win.maxscale.state = minval # copy min to max
  win.min, win.max = minval, maxval # store new range for random generator
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  win.label['text'] = rr(win.min, win.max+1) # display new random value on label
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
