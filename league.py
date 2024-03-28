import random
from names import *
from teams import Team
from players import *


class League:
  def __init__(self):
    self.teams = []
    self.nfc_north = []
    self.nfc_south = []
    self.nfc_east = []
    self.nfc_west = []
    self.afc_north = []
    self.afc_south = []
    self.afc_east = []
    self.afc_west = []
    self.draft_class = []
    self.records = []
    self.all_players = []
    self.year = 2023
    self.week1 = []
    self.week2 = []
    self.week3 = []
    self.week4 = []
    self.week5 = []
    self.week6 = []
    self.week7 = []
    self.week8 = []
    self.week9 = []
    self.week10 = []
    self.week11 = []
    self.week12 = []
    self.week13 = []
    self.week14 = []
    self.week15= []
    self.week16 = []
    self.week17 = []
    self.week18 = []
    self.sch = [self.week1, self.week2, self.week3, self.week4, self.week5, self.week6, self.week7, self.week8, self.week9, self.week10, self.week11, self.week12, self.week13, self.week14, self.week15, self.week16, self.week17, self.week18]
    self.p_yards_record = []
    self.p_tds_record = []
    self.p_ints_record = []
    self.catches_record = []
    self.rec_yards_record = []
    self.rec_tds_record = []
    self.r_yards_record = []
    self.r_tds_record = []
    self.tackles_record = []
    self.ints_record = []
    self.sacks_record = []
    self.f_fum_record = []
    self.fum_rec_record = []
    self.f_td_record = []
    self.sfty_record = []
    self.tfl_record = []


    self.free_agents = []
  
  def sort_free(self):
    # Remove retired players
    free_retired = 0
    while free_retired < len(self.free_agents):
      if self.free_agents[free_retired].retired == True:
        self.free_agents.pop(free_retired)
      else:
        free_retired += 1
    self.free_agents = sorted(self.free_agents,key=lambda player: player.ovr, reverse=True)
   
  def generate_league_teams(self):
    Falcons = Team("Atlanta Falcons", "ATL", "NFC SOUTH")
    Panthers = Team("Carolina Panthers", "CAR", "NFC SOUTH")
    Bucs = Team("Tampa Bay Buccaneers", "TB", "NFC SOUTH")
    Saints = Team("New Orleans Saints", "NO", "NFC SOUTH")
    ###############################
    Niners = Team("San Francisco 49ers", "SF", "NFC WEST")
    Seahawks = Team("Seattle Seahawks", "SEA", "NFC WEST")
    Rams = Team("LA Rams", "LAR", "NFC WEST")
    Cardinals = Team("Arizona Cardinals", "ARI", "NFC WEST")
    ###########################
    Lions = Team("Detroit Lions", "DET", "NFC NORTH")
    Vikings = Team("Minnesota Vikings", "MIN", "NFC NORTH")
    Packers = Team("Green Bay Packers", "GB", "NFC NORTH")
    Bears = Team("Chicago Bears", "CHI", "NFC NORTH")
    ###############################
    Eagles = Team("Philadelphia Eagles", "PHI", "NFC EAST")
    Cowboys = Team("Dallas Cowboys", "DAL", "NFC EAST")
    Giants = Team("New York Giants", "NYG", "NFC EAST")
    Commies = Team("Washington Commanders", "WAS", "NFC EAST")
    ###########################
    Jaguars = Team("Jacksonville Jaguars", "JAX", "AFC SOUTH")
    Titans = Team("Tennesee Titans", "TEN", "AFC SOUTH")
    Texans = Team("Houston Texans", "HOU", "AFC SOUTH")
    Colts = Team("Indianapolis Colts", "IND", "AFC SOUTH")
    ###############################
    Chiefs = Team("Kansas City Chiefs", "KC", "AFC WEST")
    Chargers = Team("LA Chargers", "LAC", "AFC WEST")
    Broncos = Team("Denver Broncos", "DEN", "AFC WEST")
    Raiders = Team("Las Vegas Raiders", "LV", "AFC WEST")
    ###########################
    Bengals = Team("Cinninati Bengals", "CIN", "AFC NORTH")
    Ravens = Team("Baltimore Ravens", "BAL", "AFC NORTH")
    Steelers = Team("Pittsburgh Steelers", "PIT", "AFC NORTH")
    Browns = Team("Cleveland Browns", "CLE", "AFC NORTH")
    ###############################
    Bills = Team("Buffalo Bills", "BUF", "AFC EAST")
    Dolphins = Team("Miami Dolphins", "MIA", "AFC EAST")
    Jets = Team("New York Jets", "NYJ", "AFC EAST")
    Patriots = Team("New England Patriots", "NE", "AFC EAST")
    ###########################
    self.teams = [Falcons, Panthers, Bucs, Saints, Niners, Seahawks, Rams, Cardinals, Lions, Vikings, Packers, Bears, Eagles, Cowboys, Giants, Commies, Jaguars, Titans, Texans, Colts, Chiefs, Chargers, Broncos, Raiders, Bengals, Ravens, Steelers, Browns, Bills, Dolphins, Jets, Patriots]
    self.nfc_south = [Bucs, Panthers, Saints, Falcons]
    self.nfc_west = [Niners, Seahawks, Rams, Cardinals]
    self.nfc_north = [Vikings, Lions, Packers, Bears]
    self.nfc_east = [Eagles, Cowboys, Giants, Commies]
    self.afc_south = [Jaguars, Titans, Colts, Texans]
    self.afc_west = [Chiefs, Chargers, Raiders, Broncos]
    self.afc_north = [Bengals, Ravens, Steelers, Browns]
    self.afc_east = [Bills, Dolphins, Patriots, Jets]

  def generate_league_players(self, t):
    ## Each team gets the minimum number of players to play games ##
    for i in range(len(self.teams)):
      player = QB("QB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = WR("WR", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = WR("WR", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = WR("WR", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = RB("RB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(10,50), random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = TE("TE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = C("C", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = G("G", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = G("G", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = T("T", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = T("T", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99),random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      #########
      player = DE("DE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = DE("DE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = DT("DT", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = DT("DT", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = OLB("OLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = OLB("OLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = ILB("MLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = CB("CB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = CB("CB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = S("S", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = S("S", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = ST("K", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, random.randint(40,99), random.randint(40,99), t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
      player = ST("P", str(random.choice(names) + " " + random.choice(surnames)), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), random.randint(40,99), False, random.randint(40,99), random.randint(40,99), t, random.randint(23,35))
      years =  random.randint(0,5)
      sal = player.asking_sal()
      self.teams[i].sign(player, self, sal, years)
      self.all_players.append(player)
      t += 1
    return t

  def create_free_agency(self, t):
    ## creates 500 free agents
    for n in range(500):
      opt = ["QB", "RB", "WR", "TE", "C", "G", "T", "DE", "DT", "OLB", "MLB", "CB", "S", "P", "K"]
      g = random.choice(opt)
      if g == "QB":
        player = QB("QB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10, 60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))

      elif g == "WR":
        player = WR("WR", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))

      elif g == "RB":
        player = RB("RB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60),random.randint(10,60), False, t, random.randint(10,60), random.randint(23,35))
 
      elif g == "TE":
        player = TE("TE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60),random.randint(10,60), False, t, random.randint(23,35))

      elif g == "C":
        player = C("C", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))
      elif g == "G":
        player = G("G", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60),False, t, random.randint(23,35))
      elif g == "T":
        player = T("T", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60),random.randint(10,60), False, t, random.randint(23,35))
      elif g == "DE":
        player = DE("DE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))
        
      elif g == "DT":
        player = DT("DT", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))
  
      elif g == "OLB":
        player = OLB("OLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))

      
      elif g == "MLB":
        player = ILB("MLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))
        
      elif g == "CB":
        player = CB("CB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))
        
      elif g == "S":
        player = S("S", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, t, random.randint(23,35))
      elif g == "K":
        player = ST("K", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, random.randint(10,60), random.randint(10,60), t, random.randint(23,35))
      elif g == "P":
        player = ST("P", str(random.choice(names) + " " + random.choice(surnames)), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), random.randint(10,60), False, random.randint(10,60), random.randint(10,60), t, random.randint(23,35))
      self.all_players.append(player)
      player.cal_ovr()
      self.free_agents.append(player)    
      t += 1

    self.sort_free()
    return t

  def create_new_free_agents(self):
    opt = ["QB", "RB", "WR", "WR", "WR", "TE", "C", "G", "G","T", "T", "DE", "DE", "DT", "OLB", "MLB", "CB", "S", "DT", "OLB", "MLB", "CB", "S", "P", "K"]
    t = 0
    for n in range(len(opt)):
      g = opt[n]

      if g == "QB":
        player = QB("QB", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "WR":
        player = WR("WR", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "RB":
        player = RB("RB", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, 10, random.randint(23,35))

      elif g == "TE":
        player = TE("TE", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "C":
        player = C("C", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))
      elif g == "G":
        player = G("G", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))
      elif g == "T":
        player = T("T", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))
      elif g == "DE":
        player = DE("DE", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "DT":
        player = DT("DT", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "OLB":
        player = OLB("OLB", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))


      elif g == "MLB":
        player = ILB("MLB", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "CB":
        player = CB("CB", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))

      elif g == "S":
        player = S("S", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, False, t, random.randint(23,35))
      elif g == "K":
        player = ST("K", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, False, 10, 10, t, random.randint(23,35))
      elif g == "P":
        player = ST("P", str(random.choice(names) + " " + random.choice(surnames)), 10, 10, 10, 10, 10, False, 10, 10, t, random.randint(23,35))
      self.all_players.append(player)
      player.cal_ovr()
      self.free_agents.append(player)    

    self.sort_free()

  def gen_draft(self, t):
    total = random.randint(300, 400)
    for n in range(total):
      opt = ["QB", "RB", "WR", "TE", "C", "G", "T", "DE", "DT", "OLB", "MLB", "CB", "S", "P", "K"]
      g = random.choice(opt)
      outcomes = ["GEN", "GOOD", "NORMAL"]
      probs = [0.03, 0.31, 0.66]
      random_outcome = random.choices(outcomes, probs)[0]
      min = 0
      max = 0
      if random_outcome == "GEN":
        min = random.randint(70, 80)
        max = random.randint(81, 95)
      elif random_outcome == "GOOD":
        min = random.randint(60, 75)
        max = random.randint(76, 90)
      elif random_outcome == "NORMAL":
        min = random.randint(20, 60)
        max = random.randint(61, 90)
      if g == "QB":
        player = QB("QB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))

      elif g == "WR":
        player = WR("WR", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))

      elif g == "RB":
        player = RB("RB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max),random.randint(min, max), True, t, random.randint(min, max), random.randint(21,23))

      elif g == "TE":
        player = TE("TE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max),random.randint(min, max), True, t, random.randint(21,23))

      elif g == "C":
        player = C("C", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))
      elif g == "G":
        player = G("G", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max),True, t, random.randint(21,23))
      elif g == "T":
        player = T("T", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max),random.randint(min, max), True, t, random.randint(21,23))
      elif g == "DE":
        player = DE("DE", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(10,60), True, t, random.randint(21,23))

      elif g == "DT":
        player = DT("DT", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))

      elif g == "OLB":
        player = OLB("OLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))


      elif g == "MLB":
        player = ILB("MLB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))

      elif g == "CB":
        player = CB("CB", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))

      elif g == "S":
        player = S("S", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, t, random.randint(21,23))
      elif g == "K":
        player = ST("K", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, random.randint(min, max), random.randint(min, max), t, random.randint(21,23))
      elif g == "P":
        player = ST("P", str(random.choice(names) + " " + random.choice(surnames)), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), random.randint(min, max), True, random.randint(min, max), random.randint(min, max), t, random.randint(21,23))
      player.cal_ovr()
      self.draft_class.append(player)
      self.all_players.append(player)
      t += 1

    self.sort_draft()
    return t

  def sort_draft(self):
    ## Sorts the draft class by overall rating
    self.draft_class = sorted(self.draft_class, key=lambda player: player.ovr, reverse=True)
    