# ==============================================================================
"""EVENT : demo program for keyboard and mouse event handlers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # check keyboard events (key)
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  # create window and set global callback for 'key' event
  global win; win = Win(title='EVENT', op=3, key=on_key)
  Label(win, font='Arial 14', height=2, width=50, border=2, grow=False)
  Label(win, font='Arial 48 bold', bg='#00F', fg='#FFF', border=2)
  # ----------------------------------------------------------------------------
  win.label, win.char = win[0], win[1]; win.loop()
# ------------------------------------------------------------------------------
def on_key(widget, code, mods):
  """callback function for all 'key' events"""
  # Hint: len(code) == 1 means printable character
  win.char['text'] = code if len(code) == 1 else ''
  display('key', code, mods)
# ------------------------------------------------------------------------------
def display(event, code, mods):
  """display event parameters"""
  text = f"Event = '{event}'  Code = '{code}'  Mods = {mods}"
  win.label['text'] = text # show event parameters on label widget
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
