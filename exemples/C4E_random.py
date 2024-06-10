# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # store random values in a scrollable listbox
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
  frame1 = Frame(win, op=0, grow=False)
  Label(frame1, text='Enter min,max : ', grow=False)
  Entry(frame1, width=10, command=on_entry)
  frame2 = Frame(win, op=0, grow=False)
  Button(frame2, text='RANDOM', command=on_random)
  Button(frame2, text='DELETE', command=on_delete)
  Listbox(win, width=30, height=15, scroll=True, grow=True)
  # ----------------------------------------------------------------------------
  win.entry, win.box = frame1[1], win[2] # friendly names
  win.min, win.max = minval, maxval; on_entry(); win.loop()
# ------------------------------------------------------------------------------
def on_entry():
  """callback function for the 'min,max' entry"""
  try: # try to parse the entry string as a couple of integer vals
    minval, maxval = win.entry.state.split(',')
    minval, maxval = int(minval), int(maxval)
    win.min, win.max = min(minval, maxval), max(minval, maxval)
  except Exception:
    pass # keep previous values if the parsing fails
  win.entry.state = f"{win.min}, {win.max}"
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  on_entry() # reparse the entry string as user may forget to hit 'ENTER'
  values = [str(rr(win.min,win.max+1)) for loop in range(len(win.box)+1)]
  win.box.append(' '.join(values)) # append new values as a single line
  #win.box('\n'.join(values)) # replace box content with new values
# ----------------------------------------------------------------------------
def on_delete():
  """callback function for the 'DELETE' button"""
  del win.box[-1] # delete last line
  #del win.box[:]  # delete all lines    
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
