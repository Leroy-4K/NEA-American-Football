print(200)
print(224)
class Conference:

  def __init__(self, team1, team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12, team13, team14, team15, team16):
    self.team1 = team1
    self.team2 = team2
    self.team3 = team3
    self.team4 = team4
    self.team5 = team5
    self.team6 = team6
    self.team7 = team7
    self.team8 = team8
    self.team9 = team9
    self.team10 = team10
    self.team11 = team11
    self.team12 = team12
    self.team13 = team13
    self.team14 = team14
    self.team15 = team15
    self.team16 = team16
    self.teams = [self.team1, self.team2, self.team3, self.team4, self.team5, self.team6, self.team7, self.team8, self.team9, self.team10, self.team11, self.team12, self.team13, self.team14, self.team15, self.team16]
    self.rankings = []
    self.the_rest = []
    self.playoffs = []
    self.div_winners = []
    self.div1 = None
    self.div2 = None
    self.div3 = None
    self.div4 = None


  def compare(self, arr): #This function is used to compare the teams in the conference
    sorted(arr, key=lambda team: [team.win_pct, team.conf_win_pct, team.pts_for_szn - team.pts_against_szn, team.pts_for_szn, team.pts_against_szn], reverse=True)
    return arr[0]
    
    
  def sort_the_rest(self): # Not working
    g = 1
    h = 1
    i = 1
    j = 1
    sorted = []
    for l in range(len(self.the_rest)):
      ar = []
      if g <=3:
        ar.append(self.div1.teams[g])
      if h <=3:
        ar.append(self.div2.teams[h])
      if i <=3:
        ar.append(self.div3.teams[i])
      if j <=3:
        ar.append(self.div4.teams[j])
      team = self.compare(ar)
      sorted.append(team)
      if team in self.div1.teams:
        g += 1
      elif team in self.div2.teams:
        h += 1
      elif team in self.div3.teams:
        i += 1
      elif team in self.div4.teams:
        j += 1
    print(len(sorted))
    return sorted
      
  def c_standings(self): #This method will be used to sort the teams in the conference standings
    self.rankings = []
    self.div1.standings()
    self.div2.standings()
    self.div3.standings()
    self.div4.standings()
    self.div_winners = [self.div1.teams[0], self.div2.teams[0], self.div3.teams[0], self.div4.teams[0]]
    self.div_winners = sorted(self.div_winners, key=lambda team: (team.win_pct, team.conf_win_pct), reverse=True)
    self.the_rest = []
    for i in range(len(self.div1.teams)-1):
      self.the_rest.append(self.div1.teams[i+1])
    for i in range(len(self.div2.teams)-1):
      self.the_rest.append(self.div2.teams[i+1])
    for i in range(len(self.div3.teams)-1):
      self.the_rest.append(self.div3.teams[i+1])
    for i in range(len(self.div4.teams)-1):
      self.the_rest.append(self.div4.teams[i+1])
    self.the_rest = sorted(self.the_rest, key=lambda team: team.win_pct, reverse=True)
    #self.the_rest = self.sort_the_rest()
    
    for i in range(len(self.div_winners)):
      self.rankings.append(self.div_winners[i])
    for i in range(len(self.the_rest)):
      self.rankings.append(self.the_rest[i])

  def playoff_teams(self): # Adds the playoff teams in the conference
    self.playoffs = self.rankings[0:7]
    for i in range(len(self.playoffs)):
      self.playoffs[i].playoff_seed = i + 1
    self.playoffs[0].div_winner()
    self.playoffs[1].div_winner()
    self.playoffs[2].div_winner()
    self.playoffs[3].div_winner()
    print(self.playoffs[0].name, self.playoffs[1].name, self.playoffs[2].name, self.playoffs[3].name)
  
  def playoff_elim(self, loser_arr): # eliminates the defeated teams and re-seeds the playoff teams
    for i in range(len(loser_arr)):
      self.playoffs.remove(loser_arr[i])
    self.re_seeding()

  def playoff_games(self): #Ensures that the lowest and highest seeded playoff teams play each other
    arr = []
    print(len(self.playoffs))
    if len(self.playoffs) == 7:
      arr = [[self.playoffs[1], self.playoffs[6]], [self.playoffs[2], self.playoffs[5]], [self.playoffs[3], self.playoffs[4]]]
    else:
      for i in range(int(len(self.playoffs)/2)):
        arr.append([self.playoffs[i], self.playoffs[-i-1]])
    return arr
    

  def re_seeding(self): # Re sorts the playoff teams by playoff seed
    self.playoffs = sorted(self.playoffs, key=lambda team: team.playoff_seed)
    

class Division:

  def __init__(self, team1, team2, team3, team4, conf, name):
    self.conf = conf
    self.name = name
    self.team1 = team1
    self.team2 = team2
    self.team3 = team3
    self.team4 = team4
    self.teams = [self.team1, self.team2, self.team3, self.team4]

  def standings(self): # Sorts division standings with win percentage, div percentage and points diffrential. 
    teams = sorted(self.teams,key=lambda team: [round(team.win_pct, 3), round(team.div_win_pct, 3), team.pts_for_szn - team.pts_against_szn, team.pts_for_szn, team.pts_against_szn], reverse=True)
    self.teams = teams
    
  def set_div(self): # Used to add attributes to the teams in the divison
    for i in range (len(self.teams)):
      self.teams[i].conf = self.conf
      self.teams[i].div = self.name