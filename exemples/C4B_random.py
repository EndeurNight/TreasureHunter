# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # use Spinbox widgets to define range for random values
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(minval=0, maxval=99):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5)
  values = tuple(range(minval,maxval+1,10)) # define all values for spinboxes
  # ----------------------------------------------------------------------------
  frame = Frame(win, op=0, grow=False)
  Label(frame, text='MIN ', anchor='E', grow=False)
  Spinbox(frame, values=values, state=values[0], width=5, wrap=False)
  Label(frame, text='MAX ', anchor='E', grow=False)
  Spinbox(frame, values=values, state=values[-1], width=5, wrap=False)
  Button(win, text='RANDOM', command=on_random, grow=False)
  Label(win, font='Arial 72 bold', width=3, border=2)
  # ----------------------------------------------------------------------------
  # set friendly names for all widgets used in callbacks
  win.label, win.minspin, win.maxspin = win[2], frame[1], frame[3]
  win.min, win.max = minval, maxval; win.loop()
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  # spinbox values are strings, so the first step is to convert them to integers
  minval, maxval = int(win.minspin.state), int(win.maxspin.state)
  if maxval < win.min: minval = win.minspin.state = maxval # copy max to min
  if minval > win.max: maxval = win.maxspin.state = minval # copy min to max
  win.min, win.max = minval, maxval # store new range for random generator
  win.label['text'] = rr(win.min, win.max+1) # display new random value on label
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
