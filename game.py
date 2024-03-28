import random
class Game:
  def __init__(self):
    # put all notable single game records, put player name and numerical record.
    self.p_yards_record = []
    self.p_tds_record = []
    self.p_ints_record = []
    self.catches_record = []
    self.rec_yards_record = []
    self.rec_tds_record = []
    self.rushing_yards_record = []
    self.rushing_tds_record = []
    self.tackles_record = []
    self.ints_record = []
    self.sacks_record = []
    self.f_fum_record = []
    self.fum_rec_record = []
    self.f_td_record = []
    self.sfty_record = []
    self.tfl_record = []

    self.longest_kick = []
    self.longest_punt = []

  def home_score(self, home, away):
    rushing_plays = 0

  def field_goal(team,yards):
    j = team.Ks[0].field_goal(yards)
    if j == True:
      return 3
    else:
      return 0
      
  def game(self, home, away):
    home.line_power()
    away.line_power()
    home.cal_ovr()
    away.cal_ovr()
    OT = ""
    home_points = (home.off_ovr/away.def_ovr)*21
    home_points = int(random.gauss(home_points, 3))
    
    if home_points < 0 or home_points == 1:
      home_points = 0
    away_points = (away.off_ovr/home.def_ovr) * 21
    away_points = int(random.gauss(away_points, 3))
    if away_points < 0 or away_points == 1:
      away_points = 0

    # Updates team attributes
    home.pts_for_szn += home_points
    home.pts_against_szn += away_points
    away.pts_for_szn += away_points
    away.pts_against_szn += home_points
    home.games_szn += 1
    away.games_szn += 1
    if home_points != away_points:
      if home_points > away_points:
        winner = home
        loser = away
        home.teams_played.append([away,1])
        away.teams_played.append([home,-1])
        home.home_wins_szn += 1
        away.away_losses_szn += 1
        
      elif away_points > home_points:
        winner = away
        loser = home
        home.teams_played.append([away,-1])
        away.teams_played.append([home,1])
        home.home_losses_szn += 1
        away.away_wins_szn += 1
      
      if winner.conf == loser.conf:
        winner.conf_wins_szn += 1
        winner.conf_games_szn += 1
        loser.conf_losses_szn += 1
        loser.conf_games_szn += 1
        ## If in the same conference they could be in the same division
        if winner.div == loser.div:
          winner.div_wins_szn += 1
          loser.div_losses_szn += 1
      winner.wins_szn += 1
      loser.losses_szn += 1
      winner.starters_exp(30)
      winner.morale(5)
      loser.morale(-3)
      loser.starters_exp(10)
      
    else:
      home.ties_szn += 1
      home.home_ties_szn += 1
      away.ties_szn += 1
      away.away_ties_szn += 1
      home.starters_exp(20)
      away.starters_exp(20)
      home.teams_played.append([away,0])
      away.teams_played.append([home,0])
      # Tie means no morale change
      if home.conf == away.conf:
        home.conf_ties_szn += 1
        home.conf_games_szn += 1
        away.conf_ties_szn += 1
        away.conf_games_szn += 1
        ## If in the same conference they could be in the same division
        if home.div == away.div:
          home.div_ties_szn += 1
          away.div_ties_szn += 1
    text = str(home.short_hand) + " (" + str(home.ovr) + ") - " + str(home_points) + " " + str(away.short_hand) + " (" + str(away.ovr) + ") - " + str(away_points) + " " + OT
    print(text)
    # text is returned to be added to the menu screen
    return text
  # unused
  def pass_play(self, off, deff):
    pass
  # unused
  def play_by_play(self, home, away):
    field = [0] * 100
    pos = "H"

  # determines playoff results
  def playoff_game(self, home, away):
    home.line_power()
    away.line_power()
    home.cal_ovr()
    away.cal_ovr()
    home_turnovers = random.randint(0, 4)
    away_turnovers = random.randint(0, 4)
    home_points = ((home.off_ovr*1.1)/away.def_ovr)*21
    home_points = int(random.gauss(home_points, 3))
    if home_points < 0 or home_points == 1:
      home_points = 0
    
    away_points = (away.off_ovr/home.def_ovr)*21
    away_points = int(random.gauss(away_points, 3))
    if away_points < 0 or away_points == 1:
        away_points = 0
    if home_points != away_points:
      if home_points > away_points:
        winner = home
        loser = away
        

      elif away_points > home_points:
        winner = away
        loser = home

    elif home_points == away_points:
      loser = random.choice([home, away])
      if loser == home:
        winner = away
      else:
        winner = home
    text = str(home.short_hand) + " (" + str(home.ovr) + ") - " + str(home_points) + " " + str(away.short_hand) + " (" + str(away.ovr) + ") - " + str(away_points)
    print(text)
    ## Do the exp gain
    winner.starters_exp(30)
    winner.morale(15)
    loser.starters_exp(15)
    loser.morale(-7)
    winner.playoff_winner()
    return [loser, text]
    
  # determines the playoff results
  def conf_champ(self, home, away):
    home.line_power()
    away.line_power()
    home.cal_ovr()
    away.cal_ovr()
    home_points = ((home.off_ovr*1.1)/away.def_ovr*21)
    home_points = int(random.gauss(home_points, 5))
    if home_points < 0 or home_points == 1:
      home_points = 0

    away_points = (away.off_ovr/home.def_ovr)*21
    away_points = int(random.gauss(away_points, 5))
    if away_points < 0 or away_points == 1:
        away_points = 0
    if home_points != away_points:
      if home_points > away_points:
        winner = home
        loser = away


      elif away_points > home_points:
        winner = away
        loser = home

    elif home_points == away_points:
      loser = random.choice([home, away])
      if loser == home:
        winner = away
      else:
        winner = home
    text = str(home.short_hand) + " (" + str(home.ovr) + ") - " + str(home_points) + " " + str(away.short_hand) + " (" + str(away.ovr) + ") - " + str(away_points)
    ## Exp and morale ##
    winner.starters_exp(50)
    winner.morale(25)
    loser.starters_exp(20)
    loser.morale(-10)
    winner.conf_winner()
    print(text)
    return [loser, text]

  # super bowl#
  def sb(self, home, away):
    home.line_power()
    away.line_power()
    home.cal_ovr()
    away.cal_ovr()
    ## Higher standing deviation ##
    home_points = (home.off_ovr/away.def_ovr)*21
    home_points = int(random.gauss(home_points, 7))
    if home_points < 0 or home_points == 1:
      home_points = 0

    away_points = (away.off_ovr/home.def_ovr)*21
    away_points = int(random.gauss(away_points, 7))
    if away_points < 0 or away_points == 1:
      away_points = 0
    if home_points != away_points:
      if home_points > away_points:
        winner = home
        loser = away

      elif away_points > home_points:
        winner = away
        loser = home

    elif home_points == away_points:
      winner = random.choice([home, away])
      if winner == home:
        loser = away
      else:
        loser = home
    text = str(home.short_hand) + " (" + str(home.ovr) + ") - " + str(home_points) + " " + str(away.short_hand) + " (" + str(away.ovr) + ") - " + str(away_points)

    ## morale and exp ##
    winner.players_exp(200)
    winner.morale(100)
    loser.players_exp(40)
    loser.morale(-20)
    winner.sb_winner()
    
    print(text)
    return [winner, text]