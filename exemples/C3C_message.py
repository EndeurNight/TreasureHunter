# ==============================================================================
"""MESSAGE : demo program for simple callback functions"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # use a multi-state Label widget
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
  # define multi-state values for 'text', 'bg' and 'fg' properties
  text = ('Try to find the correct button','RETRY','YOU WIN !','GAME OVER')
  fg, bg = ('#FFF','#FFF','#000','#FFF'), ('#00F','#F70','#0F0','#F00')
  Label(win, text=text, fg=fg, bg=bg, width=25, height=2, border=2)
  # ----------------------------------------------------------------------------
  frame = Frame(win, font=font1)
  Button(frame, text='AAA', command=lambda: on_button(1)) # set state to 1
  Button(frame, text='BBB', command=lambda: on_button(2)) # set state to 2
  Button(frame, text='CCC', command=lambda: on_button(3)) # set state to 3
  # ----------------------------------------------------------------------------
  win.label = win[0] # set friendly names for all widgets used in callbacks
  win.loop()
# ------------------------------------------------------------------------------
def on_button(state):
  """generic callback function for all three buttons"""
  win.label.state = state
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
