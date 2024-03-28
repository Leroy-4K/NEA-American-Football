import pygame, sys
from pygame.locals import QUIT
from set_up import *
from set_up2 import *
import nfl_data_py as nfl_data
## Attempt to fix the data
warnings.filterwarnings("ignore")
global viewing_team
### Sorting for viewing free agents #####
viewing_team = teems_arr[0] 
free_agency_age = [20,50]
free_agency_pos = "None"
free_agency_range = [0,100]
########################
while True:
  events = pygame.event.get()
  for event in events:
    current_menu = home_menu.get_current()
    menu = current_menu.get_title()
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  if home_menu.is_enabled():
    home_menu.update(events)
    home_menu.draw(surface)

    if (home_menu.get_current().get_selected_widget()):
      arrow.draw(surface, home_menu.get_current().get_selected_widget())
  pygame.display.update()