from ezTK import *
from random import *

def JeuGui(lig, col, tresors, level, partyconfig) :
    #lig = lignes
    #col = colonnes
    #tresors = tresors
    #level = config de la partie (1, 2, 3, 4)

    windows_title = "Treasure Hunter - Mode de jeu inconnu"

    if level == 1 : 
        windows_title = "Treasure Hunter - Facile"
    elif level == 2 :
        windows_title = "Treasure Hunter - Moyen"
    elif level == 3 :
        windows_title = "Treasure Hunter - Difficile"
    elif level == 4 :
        windows_title = "Treasure Hunter - Configuration personnalisée"

    ############
    #Tirage au sort des trésors
    #case est une liste de tuples (x, y) qui contient les coordonnées des trésors
    cases = []
    while len(cases) < tresors :
        x = randint(0, lig-1)
        y = randint(0, col-1)
        if (x, y) not in cases :
            cases.append((x, y))

    print(str(tresors)+ " trésors ont été placés aux coordonnées suivantes : " + str(cases))

    """create the main window and pack the widgets"""
    # create window and set global callbacks for 'click' and 'inout' events
    global win
    win = Win(title=windows_title, click=on_click, inout=on_inout, op=4) #op = largeur entre les widgets
    scoreb = Label(win, text="Joueur en cours : ", width=10, height=2, border=2, grow=True)
    


    grid = Frame(win, fold=col)
    colors = ("#00F", "#0F0", "#F00", "#0FF", "#F0F", "#FF0") # colors for grid cells
    for loop in range(lig*col):
        #Brick(grid, width=64, height=64, border=3, bg=colors)
        Label(grid, width=64, height=64, border=1, bg=colors, text=str(loop))
        # ----------------------------------------------------------------------------
    win.label, win.grid = win[0], win[1] ; win.loop()
    
    


def on_click(widget, code, mods):#
  """callback function for all 'mouse click' events"""
  #print(widget, code, mods, widget.master, widget.index)
  if widget.master != win.grid or widget.index is None:
    return # nothing to do (mouse click is not on a grid cell)
  display('click', widget.index, code, mods)
  if   code == 'LMB': widget.state += 1 # increment state for left click
  elif code == 'RMB': widget.state -= 1 # decrement state for right click
  elif code == 'MMB': reset() # reset grid state for middle click


# ------------------------------------------------------------------------------
def on_inout(widget, code, mods):
  """callback function for all 'mouse in' or 'mouse out' events"""
  #print(widget, code, mods, widget.master, widget.index)
  if widget.master != win.grid or widget.index is None:
    return # nothing to do (mouse in/out is not on a grid cell)
  display('inout', widget.index, code, mods) # display event parameters
  if code == 1: widget['bg'] = '#FFF' # 'mouse in' event --> white background
  else: widget.state += 0 # 'mouse out' event --> restore background


# ------------------------------------------------------------------------------
def reset():
  """reset initial windows state"""
  rows, cols = win.grid.widgets # get size for grid of widgets
  for loop in range(rows*cols): # loop over grid cells
    row, col = loop // cols, loop % cols # get coords by Euclidian division
    win.grid[row][col].state = 0 # reset state for each cell
# ------------------------------------------------------------------------------


def display(event, index, code, mods):
  """display event parameters"""
  text = f"Event = '{event}'  Index = {index}  Code = {code}  Mods = {mods}"

  win.label['text'] = text # show event parameters on label widget


# ==============================================================================
if __name__ == '__main__':
  JeuGui(5, 5, 12, 3, 1)
# ==============================================================================
