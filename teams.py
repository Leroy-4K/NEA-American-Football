import random
class Team:
  def __init__(self, name, short_hand, div, button=""):
    self.name = name
    self.short_hand = short_hand
    self.div = div
    self.button = button
    self.QBs = []
    self.Cs = []
    self.Gs = []
    self.Ts = []
    self.RBs = []
    self.WRs = []
    self.TEs = []
    self.DEs = []
    # self.div_winner = False _> becomes a method
    self.DTs = []
    self.OLBs = []
    self.ILBs = []
    self.CBs = []
    self.Ss = []
    self.Ps = []
    self.Ks = []
    self.players = []
    self.draft_picks_this_year = []
    self.draft_picks_next_year = []
    self.div_wins = 0
    self.div_losses = 0
    self.div_ties = 0
    self.salaries = 0
    self.cap_limit = 200000000
    self.wins_szn = 0
    self.home_wins_szn = 0
    self.home_losses_szn = 0
    self.home_ties_szn = 0
    self.away_wins_szn = 0
    self.away_losses_szn = 0
    self.away_ties_szn = 0
    self.win_streak = 0
    self.loss_streak = 0
    self.div_wins_szn = 0
    self.div_losses_szn = 0 
    self.div_ties_szn = 0
    self.conf_wins_szn = 0
    self.conf_losses_szn = 0
    self.conf_ties_szn = 0
    self.conf_games_szn = 0
    self.div_games_szn = 0
    self.wins = 0
    self.losses = 0
    self.losses_szn = 0
    self.ties = 0
    self.ties_szn = 0
    self.games_szn = 0
    self.games = 0
    self.ovr = 0
    self.win_pct = 0
    self.off_ovr = 0
    self.pts_for_szn = 0
    self.pts_against_szn = 0
    self.teams_played = []
    self.def_ovr = 0
    self.rb_power = 0
    self.pb_power = 0
    self.pr_power = 0
    self.rd_power = 0
    self.playoff_seed = 0
    
    self.players_sorted_by_salary = []
    self.tot_players = []

    self.conf = ""
    self.div = ""
    self.sch = []
    self.players_leaving = []
    self.div_win_pct = 0
    self.conf_win_pct = 0
    

    self.sbs = 0
    self.conf_champs = 0
    self.playoff_wins = 0
    self.div_titles = 0

  def sort_all(self):
    for i in range(len(self.tot_players)):
      self.tot_players[i].cal_ovr()
    self.QBs = sorted(self.QBs,key=lambda player: player.ovr, reverse=True)
    self.RBs = sorted(self.RBs,key=lambda player: player.ovr, reverse=True)
    self.WRs = sorted(self.WRs,key=lambda player: player.ovr, reverse=True)
    self.TEs = sorted(self.TEs,key=lambda player: player.ovr, reverse=True)
    self.Cs = sorted(self.Cs,key=lambda player: player.ovr, reverse=True)
    self.Gs = sorted(self.Gs,key=lambda player: player.ovr, reverse=True)
    self.Ts = sorted(self.Ts,key=lambda player: player.ovr, reverse=True)
    self.DEs = sorted(self.DEs,key=lambda player: player.ovr, reverse=True)
    self.DTs = sorted(self.DTs,key=lambda player: player.ovr, reverse=True)
    self.OLBs = sorted(self.OLBs,key=lambda player: player.ovr, reverse=True)
    self.ILBs = sorted(self.ILBs,key=lambda player: player.ovr, reverse=True)
    self.CBs = sorted(self.CBs,key=lambda player: player.ovr, reverse=True)
    self.Ss = sorted(self.Ss,key=lambda player: player.ovr, reverse=True)
    self.Ps = sorted(self.Ps,key=lambda player: player.ovr, reverse=True)
    self.Ks = sorted(self.Ks,key=lambda player: player.ovr, reverse=True)
    
  def all_players(self):
    self.players = [self.QBs, self.RBs, self.WRs, self.TEs, self.Cs, self.Gs, self.Ts, self.DEs, self.DTs, self.OLBs, self.ILBs, self.CBs, self.Ss, self.Ps, self.Ks]
    self.sort_all()

  def line_power(self):
    
    self.rb_power = ((self.Gs[0].rb + self.Gs[1].rb)*5.5 + self.Cs[0].rb * 5 + (self.Ts[0].rb + self.Ts[1].rb) * 4.2 + (self.WRs[0].rb + self.WRs[1].rb + self.WRs[2].rb) * 0.4 + (self.TEs[0].rb * 2)) + ((self.Gs[0].strength + self.Gs[1].strength) * 4 + self.Cs[0].strength * 4 + (self.Ts[0].strength + self.Ts[1].strength) * 4 + (self.WRs[0].strength + self.WRs[1].strength + self.WRs[2].strength) * 0.3 + (self.TEs[0].strength * 2))
    
    self.pb_power = ((self.Gs[0].pb + self.Gs[1].pb) * 4 + self.Cs[0].pb * 4.5 + (self.Ts[0].pb + self.Ts[1].pb) * 5 + (self.RBs[0].pb * 0.7)) + ((self.Gs[0].strength + self.Gs[1].strength) * 4 + self.Cs[0].strength * 4 + (self.Ts[0].strength + self.Ts[1].strength) * 4 +(self.RBs[0].strength * 1.5))

    self.pr_power = (self.DEs[0].pr+ self.DEs[1].pr) + (self.DEs[1].strength + self.DEs[0].strength) + self.DTs[0].pr + self.DTs[0].pr +  (self.DTs[0].strength + self.DTs[0].strength) + self.OLBs[0].pr + self.OLBs[1].pr + self.ILBs[0].pr + self.OLBs[0].pr + self.OLBs[1].pr + self.ILBs[0].pr + 0.1 * (self.CBs[0].pr +self.CBs[1].pr + self.Ss[0].pr + self.Ss[1].pr)

    self.rd_power = self.DEs[0].rd + self.DEs[1].rd + self.DTs[0].rd + self.DTs[0].rd + self.OLBs[0].rd + self.OLBs[1].rd + self.ILBs[0].rd + self.CBs[0].rd + self.CBs[1].rd + self.Ss[0].rd + self.Ss[1].rd

  def starters(self):
    pass

  def pay_players(self):
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].earn()
  
  def end_of_year(self):
    self.wins_szn = 0
    self.losses_szn = 0
    self.ties_szn = 0
    self.div_wins_szn = 0
    self.div_losses_szn = 0
    self.div_ties_szn = 0
    self.conf_wins_szn = 0
    self.conf_losses_szn = 0
    self.conf_ties_szn = 0
    self.win_pct = 0
    self.pts_for_szn = 0
    self.pts_against_szn = 0
    self.home_wins_szn = 0
    self.home_losses_szn = 0
    self.home_ties_szn = 0
    self.games_szn = 0
    self.div_games_szn = 0
    self.conf_games_szn = 0
    self.conf_win_pct = 0
    self.div_win_pct = 0
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].contract_years -= 1
    self.players_going()
      
  def total_players(self):
    self.all_players()
    self.tot_players = []
    for i in range (len(self.players)):
      for j in range (len(self.players[i])):
        self.tot_players.append(self.players[i][j])

  def remove_draft_pick(self, pick):
    pass
  def cut_player(self, player, nfl):
    if player.retired == False:
      nfl.free_agents.append(player)
    if player.pos == "QB":
      self.QBs.remove(player)
    elif player.pos == "RB":
      self.RBs.remove(player)
    elif player.pos == "WR":
      self.WRs.remove(player)
    elif player.pos == "TE":
      self.TEs.remove(player)
    elif player.pos == "C":
      self.Cs.remove(player)
    elif player.pos == "G":
      self.Gs.remove(player)
    elif player.pos == "T":
      self.Ts.remove(player)
    elif player.pos == "DE":
      self.DEs.remove(player)
    elif player.pos == "DT":
      self.DTs.remove(player)
    elif player.pos == "OLB":
      self.OLBs.remove(player)
    elif player.pos == "MLB":
      self.ILBs.remove(player)
    elif player.pos == "CB":
      self.CBs.remove(player)
    elif player.pos == "S":
      self.Ss.remove(player)
    elif player.pos == "P":
      self.Ps.remove(player)
    elif player.pos == "K":
      self.Ks.remove(player)
    self.total_players()
    nfl.sort_free()
    self.salaries -= player.yearly_salary
    player.yearly_salary = 0
    player.contract_years = 0
    
  def cpu_draft(self, draft_class, sal, nfl):
    draft = sorted(draft_class,key=lambda player: player.ovr, reverse=True)
    self.sign(draft[0], nfl, sal, 4)

  def sb_winner(self):
    self.playoff_winner()
    for i in range(len(self.tot_players)):
      self.tot_players[i].sb_winner()
    self.sbs += 1
    
  def conf_winner(self):
    self.playoff_winner()
    for i in range(len(self.tot_players)):
      self.tot_players[i].conf_winner()
    self.conf_champs += 1

  def playoff_winner(self):
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].playoff_winner()
    self.playoff_wins+= 1
    
  def pre_game_checks(self):
    pass

  def over_cap(self):
    pass

  def div_winner(self):
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].div_winner()
    self.div_titles =+ 1


  def sort_by_salary(self):
    self.players_sorted_by_salary = sorted(self.tot_players,key=lambda player: player.yearly_salary, reverse=True)

  def cpu_cut(self, nfl):
    self.sort_by_salary()
    if self.players_sorted_by_salary[0] == self.QBs[0]:
      self.cut_player(self.players_sorted_by_salary[1], nfl)
    else:
      self.cut_player(self.players_sorted_by_salary[0], nfl)

  def cpu_sign(self, nfl):
    nfl.sort_free()
    huui = self.min_players()
    #print(self.missing_pos)
    pl = nfl.free_agents[::-1]
    signed = False
    i = 0
    if len(self.missing_pos) > 0:
      while i < len(nfl.free_agents):
        years = random.randint(1,5)
        if pl[i].pos in self.missing_pos:
          self.sign(pl[i], nfl, pl[i].asking_sal(), years)
          signed = True
          huui = self.min_players()
          pl = nfl.free_agents[::-1]
          
        else:
          i = i + 1
      if signed == False:
        nfl.create_new_free_agents()
        i = i + 1
      pl = nfl.free_agents[::-1]
      huui = self.min_players()

  def cpu_sign_best(self, nfl):
    nfl.sort_free()
    huui = self.min_players()
    pl = nfl.free_agents
    #print(len(self.missing_pos), self.missing_pos)
    no_players = True
    i = 0
    player = 0
    while player < len(nfl.free_agents):
      years = random.randint(1,5)
      if nfl.free_agents[player].pos in self.missing_pos:
        no_players == False
        self.sign(nfl.free_agents[player], nfl, nfl.free_agents[player].asking_salary, years)
        huui = self.min_players()
      player = player + 1
    if huui == False:
      nfl.create_new_free_agents()
      self.cpu_sign_best(nfl)
        #print(self.name, "Player name", pl[player].name, "Pos", pl[player].pos, "Salary", pl[player].asking_salary, "Years", years, "OVR", pl[player].ovr)
      #print("No players")
      

  def add_free_agents(self, nfl):
    self.weakest_starters()
    nfl.sort_free()
    if len(self.weakest_pos) >= 5:
      r = 5
    else:
      self.total_players()
      r = len(self.weakest_pos)
    #print("WEAK:", self.weakest_pos)
    #for i in range(r):
    signed = False
    bypos = [obj for obj in nfl.free_agents if obj.pos == self.weakest_pos[0] or obj.pos == self.weakest_pos[1] or obj.pos == self.weakest_pos[2] or obj.pos == self.weakest_pos[1] or obj.pos == self.weakest_pos[3] or obj.pos == self.weakest_pos[1] or obj.pos == self.weakest_pos[4]]
    i = 0
    while signed == False:
      if i >= len(bypos):
        break
      player = bypos[i]
      no = 0
      comp = []
      #print(player.pos)
      for l in range(len(self.tot_players)):
        if self.tot_players[l].pos == player.pos:
          no += 1
          comp.append(self.tot_players[l])
          sorted(comp,key=lambda player: player.ovr, reverse=True)
          
      if (((self.salaries + player.asking_sal()) < 200*(10**6))):
        if no < 4:
          self.sign(player, nfl, player.asking_sal(), random.randint(1,5))
          signed = True
        elif player.ovr > comp[2].ovr:
          self.sign(player, nfl, player.asking_sal(), random.randint(1,5))
          signed = True
          self.cut_player(comp[-1], nfl)
      i += 1
          
    
  def no_of_players(self):
    return len(self.QBs) + len(self.RBs) + len(self.WRs) + len(self.TEs) + len(self.Cs) + len(self.Gs) + len(self.Ts) + len(self.DEs) + len(self.DTs) + len(self.OLBs) + len(self.ILBs) + len(self.CBs) + len(self.Ss) + len(self.Ps) + len(self.Ks)

  def min_players(self):
    self.missing_pos = []
    n = True
    if len(self.QBs) < 1:
      n = False
      self.missing_pos.append("QB")
    if len(self.RBs) < 1:
      n = False
      self.missing_pos.append("RB")
    if len(self.WRs) < 3:
      n = False
      self.missing_pos.append("WR")
    if len(self.TEs) < 1:
      n = False
      self.missing_pos.append("TE")
    if len(self.Cs) < 1:
      n = False
      self.missing_pos.append("C")
    if len(self.Gs) < 2:
      n = False
      self.missing_pos.append("G")
    if len(self.Ts) < 2:
      n = False
      self.missing_pos.append("T")
    if len(self.DEs) < 2:
      n = False
      self.missing_pos.append("DE")
    if len(self.DTs) < 2:
      n = False
      self.missing_pos.append("DT")
    if len(self.OLBs) < 2:
      n = False
      self.missing_pos.append("OLB")
    if len(self.ILBs) < 1:
      n = False
      self.missing_pos.append("MLB")
    if len(self.CBs) < 2:
      n = False
      self.missing_pos.append("CB")
    if len(self.Ss) < 2:
      n = False
      self.missing_pos.append("S")
    if len(self.Ps) < 1:
      n = False
      self.missing_pos.append("P")
    if len(self.Ks) < 1:
      n = False
      self.missing_pos.append("K")
    return n

  def players_going(self):
    self.total_players()
    for i in range(len(self.tot_players)):
      if self.tot_players[i].contract_years <= 0:
        self.players_leaving.append(self.tot_players[i])
      
  def sign(self, player, nfl, sal, years):
    if player in nfl.free_agents:
      nfl.free_agents.remove(player)
      #print("Removed from free")
    if player.pos == "QB":
      self.QBs.append(player)
    elif player.pos == "RB":
      self.RBs.append(player)
    elif player.pos == "WR":
      self.WRs.append(player)
    elif player.pos == "TE":
      self.TEs.append(player)
    elif player.pos == "C":
      self.Cs.append(player)
    elif player.pos == "G":
      self.Gs.append(player)
    elif player.pos == "T":
      self.Ts.append(player)
    elif player.pos == "DE":
      self.DEs.append(player)
    elif player.pos == "DT":
      self.DTs.append(player)
    elif player.pos == "OLB":
      self.OLBs.append(player)
    elif player.pos == "MLB":
      self.ILBs.append(player)
    elif player.pos == "CB":
      self.CBs.append(player)
    elif player.pos == "S":
      self.Ss.append(player)
    elif player.pos == "P":
      self.Ps.append(player)
    elif player.pos == "K":
      self.Ks.append(player)
    self.all_players()
    self.total_players()
    self.salaries += sal
    player.yearly_salary = sal
    player.contract_years = years

  def weakest_starters(self):
    self.weakest_pos = []
    self.players_sorted_by_ovr = sorted(self.tot_players,key=lambda player: player.ovr)
    #print(self.players_sorted_by_ovr[0].ovr)
    for i in range(len(self.players_sorted_by_ovr)):
      if self.players_sorted_by_ovr[i].pos in self.weakest_pos:
        pass
      else:
        self.weakest_pos.append(self.players_sorted_by_ovr[i].pos)

  def re_sign(self, player, sal, years):
    self.players_leaving.remove(player)
    self.salaries -= player.yearly_salary - sal
    player.yearly_salary = sal
    player.contract_years = years

  def cpu_re_sign(self):
    i = 0
    while i < len(self.players_leaving):
      player = self.players_leaving[i]
      sal = self.players_leaving[i].asking_sal()
      years = random.randint(1,6)
      if player.pos != "QB":
        if (self.salaries- player.yearly_salary + sal) < 200*(10**6) and player.ovr > 75 and random.randint(0, 100) < player.ovr and player.retired == False:
          self.re_sign(player, sal, years)
          #print("Name:", player.name, "Pos:", player.pos, "Salary:", sal, "Years:", years, "OVR:", player.ovr, "Team", self.short_hand)
          #print("CPU RESIGNED")
        else:
          i = i + 1
      else:
        if player == self.QBs[0]:
          self.re_sign(player, sal, years)
        else:
            i = i + 1
    
  def players_gone(self, nfl):
    for i in range(len(self.players_leaving)):
      self.cut_player(self.players_leaving[i], nfl)
    self.players_leaving = []
  
  def view_team(self):
    opt = ""
    while opt != "Off" and opt != "Def" and opt != "Sp":
      opt = input("Enter Off, Def, Sp ")
    if opt == "Off":
      print("QB")
    h = ""
    while h == "":
      h = input("Enter any character to leave to main menu")

  def show(self):
    print(self.short_hand, "Off ovr -", self.off_ovr, "Def ovr -", self.def_ovr)

  def view_sch(self, week):
    pass

  def players_exp(self, exp):
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].exp_gain(exp)
  
  def starters_exp(self, exp):
    starters = [self.QBs[0], self.RBs[0], self.WRs[0], self.WRs[1], self.WRs[2], self.TEs[0], self.Cs[0], self.Gs[0], self.Gs[1], self.Ts[0], self.Ts[1], self.DEs[0], self.DEs[1], self.DTs[0], self.DTs[1], self.OLBs[0], self.OLBs[1], self.ILBs[0], self.CBs[0], self.CBs[1], self.Ss[0], self.Ss[1], self.Ps[0], self.Ks[0]]
    for i in range(len(starters)):
      starters[i].exp_gain(exp)

  def morale(self, mor):#Changes the morale of a team players
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].morale_change(mor)
  
  def cal_ovr(self): #Calculate the team's overall rating if the team has their minimum number of players
    self.total_players()
    for i in range(len(self.tot_players)):
      self.tot_players[i].cal_ovr()
    self.off_ovr = round(((self.QBs[0].ovr * 4) + self.RBs[0].ovr + self.Ts[0].ovr + self.Cs[0].ovr + self.Gs[0].ovr + self.Ts[1].ovr + self.Gs[1].ovr + self.WRs[0].ovr + self.WRs[1].ovr + self.WRs[2].ovr + self.TEs[0].ovr)/15)
    self.def_ovr = round((self.DEs[0].ovr + self.DEs[1].ovr + self.DTs[0].ovr + self.DTs[1].ovr + self.ILBs[0].ovr + self.OLBs[0].ovr + self.OLBs[1].ovr + self.CBs[0].ovr + self.CBs[1].ovr + self.Ss[0].ovr + self.Ss[1].ovr)/11)
    self.st_ovr = round((self.Ps[0].ovr+self.Ks[0].ovr)/2)
    self.ovr = round((self.off_ovr +self.def_ovr+ self.st_ovr*0.1)/2.1)
    self.off_ovr = round(self.off_ovr)
    self.def_ovr = round(self.def_ovr)
  
  def win_per(self): #Calculates the win percentage, div win percentage and conf win percentage of the team
    if self.games_szn != 0:
      self.win_pct = round((self.wins_szn + (1/2)*self.ties_szn) /(self.games_szn),3)
    else:
      self.win_pct = 0
    if self.conf_games_szn != 0:
      self.conf_win_pct = round((self.conf_wins_szn + ((1/2) 
* self.conf_ties_szn)) / (self.conf_games_szn), 3)
    else:
      self.conf_win_pct = 0
    if self.div_games_szn != 0:
      self.div_win_pct = round((self.div_wins_szn+ ((1/2)*self.div_ties_szn))/(self.div_games_szn), 3)
    else:
      self.div_win_pct = 0

  def update(self):
    #updates the team each week
    self.all_players()
    self.cal_ovr()
    self.win_per()