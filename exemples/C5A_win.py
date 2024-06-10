# ==============================================================================
"""WIN : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # dynamic creation and destruction of windows 
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
# Note: three different kinds of windows may be created by calling Win(...):
# - a MASTER window, when the first argument of Win(...) is None
# - a SLAVE window, when the first argument represents an existing window
# - a MODAL window, is a special type of SLAVE window that blocks all events
#   of its MASTER window until the MODAL window is closed
# ------------------------------------------------------------------------------
def window(master=None, modal=False):
  """create a new window (either master, slave, modal)"""
  global counter
  counter +=1; win = Win(master, title=counter, op=2)
  # use specific 'text' and 'bg' according to window type (master, slave, modal)
  if master is None: text, bg = 'MASTER', '#0F0'
  elif modal: text, bg = f"MODAL of window {master.title}", '#F00'
  else: text, bg = f"SLAVE of window {master.title}", '#FF0'
  Label(win, text=text, bg=bg, border=2, height=2)
  Button(win, text='Create master window', command=lambda: window())
  Button(win, text='Create slave window',  command=lambda: window(win))
  Button(win, text='Create modal window',  command=lambda: window(win, True))
  Button(win, text='Kill me and all my slaves', command=win.exit)
  # modal window (= blocking window) requires win.wait() instead of win.loop()
  win.wait() if modal else win.loop()
# ==============================================================================
if __name__ == "__main__":
  counter = 0 # 'counter' is a global variable used for windows numbering
  window() # create window with default arguments (= master window)
# ==============================================================================
