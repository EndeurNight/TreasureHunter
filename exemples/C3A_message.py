# ==============================================================================
"""MESSAGE : demo program for simple callback functions"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # use specific callback function for each button
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  font1, font2 = 'Arial 14', 'Arial 18 bold'
  win = Win(title='MESSAGE', font=font2, op=5, grow=False)
  # ----------------------------------------------------------------------------
  text, fg, bg = 'Try to find the correct button', '#FFF', '#00F'
  Label(win, text=text, fg=fg, bg=bg, width=25, height=2, border=2)
  # ----------------------------------------------------------------------------
  frame = Frame(win, font=font1)
  Button(frame, text='AAA', command=on_AAA)
  Button(frame, text='BBB', command=on_BBB)
  Button(frame, text='CCC', command=on_CCC)
  # ----------------------------------------------------------------------------
  win.label = win[0] # set friendly names for all widgets used in callbacks
  win.loop()
# ------------------------------------------------------------------------------
def on_AAA():
  """callback function for button AAA"""
  win.label['text'],win.label['fg'],win.label['bg'] = 'RETRY','#FFF','#F70'
# ------------------------------------------------------------------------------
def on_BBB():
  """callback function for button BBB"""
  win.label['text'],win.label['fg'],win.label['bg'] = 'YOU WIN !','#000','#0F0'
# ------------------------------------------------------------------------------
def on_CCC():
  """callback function for button CCC"""
  win.label['text'],win.label['fg'],win.label['bg'] = 'GAME OVER','#FFF','#F00'
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
