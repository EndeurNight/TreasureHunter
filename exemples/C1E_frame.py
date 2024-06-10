# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "5.0" # complex packing by using several levels of sub-frames
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='FRAME', font='Arial 14', op=2) # default flow='SE'
  # ----------------------------------------------------------------------------
  fr1 = Frame(win, grow=False) # flow='ES' (orthogonal flow)
  Button(fr1, text='III', grow=False)
  Label(fr1, text='OOOOOO', border=2)
  Button(fr1, text='III', grow=False)
  # ----------------------------------------------------------------------------
  fr2 = Frame(win) # flow='ES' (orthogonal flow)
  Label(fr2, text='A\nB\nC\nD\nE', grow=False)
  fr3 = Frame(fr2, border=4, op=5) # flow='SE' (orthogonal flow again)
  Label(fr3, text='ZZZ\nZZZ', border=2)
  fr4 = Frame(fr3, op=0, grow=False) # flow='ES' (orthogonal flow again)
  Button(fr4, text='XXX\nXXX')
  Button(fr4, text='YYY\nYYY')
  Label(fr2, text='A\nB\nC\nD\nE', grow=False)
  # ----------------------------------------------------------------------------
  # Each widget can be accessed starting at any level of its parent hierarchy
  #win[0][2]['bg'], fr1[0]['bg'] = '#AFA','#FAA'
  #fr3[0]['bg'], fr3[1][0]['bg'], fr4[1]['bg'] = '#FFA','#FAA','#AFA'
  # ----------------------------------------------------------------------------
  win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
