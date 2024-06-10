# ==============================================================================
"""WIN : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # demo for some standard dialog windows
__date__    = "2021-03-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  win = Win(title='DIALOG', fold=4, op=2, grow=False)
  # ----------------------------------------------------------------------------
  Button(win, text='INFO', width=12, command=on_info)
  Button(win, text='WARN', width=12, command=on_warn)
  Button(win, text='ERROR', width=12, command=on_error)
  Button(win, text='CHOICE', width=12, command=on_choice)
  Button(win, text='COLOR', width=12, command=on_color)
  Button(win, text='OPEN FILE', width=12, command=on_open)
  Button(win, text='SAVE FILE', width=12, command=on_save)
  Button(win, text='POPUP', width=12, command=on_popup)
  # ----------------------------------------------------------------------------
  win.label = Label(win, text='', anchor='W', border=1) # create status line
  win.loop()
# ------------------------------------------------------------------------------
def message(text):
  """change message shown on status bar"""
  win.label['text'] = text
# ------------------------------------------------------------------------------
def on_info():
  """callback for the "INFO" button"""
  message("INFO button has been pressed")
  val = Dialog(mode='info', message='Information message', title='INFO')
  message(f"Dialog return : {val}")
# ------------------------------------------------------------------------------
def on_warn():
  """callback for the "WARN" button"""
  message("WARN button has been pressed")
  val = Dialog(mode='warning', message='Warning message', title='WARNING')
  message(f"Dialog return : {val}")
# ------------------------------------------------------------------------------
def on_error():
  """callback for the "ERROR" button"""
  message("ERROR button has been pressed")
  val = Dialog(mode='error', message='Error message', title='ERROR')
  message(f"Dialog return : {val}")
# ------------------------------------------------------------------------------
def on_choice():
  """callback for the "CHOICE" button"""
  message("CHOICE button has been pressed")
  val = Dialog(mode='choice', message='Select YES or NO', title='CHOICE')
  message(f"Dialog return : {val}")
# ------------------------------------------------------------------------------
def on_color():
  """callback for the "COLOR" button"""
  message("COLOR button has been pressed")
  val = Dialog(mode='color', title='COLOR')
  message(f"Dialog return : RGB = {val[0]} Color = {val[1]}")
# ------------------------------------------------------------------------------
def on_open():
  """callback for the "OPEN FILE" button"""
  message("OPEN FILE button has been pressed")
  val = Dialog(mode='open', title='OPEN FILE')
  message(f"Dialog return : File = {val}")
# -----------------------------------------------------------------------------
def on_save():
  """callback for the "SAVE FILE" button"""
  message("SAVE FILE button has been pressed")
  val = Dialog(mode='save', title='SAVE FILE')
  message(f"Dialog return : File = {val}")
# ------------------------------------------------------------------------------
def on_popup():
  """callback for the "POPUP" button"""
  message("POPUP button has been pressed")
  popup = Win(win, title='POPUP', op=10) # create popup window
  text = 'This is a modal window\n\nPlease close it to continue'
  Label(popup, text=text); popup.wait() # wait for popup window to be closed
  message("POPUP window has been closed")
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
