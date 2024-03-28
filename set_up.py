from schedule import *
from teams import *
from players import *
from league import *
from menu import *
from game import *
from names import *
from text import *
from button import *
from standings import *
from pygame_menu import sound
import warnings


import sys
import random
import os
import time
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


game = Game()
nfl = League()

nfl.generate_league_teams()

t = 0

### Generate League ###
t = nfl.generate_league_players(t)

#### Gen free agnets

t = nfl.create_free_agency(t)
t = nfl.gen_draft(t)

NFC = Conference(nfl.teams[0], nfl.teams[1], nfl.teams[2], nfl.teams[3], nfl.teams[4], nfl.teams[5], nfl.teams[6], nfl.teams[7], nfl.teams[8], nfl.teams[9], nfl.teams[10], nfl.teams[11], nfl.teams[12], nfl.teams[13], nfl.teams[14], nfl.teams[15])

AFC = Conference(nfl.teams[16], nfl.teams[17], nfl.teams[18], nfl.teams[19], nfl.teams[20], nfl.teams[21], nfl.teams[22], nfl.teams[23], nfl.teams[24], nfl.teams[25], nfl.teams[26], nfl.teams[27], nfl.teams[28], nfl.teams[29], nfl.teams[30], nfl.teams[31])


NFC_SOUTH = Division(NFC.team1, NFC.team2, NFC.team3, NFC.team4, "NFC", "NFC South")
NFC_WEST = Division(NFC.team5, NFC.team6, NFC.team7, NFC.team8, "NFC", "NFC West")
NFC_NORTH = Division(NFC.team9, NFC.team10, NFC.team11, NFC.team12, "NFC", "NFC North")
NFC_EAST = Division(NFC.team13, NFC.team14, NFC.team15, NFC.team16, "NFC", "NFC East")

NFC.div1 = NFC_SOUTH
NFC.div2 = NFC_WEST
NFC.div3 = NFC_NORTH
NFC.div4 = NFC_EAST

AFC_SOUTH = Division(AFC.team1, AFC.team2, AFC.team3, AFC.team4, "AFC", "AFC South")
AFC_WEST = Division(AFC.team5, AFC.team6, AFC.team7, AFC.team8, "AFC", "AFC West")
AFC_NORTH = Division(AFC.team9, AFC.team10, AFC.team11, AFC.team12, "AFC", "AFC North")
AFC_EAST = Division(AFC.team13, AFC.team14, AFC.team15, AFC.team16, "AFC", "AFC East")

AFC.div1 = AFC_SOUTH
AFC.div2 = AFC_WEST
AFC.div3 = AFC_NORTH
AFC.div4 = AFC_EAST

all_divs = [NFC_SOUTH, NFC_WEST, NFC_NORTH, NFC_EAST, AFC_SOUTH, AFC_WEST, AFC_NORTH, AFC_EAST]
for i in range(len(all_divs)):
  all_divs[i].set_div()

teams = nfl.teams
for i in range(len(nfl.all_players)):
  nfl.all_players[i].retire()
random.shuffle(teams)
for i in range(len(teams)):
  n = i
  while n <= 224:
    
    teams[i].draft_picks_this_year.append(n)
    n += 32

user_team = nfl.nfc_south[3]
viewing_team = nfl.nfc_south[3]

reverse_win_order = nfl.teams
random.shuffle(reverse_win_order)
print(len(reverse_win_order))
draft_pick = (reverse_win_order.index(user_team) + 1) % 32
if draft_pick != 0:
  print(reverse_win_order[draft_pick - 1].name)
  print(draft_pick, draft_pick -1)
import pygame
import pygame_menu 
from pygame_menu import themes
from pygame.locals import QUIT
year = 2023
week = ["Offseason", "Resigning", "Free agency", "Draft", "Training Camp", "Preseason 1", "Preseason 2",  "Preseason 3", "Preseason 4", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16", "Week 17", "Week 18", "Wildcard Round", "Divisional Round", "Conference Championship", "Super Bowl", "End of Year"]

wk = 0
menu = "Home"
start = 9
late = 17
playoff = 27

pygame.init()
########### Change l and w ##############
l = 700
w = 550
surface = pygame.display.set_mode((l, w))
print("Surface made")
pygame.display.set_caption('American Football Game')
menu = "Home"
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10,15))
#pygame_menu.sound.Sound = lambda *args, **kwargs: None
warnings.filterwarnings("ignore", message="sound error: dsp: No such audio device")

home_menu = pygame_menu.Menu("Home", l, w, theme=themes.THEME_GREEN)


### Menus ###

menu_settings = pygame_menu.Menu("Settings", l, w, theme=themes.THEME_GREEN)

menu_off = pygame_menu.Menu("Offseason", l, w, theme=themes.THEME_GREEN)

off_week_text = menu_off.add.label(week[wk] + " - " + str(year), max_char=-1, font_size=20)

menu_early = pygame_menu.Menu("Early Season", l, w, theme=themes.THEME_GREEN)

early_week_text = menu_early.add.label(week[wk] + " - " + str(year), max_char=-1, font_size=20)

menu_late = pygame_menu.Menu("Late Season", l, w, theme=themes.THEME_GREEN)

late_week_text = menu_late.add.label(week[wk] + " - " + str(year), max_char=-1, font_size=20)

menu_playoffs = pygame_menu.Menu("Playoffs", l, w, theme=themes.THEME_GREEN)

playoff_week_text = menu_playoffs.add.label(week[wk] + " - " + str(year), max_char=-1, font_size=20)

### Sub menus ###
menu_resign = pygame_menu.Menu("Re-sign", l, w, theme=themes.THEME_GREEN)

menu_last_weeks_results = pygame_menu.Menu("Last Week's Results", l, w, theme=themes.THEME_GREEN)

menu_draft = pygame_menu.Menu("Draft", l, w, theme=themes.THEME_GREEN)

menu_trade = pygame_menu.Menu("Trade", l, w, theme=themes.THEME_GREEN)

menu_game_play_by_play = pygame_menu.Menu("Game Play by Play", l, w, theme=themes.THEME_GREEN)

menu_your_schedule = pygame_menu.Menu("Schedule", l, w, theme=themes.THEME_GREEN)

menu_week_games = pygame_menu.Menu("Weekly Games", l, w, theme=themes.THEME_GREEN)

menu_free_agency = pygame_menu.Menu("Free Agency", l, w, theme=themes.THEME_GREEN)

menu_view_your_team = pygame_menu.Menu("View Your Team", l, w, theme=themes.THEME_GREEN)

menu_view_another_team = pygame_menu.Menu("View Another Team", l, w, theme=themes.THEME_GREEN)

menu_view_team_stats = pygame_menu.Menu("View Team Stats", l, w, theme=themes.THEME_GREEN)

menu_info = pygame_menu.Menu("INFO", l, w, theme=themes.THEME_GREEN)

menu_awards = pygame_menu.Menu("Awards", l, w, theme=themes.THEME_GREEN)

menu_weekly_awards = pygame_menu.Menu("Weekly Awards", l, w, theme=themes.THEME_GREEN)

menu_team_stats = pygame_menu.Menu("Team Stats", l, w, theme=themes.THEME_GREEN)

menu_training = pygame_menu.Menu("Training", l, w, theme=themes.THEME_GREEN)

#menu_coaches = pygame_menu.Menu("Coaches", l, w, theme=themes.THEME_GREEN)

menu_standings = pygame_menu.Menu("Standings", l, w, theme=themes.THEME_GREEN)

menu_div_standings = pygame_menu.Menu("Division Standings", l, w, theme=themes.THEME_GREEN)

menu_conf_standings = pygame_menu.Menu("Conference Standings", l, w, theme=themes.THEME_GREEN)

menu_player_career_stats = pygame_menu.Menu("Career Stats", l, w, theme=themes.THEME_GREEN)

menu_free_agency_choice = pygame_menu.Menu("Free Agency Options", l, w, theme=themes.THEME_GREEN)

free_agency_range = [0,100]
free_agency_pos = "None"
free_agency_age = [20,50]
def free_agency_opt(value):
  global free_agency_range
  free_agency_range = [value[0], value[1]]

def free_agency_opt2(value):
  global free_agency_pos
  free_agency_pos = value

def free_agency_opt3(value):
  global free_agency_age
  free_agency_age = value

def return_free_age():
  global free_agency_age
  return free_agency_age

def return_free_pos():
  global free_agency_pos
  return free_agency_pos

def return_free_range():
  global free_agency_range
  return free_agency_range

def go_free_agency():
  menu_free_agency.clear(False)
  nfl.sort_free()
  free_agency_pos = return_free_pos()
  free_agency_range = return_free_range()
  free_agency_age = return_free_age()
  free_agency_list = []
  for e in range(len(nfl.free_agents)):
    nfl.free_agents[e].cal_ovr()
    if nfl.free_agents[e].ovr >= free_agency_range[0] and nfl.free_agents[e].ovr <= free_agency_range[1] and nfl.free_agents[e].pos == free_agency_pos and nfl.free_agents[e].age >= free_agency_age[0] and nfl.free_agents[e].age <= free_agency_age[1]:
      free_agency_list.append(nfl.free_agents[e])
  if free_agency_pos == "None":
    fr_list = nfl.free_agents
    for x in range(len(fr_list)):
      if fr_list[x].ovr >= free_agency_range[0] and fr_list[x].ovr <= free_agency_range[1] and fr_list[x].age >= free_agency_age[0] and fr_list[x].age <= free_agency_age[1]:
        free_agency_list.append(fr_list[x]) 
  idk = 0
  if idk + 30 > len(free_agency_list):
    idek = len(free_agency_list)
  else:
    idek = idk + 30
  for i in range(idk, idek):
    fr_ag = menu_free_agency.add.button(free_agency_list[i].name + ": " + free_agency_list[i].pos + ": " + str(free_agency_list[i].ovr), go_player_card, free_agency_list[i], menu_free_agency)
  if idek == 0:
    menu_free_agency.add.label("No Free Agents", max_char=-1, font_size=20)
  menu_free_agency_choice._open(menu_free_agency)

ovrs = []
for i in range(0,11):
  ovrs.append(i*10)
ages = []
for i in range(3, 11):
  ages.append(i*5)

selector2 = menu_free_agency_choice.add.range_slider('Pick a range of OVR', (0, 100), ovrs, 1, onchange=lambda value: [free_agency_opt(value)], font_size =15)

selector3 = menu_free_agency_choice.add.range_slider('Pick a range of ages', (20, 50), ages, 1, onchange=lambda value: [free_agency_opt3(value)], font_size =15)

pos = ["None", "QB", "RB", "WR", "TE", "T", "G", "C", "DE", "DT", "MLB", "OLB", "CB", "S", "K", "P"]
poses = []
for i in range(len(pos)):
  poses.append((pos[i], pos[i]))
selector_epic = menu_free_agency_choice.add.dropselect(
    title='Pick A Position',
    items=poses,
    font_size=16,
    selection_option_font_size=20,
    onchange=lambda selected, value: [free_agency_opt2(value)]
)

menu_free_agency_choice.add.button("Confirm", go_free_agency)

######

menu_player_card = pygame_menu.Menu("Player Card", l, w, theme=themes.THEME_GREEN)

########## Newer ones

menu_choose_another_team = pygame_menu.Menu("Pick Another Team", l, w, theme=themes.THEME_GREEN)

teems = nfl.teams
teems = sorted(teems, key=lambda team: team.name)
teems_arr = []
for i in range(len(teems)):
  teems_arr.append((teems[i].name, teems[i]))
def open_team_choice(value, team):
  global viewing_team
  viewing_team = team

def return_viewing_team():
  return viewing_team
  
def go_view_that_team():
  menu_view_another_team.clear(False)
  viewing_team = return_viewing_team()
  menu_view_another_team.add.label("Cap space used: " +str(viewing_team.salaries), font_size=20)
  #print(test_number)
  test_text = viewing_team.name
  menu_view_another_team.add.label(test_text, max_char=-1, font_size=20)
  menu_view_another_team.add.button("View Team Stats", go_team_stats, viewing_team, menu_view_another_team, font_size = 20)
  viewing_team.all_players()
  for i in range(len(viewing_team.players)):
    for player in range(len(viewing_team.players[i])):
      viewing_team.players[i][player].cal_ovr()
      menu_view_another_team.add.button(viewing_team.players[i][player].name + ": " + viewing_team.players[i][player].pos + ": " + str(viewing_team.players[i][player].ovr), go_player_card, viewing_team.players[i][player], menu_view_another_team)
  menu_choose_another_team._open(menu_view_another_team)
  
  
selector1 = menu_choose_another_team.add.selector(
    title='Team:',
    items=teems_arr,
    style=pygame_menu.widgets.SELECTOR_STYLE_FANCY,
    onreturn= lambda selected, value: [open_team_choice(selected, value), go_view_that_team()], # User press "Return" button
    onchange=None,  # User changes value with left/right keys
    font_color = (132, 123, 213)
)

menu_info.add.label("MIN PLAYERS FOR EACH POS", max_char=-1, font_size=20)
menu_info.add.label("QB: 1", max_char=-1, font_size=20)
menu_info.add.label("RB: 1", max_char=-1, font_size=20)
menu_info.add.label("WR: 3", max_char=-1, font_size=20)
menu_info.add.label("TE: 1", max_char=-1, font_size=20)
menu_info.add.label("C: 1", max_char=-1, font_size=20)
menu_info.add.label("G: 2", max_char=-1, font_size=20)
menu_info.add.label("T: 2", max_char=-1, font_size=20)
menu_info.add.label("DE: 2", max_char=-1, font_size=20)
menu_info.add.label("DT: 2", max_char=-1, font_size=20)
menu_info.add.label("OLB: 2", max_char=-1, font_size=20)
menu_info.add.label("MLB: 2", max_char=-1, font_size=20)
menu_info.add.label("CB: 2", max_char=-1, font_size=20)
menu_info.add.label("S: 2", max_char=-1, font_size=20)
menu_info.add.label("K: 2", max_char=-1, font_size=20)
menu_info.add.label("P: 2", max_char=-1, font_size=20)
menu_info.add.label("""
""", max_char=-1, font_size=20)

menu_info.add.label("Cap limit: $200,000,000", max_char=-1, font_size=20)
menu_info.add.label("You can have a maximum of 53 players once the season starts", max_char=-1, font_size=20)
menu_info.add.label("""
""", max_char=-1, font_size=20)
menu_info.add.label("PLAYOFFS", max_char=-1, font_size=20)
menu_info.add.label("Top 4 teams are division winners", max_char=-1, font_size=20)
menu_info.add.label("The No.1 seed gets a first round bye", max_char=-1, font_size=20)
menu_info.add.label("The higher seeded team has home field advantage", max_char=-1, font_size=20)



menu_choose_conf = pygame_menu.Menu("Pick Conference", l, w, theme=themes.THEME_GREEN)

menu_afc_standings = pygame_menu.Menu("AFC standings", l, w, theme=themes.THEME_GREEN)

menu_nfc_standings = pygame_menu.Menu("NFC standings", l, w, theme=themes.THEME_GREEN)

menu_players_leaving = pygame_menu.Menu("Players Leaving", l, w, theme=themes.THEME_GREEN)


### Menu Functions ###

def clear(menu):
  tot = list(menu.get_widgets())
  for i in range(len(tot)):
    menu_view_another_team.remove_widget(tot[i])

####

def go_from_main_menu(next_menu):
  if wk < start:
    menu_off._open(next_menu)
  elif wk < late:
    menu_early._open(next_menu)
  elif wk < playoff:
    menu_late._open(next_menu)
  else:
    menu_playoffs._open(next_menu)

def go_to_game_menu():
  if wk < start:
    home_menu._open(menu_off)

  elif wk < late:
    home_menu._open(menu_early)

  elif wk < playoff:
    home_menu._open(menu_late)
  else:
    home_menu._open(menu_playoffs)

def go_to_nfc_standings():
  menu_nfc_standings.clear(False)
  update_conf()
  nfc_conf_standings()
  menu_choose_conf._open(menu_nfc_standings)

def go_to_afc_standings():
  menu_afc_standings.clear(False)
  update_conf()
  afc_conf_standings()
  menu_choose_conf._open(menu_afc_standings)

def menu_conf(prev):
  prev._open(menu_choose_conf)
  

def go_draft():
  pass


def draft_to_trade():
  pass

def go_to_choose_team():
  go_from_main_menu(menu_choose_another_team)


def go_home():
  home_menu.full_reset()

def go_settings():
  home_menu._open(menu_settings)

def go_view_your_team():
  menu_view_your_team.clear(False)
  menu_view_your_team.add.label("Cap space used: " +str(user_team.salaries), font_size=20)
  menu_view_your_team.add.button("View Team Stats", go_team_stats, user_team, menu_view_your_team, font_size = 20)
  user_team.all_players()
  your_player_buttons = []
  for i in range(len(user_team.players)):
    for player in range(len(user_team.players[i])):
      user_team.players[i][player].cal_ovr()
      b = menu_view_your_team.add.button(user_team.players[i][player].name + ": " + user_team.players[i][player].pos + ": " + str(user_team.players[i][player].ovr), go_player_card, user_team.players[i][player], menu_view_your_team)
      your_player_buttons.append(b)
  go_from_main_menu(menu_view_your_team)

def select_team(prev):
  menu._open(menu_choose_another_team)

def go_stats():
  go_from_main_menu(menu_team_stats)

def go_free():
  go_from_main_menu(menu_free_agency_choice)


def go_awards():
  go_from_main_menu(menu_awards)


def go_training():
  go_from_main_menu(menu_training)

def go_info():
  home_menu._open(menu_info)

def go_coaches():
  pass


def go_standings():
  go_from_main_menu(menu_standings)

def go_div_standings():
  menu_div_standings.clear(False)
  update_div()
  weekly_standings()
  menu_standings._open(menu_div_standings)
  

def go_conf_standings():
  menu_standings._open(menu_choose_conf)
random_teams = nfl.teams
def sign(user, player, years):
  user.sign(player, nfl, player.asking_sal(), years)
  if wk == 2 or wk == 4:
    random.shuffle(random_teams)
    for i in range(len(nfl.teams)):
      if random_teams[i] != user_team:
        if random_teams[i].min_players() == False:
          random_teams[i].cpu_sign_best(nfl)
        else:
          random_teams[i].add_free_agents(nfl)
  else:
    for i in range(len(nfl.teams)):
      if random_teams[i] != user_team:
        if random.randint(0,10) <= 3:
          if random_teams[i].min_players() == False:
            random_teams[i].cpu_sign_best(nfl)
          else:
            random_teams[i].add_free_agents(nfl)
        
  home_menu.full_reset()
  go_to_game_menu()

def re_sign(user, player, years):
  user.re_sign(player, player.asking_sal(), years)
  home_menu.full_reset()
  go_to_game_menu()
#New
def cut(user, player, nfl):
  user.cut_player(player, nfl)
  home_menu.full_reset()
  go_to_game_menu()
  

def career_stats(player):
  menu_player_career_stats.clear(False)
  menu_player_career_stats.add.label("Super Bowls: " + str(player.sbs), font_size=20)
  menu_player_career_stats.add.label("Conference Champs: " + str(player.conf_champs), font_size=20)
  menu_player_career_stats.add.label("Division Titles: " + str(player.div_titles), font_size=20)
  menu_player_career_stats.add.label("Playoff Wins: " + str(player.playoff_wins), font_size=20)
  menu_player_career_stats.add.label("Exp Multiplier: " + str(round(player.exp_mult,5)), max_char=-1, font_size=20)
  menu_player_career_stats.add.label("Money made: $" + str(round(player.money,2)), font_size=20)
  menu_player_card._open(menu_player_career_stats)

def draft(player):
  pass

def go_players_leaving():
  menu_players_leaving.clear(False)
  if len(user_team.players_leaving) > 0:
    for i in range(len(user_team.players_leaving)):
      menu_players_leaving.add.button(user_team.players_leaving[i].name + " "  + str(user_team.players_leaving[i].pos) + ": " +str(user_team.players_leaving[i].ovr), go_player_card, user_team.players_leaving[i], menu_players_leaving)
  else:
    menu_players_leaving.add.label("No players leaving", font_size=20)
  menu_off._open(menu_players_leaving)

def add_player_stats(self):
  pass

def go_player_card(player, prev):
  global user_team
  size = 15
  menu_player_card.clear(False)
  prev._open(menu_player_card)
  user_team.total_players()
  player.cal_ovr()
  menu_player_card.add.label("Name: " + player.name + " Age: " + str(player.age), max_char=-1, font_size=size)
  if player.retired == True:
    menu_player_card.add.label("Retired")
  menu_player_card.add.label("Tech: " + str(round(player.tech_ovr)), max_char=-1, font_size=size)
  menu_player_card.add.label("Phy: " + str(round(player.phy_ovr)), max_char=-1, font_size=size)
  menu_player_card.add.label("Mental: " + str(round(player.mental_ovr)), max_char=-1, font_size=size)
  menu_player_card.add.label("Ovr: " + str(player.ovr), max_char = -1, font_size=size)
  menu_player_card.add.label("Morale: " + str(player.morale), max_char = -1, font_size=size)
  menu_player_card.add.label("Level: " + str(player.level) + " Next Level: " + str(player.exp) + "/" + str(player.next_level_exp), max_char = -1, font_size=size)
  player_table = menu_player_card.add.table(font_size = size)
  player_table.add_row(player.attr_names)
  player_table.add_row(player.attr)
  if player.retired == False:
    if player in nfl.free_agents:
      years = random.randint(1,6)
      menu_player_card.add.label("Asking Salary: " + str(player.asking_sal()) + " Years Wanted: " + str(years) , max_char=-1, font_size=size)
      menu_player_card.add.button("Sign", sign, user_team, player, years)
    elif player in nfl.draft_class:
      menu_player_card.add.button("Draft", draft)
    elif player in user_team.tot_players:
      if player in user_team.players_leaving:
        if player.retired == False:
          years = random.randint(1,6)
          menu_player_card.add.label("Asking Salary: " + str(player.asking_sal()) + " Years Wanted: " + str(years) , max_char=-1, font_size=20)
          menu_player_card.add.button("Re-Sign", re_sign, user_team, player, years)
        
      else:
        menu_player_card.add.label("Salary: " + str(player.yearly_salary) + " Years Left: " + str(player.contract_years), max_char=-1, font_size=size)
        menu_player_card.add.button("Cut", cut, user_team, player, nfl)
  menu_player_card.add.button("View Career Stats", career_stats, player)
  
def go_another_player_card():
  menu_player_card.clear(False)
  menu_view_another_team._open(menu_player_card)

def go_team_stats(team, prev):
  menu_view_team_stats.clear(False)
  menu_view_team_stats.add.label(team.name , max_char=-1, font_size=20)
  menu_view_team_stats.add.label("Super Bowls: " + str(team.sbs) , max_char=-1, font_size=20)
  menu_view_team_stats.add.label("Conf Champs: " + str(team.conf_champs) , max_char=-1, font_size=20)
  menu_view_team_stats.add.label("Playoff Wins: " + str(team.playoff_wins) , max_char=-1, font_size=20)
  menu_view_team_stats.add.label("Division Titles: " + str(team.div_titles) , max_char=-1, font_size=20)
  
  prev._open(menu_view_team_stats)
  
###################### new

def change_current_menu(menu1,menu2):
  pass

### Adding Buttons ###
def game_start():
  pass


home_menu.add.button("Play", go_to_game_menu)
home_menu.add.button("Settings", go_settings)
#pregame = pygame_menu.Menu("Game", None) 
#pregame.add.button("Next", game_start)
def music_on_off():
  global music
  if music.get_title() == "Music Off":
    music.set_title("Music On")
  else:
    music.set_title("Music Off")

music = home_menu.add.button("Music Off", music_on_off)
home_menu.add.button("Info", go_info)

for i in range(len(nfl.teams)):
  nfl.teams[i].players_going()

for i in range(len(nfl.all_players)):
  nfl.all_players[i].retire()
def next_week():
  global wk
  global week_text
  global game_results
  global year
  global t
  global reverse_win_order
  game_results = []
  playoff_losers_a = []
  playoff_losers_n = []
  #print(wk)
  if wk == 1:
    for i in range(len(nfl.teams)):
      if nfl.teams[i] != user_team:
        nfl.teams[i].cpu_re_sign()
      nfl.teams[i].players_gone(nfl)
    user_team.min_players()
  if wk >= start:
    if user_team.salaries <= user_team.cap_limit and user_team.min_players() == True and user_team.no_of_players() <= 53: 
      ###### Other teams ############
      # Will add 53 man rule to them
      for i in range(len(reverse_win_order)):
        reverse_win_order[i].players_exp(10)
        if reverse_win_order != user_team:
          reverse_win_order[i].cpu_sign_best(nfl)
          while reverse_win_order[i].salaries > nfl.teams[i].cap_limit:
            reverse_win_order[i].cpu_cut(nfl)
          while reverse_win_order[i].min_players() == False:
            reverse_win_order[i].cpu_sign(nfl)
    else:
      ## breaks the next_week procedure
      print("You cannot go to next week. Check info")
      return
  for i in range(len(nfl.teams)):
    nfl.teams[i].pay_players()
  menu_last_weeks_results.clear(False)
  menu_last_weeks_results.add.label("Last Week's Games", max_char=-1, font_size=20)
  if wk == 2:
    random_teams = nfl.teams
    flag = True
    j = 0
    while True:
      random.shuffle(random_teams)
      flag = False
      for i in range(len(random_teams)):
        if random_teams[i] != user_team:
          if random_teams[i].min_players() == False:
            flag = True
            # Teams try to fill their rosters
            random_teams[i].cpu_sign_best(nfl)
            random_teams[i].cpu_sign(nfl)
            if random_teams[i].min_players() == True:
              flag = False
            nfl.create_new_free_agents()
      
      if flag == False:
        break
      
    random.shuffle(random_teams)
    for i in range(len(nfl.teams)):
      if nfl.teams[i] != user_team:
        random_teams[i].add_free_agents(nfl)
  if wk == 3:
    #### After draft undrafted players go to free agency
    for i in range(len(nfl.draft_class)):
      nfl.free_agents.append(nfl.draft_class[i])
    nfl.draft_class = []
    t = nfl.gen_draft(t)
    print("NFL Players:", len(nfl.all_players))
    pick = 0
    while user_team != reverse_win_order[pick]:
      reverse_win_order[pick].add_free_agents(nfl)
      pick += 1
      if pick >= len(nfl.teams):
        pick = 0

  if wk == 4: # Teams sign free agents after draft
    for i in range(len(reverse_win_order)):
      if reverse_win_order[i] != user_team:
        reverse_win_order[i].add_free_agents(nfl)
  if wk >= 9 and wk <= 26: # Teams play regular season games
    for i in range(len(nfl.sch[wk-9])):
      game_results.append(game.game(nfl.sch[wk-9][i][0], nfl.sch[wk-9][i][1]))
    for x in range(len(game_results)):
      menu_last_weeks_results.add.label(game_results[x], max_char=-1, font_size=20)
  if wk == 26:
    AFC.c_standings()
    NFC.c_standings()
    AFC.playoff_teams()
    NFC.playoff_teams()
    reverse_win_order = sorted(nfl.teams,key=lambda team: (team.win_pct), reverse=False)
    draft_pick = (reverse_win_order.index(user_team) + 1) %32
  if wk >= playoff and wk<31: # Playoff games
    a = AFC.playoff_games()
    n = NFC.playoff_games()
    for i in range(len(a)):
      if week[wk] == "Conference Championship": # Conf champ games
        afc_playoff_game = game.conf_champ(a[i][0], a[i][1])
        nfc_playoff_game = game.conf_champ(n[i][0], n[i][1])
      else: # Wild card and divisional round games
        afc_playoff_game = game.playoff_game(a[i][0], a[i][1])
        nfc_playoff_game = game.playoff_game(n[i][0], n[i][1])
      playoff_losers_a.append(afc_playoff_game[0])
      playoff_losers_n.append(nfc_playoff_game[0])
      game_results.append(afc_playoff_game[1])
      game_results.append(nfc_playoff_game[1])
    for l in range(len(game_results)):
      menu_last_weeks_results.add.label(game_results[l], max_char=-1, font_size=20)
    AFC.playoff_elim(playoff_losers_a)
    NFC.playoff_elim(playoff_losers_n)
  if week[wk] == "Super Bowl": ## Super bowl
    champions = game.sb(AFC.playoffs[0], NFC.playoffs[0])
    print(champions[0].name, "WORLD CHAMPS")
    menu_last_weeks_results.add.label(champions[1], max_char=-1, font_size=20)
    menu_last_weeks_results.add.label(champions[0].name + " World Champs", max_char=-1, font_size=20)
    
  if wk < 9: #
    pass
  #also if wk = last, open end of year screen and wk = 0
  wk = wk + 1
  if wk < len(week):
    week_text = week[wk]
  else:
    wk = 0
    week_text = week[wk]
    year = year + 1
    nfl.nfc_south = NFC_SOUTH.teams
    nfl.nfc_north = NFC_NORTH.teams
    nfl.nfc_east = NFC_EAST.teams
    nfl.nfc_west = NFC_WEST.teams
    nfl.afc_east = AFC_EAST.teams
    nfl.afc_west = AFC_WEST.teams
    nfl.afc_south = AFC_SOUTH.teams
    nfl.afc_north = AFC_NORTH.teams
    for i in range(len(nfl.all_players)):
      nfl.all_players[i].end_of_year()
      nfl.all_players[i].retire()
    generate_sch(year, nfl)
    for i in range(len(nfl.teams)):
      nfl.teams[i].end_of_year()
  if wk > start:
    for i in range(len(nfl.teams)):
      nfl.teams[i].update()
  for te in range(len(nfl.teams)):
    nfl.teams[te].players_exp(10)
  for te in range(len(nfl.all_players)):
    nfl.all_players[te].regress()
  home_menu.full_reset()
  early_week_text.set_title(week_text + " - " + str(year))
  late_week_text.set_title(week_text + " - " + str(year))
  off_week_text.set_title(week_text + " - " + str(year))
  playoff_week_text.set_title(week_text + " - " + str(year))
  go_to_game_menu()
# Viewing the last weeks result
def go_to_results():
  go_from_main_menu(menu_last_weeks_results)

# Buttons and removed buttons
menu_off.add.button("Home", go_home)
menu_off.add.button("View Team", go_view_your_team)
menu_off.add.button("Players Leaving", go_players_leaving)
menu_off.add.button("Free Agency", go_free)
#menu_off.add.button("Draft", go_draft)
#menu_off.add.button("Coaches", go_coaches)
menu_off.add.button("View Another Team", go_to_choose_team)
menu_off.add.button("Next Week", next_week)
#####



menu_early.add.button("Home", go_home)
menu_early.add.button("Free Agency", go_free)
menu_early.add.button("View Team", go_view_your_team)
menu_early.add.button("Standings", go_standings)
menu_early.add.button("Last Week's Games", go_to_results)
#menu_early.add.button("Stats", go_stats)
#menu_early.add.button("Training", go_training)
#menu_early.add.button("Draft", go_draft)
menu_early.add.button("View Another Team", go_to_choose_team)
menu_early.add.button("Next Week", next_week)
#####
menu_playoffs.add.button("Home", go_home)
menu_playoffs.add.button("Free Agency", go_free)
menu_playoffs.add.button("View Team", go_view_your_team)
menu_playoffs.add.button("Standings", go_standings)
menu_playoffs.add.button("Last Week's Games", go_to_results)
#menu_playoffs.add.button("Stats", go_stats)
#menu_playoffs.add.button("Training", go_training)
#menu_playoffs.add.button("Draft", go_draft)
menu_playoffs.add.button("View Another Team", go_to_choose_team)
menu_playoffs.add.button("Next Week", next_week)

menu_late.add.button("Home", go_home)
menu_late.add.button("Free Agency", go_free)
menu_late.add.button("View Team", go_view_your_team)
menu_late.add.button("Standings", go_standings)
menu_late.add.button("Last Week's Games", go_to_results)
#menu_late.add.button("Stats", go_stats)
#menu_late.add.button("Training", go_training)
#menu_late.add.button("Draft", go_draft)
menu_late.add.button("View Another Team", go_to_choose_team)
menu_late.add.button("Next Week", next_week)
# Test
print("NFL Players:", len(nfl.all_players))