def cpu_trade(self, team1, team2):
  #### team1 value and team2, value
  pass

def trade(team1_players, team1_picks, team2_players, team2_picks, team1, team2, nfl):
  ## user selects players and picks with tick box, selects oppoising players and picks and clicks confirm to trade
  ## This is the actual trade 
  for i in range(len(team1_players)):
    sal = team1_players[i].yearly_salary
    years = team1_players[i].years_left
    team1.cut_player(team1_players[i], nfl)
    team2.sign(team1_players[i], nfl)
  for i in range(len(team2_players)):
    team2.cut_player(team2_players[i], nfl)
  for i in range(1):
    pass
  
  