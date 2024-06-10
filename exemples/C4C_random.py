# ==============================================================================
"""RANDOM : generate random vals within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # use Entry widget to define range for random values
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(minval=0, maxval=99):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5)
  # ----------------------------------------------------------------------------
  frame = Frame(win, op=0, grow=False)
  Label(frame, text='Enter min,max : ', grow=False)
  Entry(frame, width=10, command=on_entry)
  Button(win, text='RANDOM', command=on_random, grow=False)
  Label(win, font='Arial 72 bold', width=3, border=2)
  # ----------------------------------------------------------------------------
  win.label, win.entry = win[2], frame[1] # friendly names
  win.min, win.max = minval, maxval; on_entry(); win.loop()
# ------------------------------------------------------------------------------
def on_entry():
  """callback function for the 'min,max' entry"""
  try: # try to parse the entry string as a couple of integer vals
    minval, maxval = win.entry.state.split(',') # get current min/max values
    minval, maxval = int(minval), int(maxval) # convert to integer
    win.min, win.max = min(minval,maxval), max(minval,maxval) # swap if needed
  except Exception:
    pass # keep previous values if the parsing fails
  win.entry.state = f"{win.min}, {win.max}"
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  on_entry() # reparse the entry string as user may forget to hit 'ENTER'
  win.label['text'] = rr(win.min, win.max+1) # display new random value on label
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
