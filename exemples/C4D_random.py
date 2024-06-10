# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # use Menu widget to define range for random values
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def main(minval=0, maxval=99):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5)
  values = tuple(range(minval,maxval+1,10)) # define boundary values for range
  # ----------------------------------------------------------------------------
  win.master['menu'] = menu = Menu(win.master) # create master menu bar
  menu.add_command(label='EXIT', command=win.exit) # create command menu
  # ----------------------------------------------------------------------------
  minmenu = Menu(menu, tearoff=False) # create new menu to store min values
  menu.add_cascade(label='MIN', menu=minmenu) # add menu to menubar as cascade
  minmenu.state = StringVar(win, value=values[0]) # set initial min value
  for val in values: # insert all possible min values as radiobutton items
    minmenu.add_radiobutton(label=val, var=minmenu.state, command=on_menu)
  # ----------------------------------------------------------------------------
  maxmenu = Menu(menu, tearoff=False) # create new menu to store max values
  menu.add_cascade(label='MAX', menu=maxmenu) # add menu to menubar as cascade
  maxmenu.state = StringVar(win, value=values[-1]) # set initial max value
  for val in values: # insert all possible max values as radiobutton items
    maxmenu.add_radiobutton(label=val, var=maxmenu.state, command=on_menu)
  # ----------------------------------------------------------------------------
  Button(win, text='RANDOM', command=on_random, grow=False)
  win.label = Label(win, font='Arial 72 bold', width=3, border=2)
  # ----------------------------------------------------------------------------
  win.minmenu, win.maxmenu = minmenu, maxmenu
  win.min, win.max = minval, maxval; win.loop()
# ------------------------------------------------------------------------------
def on_menu():
  """callback function for all menu radiobuttons"""
  # radiobutton items are strings, so first converted them to integers
  minval, maxval = int(win.minmenu.state.get()), int(win.maxmenu.state.get())
  if maxval < win.min: minval = maxval; win.minmenu.state.set(maxval)
  if minval > win.max: maxval = minval; win.maxmenu.state.set(minval)
  win.min, win.max = minval, maxval # store new range for random generator
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  win.label['text'] = rr(win.min, win.max+1) # display new random value on label
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
