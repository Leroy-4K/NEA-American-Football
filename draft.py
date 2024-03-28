import random
from names import *
from teams import Team
from players import *
def Draft(self):
  ## arrays
  self.draft = []
  self.draft_class = []

  def draft_round_1(self):
    pass


  def add_picks(self, picks):
    self.draft = picks

  def sim_to_next_user_pick(self, current_pick, user_team):
    i = current_pick
    while i < 224:
      if self.draft[i].current_team == user_team:
        return i
        break
      else:
        i += 1
    return -1

  def draft_pick_sal(self, pos):
    if pos <= 5:
      sal = (33 - pos)/5
    elif pos <= 10:
      sal = (24 - (pos/2))/5
    elif pos <= 32:
      sal = (18 - (pos/32))/5
    elif pos <= 64:
      ## 2nd round
      sal = 2
    elif pos <= 96:
      ## 3rd round
      sal = 1.2
    elif pos <= 128:
      ## 4th round
      sal = 1
    elif pos <= 160:
      ## 5th round
      sal = 0.9
    elif pos <= 192:
      ## 6th round
      sal = 0.5
    elif pos <= 224:
      ## 7th round
      sal = 0.7
    sal = round(sal * (10 **6))
    return sal
  def next_pick(self, pos, user_team, nfl):
    sal = self.draft_pick_sal(pos)
    if self.draft[pos].current_team != user_team:
      self.draft[pos].current_team.cpu_draft(self.draft_class, sal, nfl)
  
def Draft_Pick(self, team, year, rd):
  self.team = team
  self.year = year
  self.rd = rd
  self.title = str(year) + " " + team.short_hand + "'s' " + rd + " Draft Pick"
  self.no = 0
  self.current_team = team

  def draft_no(self, order):
    self.no = (32*self.rd) + order + 1
    self.title = str(year) + " " + self.current_team.short_hand + "'s' " + rd + " Draft Pick" + " " + str(self.no) 

  def traded(self, new_team):
    self.current_team = new_team
    
