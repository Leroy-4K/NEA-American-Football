import random
images = ["playerfaces/football_player2.svg", "playerfaces/football_player1.svg"]
class Player:
  def __init__(self, pos, name, spd, acc, str, awr, inj, rookie, idx, age): #Constructor for the Player class
    ### sets attributes to the values passed in ### 
    self.pos = pos
    self.name = name
    self.age = age
    self.spd = spd 
    self.strength = str
    self.awr = awr
    self.acc = acc
    self.inj = inj
    self.idx = idx 
    ############### 
    self.morale = 80 
    self.exp = 0
    self.level = 0
    self.years_left = 0
    self.retired = False #
    self.sbs = 0
    self.mvps = 0
    self.pro_bowls = 0
    self.div_titles = 0
    self.conf_champs = 0
    self.money = 0
    self.salary = 0
    self.rookie = rookie
    self.games_szn = 0
    self.yearly_salary = 0
    self.games = 0
    self.inj_no = 0
    self.injured = False
    self.playoff_wins = 0
    self.playoff_losses = 0
    self.career_wins = 0
    self.career_losses = 0
    self.starter = False
    self.pos_award = 0
    self.ovr = 0
    self.pos_sal_avg = 0
    self.retirement_age = 35
    self.button = ""
    self.img = ""
    self.face = random.choice(images)
    self.asking_salary = 0
    self.exp = 0
    self.exp_mult = (random.randint(50, 150)/100)
    self.next_level_exp = 100
    self.inj_len = 0
    self.last_game_stats = []
    self.year_stats = []
    ###### career stats is a multidimensional list with year being in it.
    self.career_stats = []
    self.phy_ovr = 0
    self.tech_ovr = 0
    self.mental_ovr = 0
    self.attr = []
    self.ratings = []
    self.contract_years = 0
    self.missing_pos = []
  def inj(self):
    self.inj_no += 1
    self.inj_len = random.randint(1,3)
    self.injured = True
    self.ratings = []
    # in next week in set up put for all players injured = True, inj_len - 0. if inj_len = 0, self.injured = False
  

  def upgrade_att(self, att):
    att = att + random.randint(1,3)
    if att > 99:
      att = 99
    return att

  def regress_att(self, att):
    att = att - random.randint(1,3)
    if att <= 0:
      att = 1
    return att

  def cal_ovr(self):
    pass

  def asking_sal(self):
    self.cal_ovr()
    if self.ovr > 95:
      self.asking_salary = round(self.pos_sal_avg * (2*self.ovr/75))
    elif self.ovr > 85:
      self.asking_salary = round(self.pos_sal_avg * (1.5*self.ovr/75))
    elif self.ovr >= 40:
      self.asking_salary = round(self.pos_sal_avg * (0.4*self.ovr/80))
    elif self.ovr < 40:
      self.asking_salary = 0
    return self.asking_salary
  def mvp_winner(self):
    self.mvps += 1
    self.exp_mult += 0.3
    self.exp_mult = round(self.exp_mult, 2)
  def sb_winner(self):
    self.sbs += 1
    self.exp_mult += 0.1
    self.exp_mult = round(self.exp_mult, 2)
  def conf_winner(self):
    self.conf_champs += 1
    self.exp_mult += 0.05
    self.exp_mult = round(self.exp_mult, 2)

  def playoff_winner(self):
    self.playoff_wins += 1
    self.exp_mult += 0.05
    self.exp_mult = round(self.exp_mult, 2)

  def div_winner(self):
    self.div_titles += 1
    self.exp_mult += 0.03
    self.exp_mult = round(self.exp_mult, 2)
    
  def pro_bowler(self):
    self.pro_bowls += 1
    self.exp_mult += 0.1
    self.exp_mult = round(self.exp_mult, 2)
  def money_earnt(self):
    self.money += self.yearly_salary
  def pos_award_winner(self):
    self.pos_award += 1
    self.exp_mult += 0.2
  def phy_regress(self):
    for i in range(3):
      stats = ["str", "spd", "acc"]
      up = random.choice(stats)
      if up == "str":
        self.strength = self.regress_att(self.strength)
      elif up == "spd":
        self.spd = self.regress_att(self.spd)
      elif up == "acc":
        self.acc = self.regress_att(self.acc)
  def tech_regress(self):
    pass
  def morale_change(self, mor):
    self.morale += mor
    if self.morale < 1:
      self.morale = 1
    elif self.morale > 99:
      self.morale = 99
  def regress(self):
    if self.age >= (self.retirement_age - 5):
      if random.randint(1,200) < self.age:
        self.phy_regress()
        self.phy_regress()
        self.tech_regress()
  def train_phy_stats(self):
    for i in range(3):
      stats = ["str", "spd", "acc"]
      up = random.choice(stats)
      if up == "str":
        self.strength += random.randint(1,3)
        if self.strength > 99:
          self.strength = 99
      elif up == "spd":
        self.spd += random.randint(1,3)
        if self.spd > 99:
          self.spd = 99
      elif up == "acc":
        self.acc += random.randint(1,3)
        if self.acc > 99:
          self.acc = 99
  def train_tech_stats(self):
    pass
  def next_upgrade_exp(self):
    pass
  def level_up(self):
    self.train_phy_stats()
    self.train_tech_stats()
    self.exp -= self.next_level_exp 
    self.next_upgrade_exp()
  def print_att(self):
    print("Name-", self.name, "Spd -", self.spd, "Acc -", self.acc, "Str -", self.strength, "Awr -", self.awr, "Inj -", self.inj, "Is Rookie? -", self.rookie)
    
  def round_ovr(self):
    self.ovr = round(self.ovr)

  def cal_contract_wanted(self):
    pass

  def contract_decision(self, money, years):
    pass

  def awards(self):
    print("SBs:", self.sbs, "Pro Bowls", self.pro_bowls, "Pos Awards", self.pos_award, "MVPs:", self.mvps, "Conf Champs:", self.conf_champs, "Div Titles:", self.div_titles)
    
  def earn(self):
    self.money += round(((self.yearly_salary)/32),2)
  def exp_gain(self, exp):
    self.exp += round(exp * self.exp_mult)
    if self.exp >= self.next_level_exp:
      self.train_phy_stats()
      self.train_tech_stats()
      self.train_tech_stats()
      self.exp -= self.next_level_exp
      self.next_level_exp = round(self.next_level_exp * 1.5 * (self.age/25))
      self.level += 1

  def retire(self):
    if self.age >= self.retirement_age:
      self.retired = True
      self.contract_years = 0
    
  def end_of_year(self): #A method that will update the Player object at the end of every season 
    self.age += 1
    self.games_szn = 0
    self.regress()
    self.regress()
    self.retire()

  def update_stats(self):
    pass
    
  
class Offense(Player):
  def __init__(self, pos, name, spd, acc, str, awr, rookie, inj, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, inj, rookie, idx, age)
    self.OPOY = 0
    self.OROY = False
  def OROY_winner(self):
    self.OROY = True
  def OPOY_winner(self):
    self.OPOY += 1

  def all_attr(self):
    self.attr = []
    self.attr.append(self.spd)
    self.attr.append(self.acc)
    self.attr.append(self.strength)
    self.attr.append(self.awr)


class OL(Offense):
  def __init__(self, pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, inj, rookie, idx, age)
    self.pb = pb
    self.rb = rb
    
    self.sacks_allowed = 0
    self.sacks_allowed_szn = 0
    self.passing_snaps = 0
    self.passing_snaps_szn = 0
    self.rushing_snaps = 0

    self.rushing_snaps_szn = 0
    self.rushing_yards_blocked = 0
    self.rushing_yards_blocked_szn = 0
    self.avg_rush_szn = 0
    self.avg_rush = 0
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "Rb", "Pb"]

  def all_attr(self):
    super().all_attr()
    self.attr.append(self.rb)
    self.attr.append(self.pb)
    self.ratings = [self.attr_names, self.attr]

  def tech_regress(self):
    stats = ["awr", "rb", "pb"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.regress_att(self.awr)
      elif up == "rb":
        self.rb = self.regress_att(self.rb)
      elif up == "pb":
        self.pb = self.regress_att(self.pb)
  def train_tech_stats(self):
    stats = ["awr", "rb", "pb"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.upgrade_att(self.awr)
      elif up == "rb":
        self.rb = self.upgrade_att(self.rb)
      elif up == "pb":
        self.pb = self.upgrade_att(self.pb)
    
  def update_stats(self, team_rushing_yards, sacks_allowed, passing_snaps, rushing_snaps):
    self.sacks_allowed_szn += sacks_allowed
    self.rushing_yards_szn += team_rushing_yards
    self.passing_snaps_szn += passing_snaps
    self.rushing_snaps_szn += rushing_snaps
    self.rushing_yards_blocked_szn += team_rushing_yards
    self.avg_rush_szn = self.rushing_yards_szn/self.rushing_snaps_szn
    self.games_szn += 1

class C(OL):
  def __init__(self, pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age)
    self.retirement_age = 38
    self.pos_sal_avg = 3.5 * (10**6)
  def cal_ovr(self):
    strength = 10
    speed = 0.5
    acc = 1
    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)
    pb = 8
    rb = 10
    self.tech_ovr = (self.pb * pb + self.rb *rb)/(pb+rb)
    phy = 8
    tech = 8
    mor = 0.01
    awr = 5
    men = 0.1
    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/ (awr + mor)
    self.ovr = round((self.phy_ovr * phy + self.tech_ovr * tech + self.mental_ovr * men)/(phy+tech+men))
    self.all_attr()

class T(OL):
  def __init__(self, pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age)
    self.pos_sal_avg = 7 * (10**6)
    self.retirement_age = 35
  def cal_ovr(self):
    strength = 9
    speed = 1.5
    acc = 2.5
    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)
    pb = 10
    rb = 7
    self.tech_ovr = (self.pb * pb + self.rb *rb)/(pb+rb)
    phy = 7
    tech = 10
    mor = 0.01
    awr = 4
    men = 0.1
    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/ (awr + mor)
    self.ovr = round((self.phy_ovr*phy + self.tech_ovr * tech + self.mental_ovr* men)/(phy+tech+men))
    self.all_attr()
    
class G(OL):
  def __init__(self, pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age)
    self.pos_sal_avg = 3.5 * (10**6)
    self.retirement_age = 38
  def cal_ovr(self):
    strength = 10
    speed = 0.5
    acc = 1
    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)
    pb = 6
    rb = 10
    self.tech_ovr = (self.pb * pb + self.rb *rb)/(pb+rb)
    phy = 9
    tech = 6
    mor = 0.01
    awr = 3
    men = 0.1
    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/ (awr + mor)
    self.ovr = round((self.phy_ovr *phy + self.tech_ovr * tech + self.mental_ovr* men)/(phy+tech+men))
    self.all_attr()
      
class QB(Offense):
  def __init__(self, pos, name, spd, acc, str, car, awr, p_acc, p_str, br_sk, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, rookie, inj, idx, age)
    self.pos_sal_avg = 18 * (10**6)
    self.retirement_age = 40
    self.p_str = p_str
    self.passing_att_szn = 0
    self.p_acc = p_acc
    self.br_sk = br_sk
    self.car = car
    self.passing_att = 0
    self.passing_yards = 0
    self.passing_yards_szn = 0
    self.comps = 0
    self.comps_szn = 0
    
    self.sacked = 0
    self.sacked_szn = 0
    
    self.rushing_att = 0
    self.rushing_att_szn = 0
    self.rushing_yards = 0
    self.rushing_yards_szn = 0

    self.p_tds_szn = 0
    self.p_tds = 0
    self.rushing_tds_szn = 0
    self.rushing_tds = 0
    self.fumbles = 0
    self.fumbles_szn = 0

    
    self.ints = 0
    self.ints_szn = 0
    self.pick_six = 0
    self.pick_six_szn = 0
    self.avg_rush_szn = 0
    self.yards_per_att_szn = 0
    self.avg_rush = 0
    self.yards_per_att = 0

    self.yards_per_car_szn = 0
    self.yards_per_car = 0
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "P Acc", "P Str", "Car", "Br Sk"]


  def train_tech_stats(self):
    stats = ["awr", "p acc", "p str", "car", "br sk"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr += random.randint(1,3)
        if self.awr> 99:
          self.awr = 99
      elif up == "p acc":
        self.p_acc += random.randint(1,3)
        if self.p_acc > 99:
          self.p_acc = 99
      elif up == "p str":
        self.p_str = self.upgrade_att(self.p_str)
      elif up == "car":
        self.car = self.upgrade_att(self.car)
      elif up == "br sk":
        self.br_sk = self.upgrade_att(self.br_sk)

  def regress_tech(self):
    stats = ["awr", "p acc", "p str", "car", "br sk"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.regress_att(self.awr)
      elif up == "p acc":
        self.p_acc = self.regress_att(self.p_acc)
      elif up == "p str":
        self.p_str = self.regress_att(self.p_str)
      elif up == "car":
        self.car = self.regress_att(self.car)
      elif up == "br sk":
        self.br_sk = self.regress_att(self.br_sk)
      
  def update_stats(self, passing_snaps, comps, passing_yards, rushing_snaps, rushing_yards, sacks, p_tds, r_tds, ints, pick_six, fumbles): #passes in stats from games and updates szn stats
    self.sacked_szn += sacks
    self.rushing_yards_szn += rushing_yards
    self.rushing_att_szn += rushing_snaps
    self.avg_rush_szn = self.rushing_yards_szn/self.rushing_att_szn
    self.passing_att_szn += passing_snaps
    self.comps_szn += comps
    self.passing_yards_szn += passing_yards
    self.yards_per_att = self.passing_yards_szn/self.passing_att_szn
    self.p_tds_szn += p_tds
    self.rushing_tds_szn += r_tds
    self.ints_szn += ints
    self.yards_per_car_szn = self.rushing_yards_szn/self.rushing_att_szn
    self.games_szn += 1

  def show_stats(self):
    print(self.sacks_szn, "times sacked")
    print(self.rushing_yards_szn, "rushing yards")
    print(self.rushing_snaps_szn, "rushings attempts")
    print(self.avg_rush_szn, "rushing avg") 
    print(self.passing_att_szn, "pass attempts")
    print(self.comps_szn, "comps")
    print(self.passing_yards_szn, "passing yards")
    print(self.avg_pass_szn, "passing yards per att")
    print(self.p_tds_szn, "passing touchdowns")
    print(self.r_tds_szn, "rushing touchdowns")
    print(self.ints_szn, "ints") 
    print(self.games_szn, "games") 

  def all_attr(self):
    super().all_attr()
    self.attr.append(self.p_str)
    self.attr.append(self.p_acc)
    self.attr.append(self.car)
    self.attr.append(self.br_sk)
    self.ratings = [self.attr_names, self.attr]
    
  def cal_ovr(self):
    p_str = 9
    p_acc = 10
    br_sk = 1.5
    awr = 8
    mor = 1
    men = 5
    strength = 4
    speed = 3
    acc = 1.5
    car = 1
    phy = 8
    tech = 9

    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)

    self.tech_ovr = (self.p_str * p_str + self.p_acc * p_acc + self.br_sk * br_sk + self.car * car)/ (p_str + p_acc + br_sk + car)

    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/ (awr + mor)

    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy+tech+men))

    self.all_attr()
    
class WR(Offense):
  def __init__(self, pos, name, spd, acc, str, rtr, cat, rb, car, awr, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, rookie, idx, inj, age)
    self.pos_sal_avg = 9.6 * (10**6)
    self.retirement_age = 33
    self.rtr = rtr
    self.cat = cat
    self.rb = rb
    self.car = car
    self.rec_yards = 0
    self.rec_yards_szn = 0
    self.rec_tds_szn = 0
    self.targets_szn = 0
    self.catches_szn = 0
    self.rec_tds = 0
    self.catches = 0
    self.targets = 0
    self.fumbles = 0
    self.fumbles_szn = 0
    self.rec_ovr = 0
    self.block_ovr = 0
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "Rb", "Car", "Rtr", "Cat"]


  def train_tech_stats(self):
    stats = ["awr", "rb", "car", "rtr", "cat"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.upgrade_att(self.awr)
      elif up == "rb":
        self.rb = self.upgrade_att(self.rb)
      elif up == "car":
        self.car = self.upgrade_att(self.car)
      elif up == "rtr":
        self.rtr = self.upgrade_att(self.rtr)
      elif up == "cat":
        self.cat = self.upgrade_att(self.cat)

  def regress_tech(self):
    stats = ["awr", "rb", "car", "rtr", "cat"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.regress_att(self.awr)
      elif up == "rb":
        self.rb = self.regress_att(self.rb)
      elif up == "car":
        self.car = self.regress_att(self.car)
      elif up == "rtr":
        self.rtr = self.regress_att(self.rtr)
      elif up == "cat":
        self.cat = self.regress_att(self.cat)
        
          
  def update_stats(self, yards, tds, targets, catches, fumbles):
    self.rec_yards_szn += yards
    self.rec_tds_szn += tds
    self.catches_szn += catches
    self.targets_szn += targets 
    self.fumbles_szn += fumbles
    self.games_szn += 1

  def all_attr(self):
    super().all_attr()
    self.attr.append(self.rb)
    self.attr.append(self.car)
    self.attr.append(self.rtr)
    self.attr.append(self.cat)
    self.ratings = [self.attr_names, self.attr]
    
  def cal_ovr(self):
    blocking = 3
    rec = 10
    strength = 5
    speed = 9
    acc = 10
    rtr = 10
    cat = 10
    ###
    car = 1
    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)
    self.blocking_ovr = self.rb
    self.rec_ovr = (self.rtr * rec + self.cat * cat)/ (rtr + cat)
    self.tech_ovr = (self.blocking_ovr*blocking + self.rec_ovr*rec)/(blocking + rec)
    phy = 10
    tech = 9
    mor = 0.01
    awr = 3
    men = 0.1
    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/(awr+mor)
    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy+tech+men))
    self.all_attr()

### RB is not a WR
class RB(Offense):
  def __init__(self, pos, name, spd, acc, str, rtr, cat, pb, car, awr, inj, rookie, idx, rb, age):
    super().__init__(pos, name, spd, acc, str, awr, rookie, idx, inj, age)
    self.pos_sal_avg = 4 * (10**6)
    self.retirement_age = 30
    self.pb = pb
    self.rtr = rtr
    self.cat = cat
    self.rb = rb
    self.car = car
    self.rec_yards = 0
    self.rec_yards_szn = 0
    self.rec_tds_szn = 0
    self.targets_szn = 0
    self.catches_szn = 0
    self.rec_tds = 0
    self.catches = 0
    self.targets = 0
    
    self.rushing_yards_szn = 0
    self.rushing_att_szn = 0
    self.rushing_yards = 0
    self.rushing_tds_szn = 0
    self.rushing_tds = 0
    self.rushing_att = 0

    self.rec_ovr = 0
    self.rush = 0
    self.block_ovr = 0
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "Rb", "Pb", "Car", "Rtr", "Cat"]

  def train_tech_stats(self):
    stats = ["awr", "rb", "pb", "car", "rtr", "cat"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.upgrade_att(self.awr)
      elif up == "rb":
        self.rb = self.upgrade_att(self.rb)
      elif up == "pb":
        self.pb = self.upgrade_att(self.pb)
      elif up == "car":
        self.car = self.upgrade_att(self.car)
      elif up == "rtr":
        self.rtr = self.upgrade_att(self.rtr)
      elif up == "cat":
        self.cat = self.upgrade_att(self.cat)

  def regress_tech(self):
    stats = ["awr", "rb", "pb", "car", "rtr", "cat"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.regress_att(self.awr)
      elif up == "rb":
        self.rb = self.regress_att(self.rb)
      elif up == "pb":
        self.pb = self.regress_att(self.pb)
      elif up == "car":
        self.car = self.regress_att(self.car)
      elif up == "rtr":
        self.rtr = self.regress_att(self.rtr)
      elif up == "cat":
        self.cat = self.regress_att(self.cat)

  def all_attr(self):
    super().all_attr()
    self.attr.append(self.rb)
    self.attr.append(self.pb)
    self.attr.append(self.car)
    self.attr.append(self.rtr)
    self.attr.append(self.cat)
    self.ratings = [self.attr_names, self.attr]

  
  def update_stats(self, yards, tds, targets, catches, atts, r_tds, r_yards):
    self.rushing_att_szn + atts
    self.rushing_yards_szn += yards
    self.rushing_tds += tds
    self.targets_szn += targets 
    self.catches_szn += catches
    self.rec_yards_szn = r_yards
    self.rec_tds_szn += r_tds
    self.games_szn += 1

  def cal_ovr(self):
    blocking = 3
    rec = 5
    rush = 10
    strength = 5
    cat = 4
    speed = 9
    acc = 10
    rtr = 10
    car = 7
    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)
    pb = 5
    rb = 0.1
    self.blocking_ovr = (self.rb * rb + self.pb * pb)/ (rb + pb)
    self.rec_ovr = (self.rtr * rec + self.cat * cat)/ (rtr + cat)
    self.tech_ovr = (self.blocking_ovr*blocking + self.rec_ovr*rec + self.car * car)/(blocking + rec + car)
    phy = 10
    tech = 3
    mor = 0.01
    awr = 9
    men = 0.1
    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/(awr+mor)
    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy+tech+men))
    self.all_attr()

### TE is not a WR

class TE(OL):
  def __init__(self, pos, name, spd, acc, str, pb, rb, rtr, cat, car, awr, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, pb, rb, awr, inj, rookie, idx, age)
    self.pos_sal_avg = 6 * (10**6)
    self.retirement_age = 36
    self.rtr = rtr
    self.cat = cat
    self.rb = rb
    self.pb = pb
    self.car = car
    self.cat = cat

    self.rec_yards = 0
    self.rec_yards_szn = 0
    self.rec_tds_szn = 0
    self.targets_szn = 0
    self.catches_szn = 0
    self.rec_tds = 0
    self.catches = 0
    self.targets = 0

    self.rec_ovr = 0
    self.block_ovr = 0
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "Rb", "Pb", "Car", "Rtr", "Cat"]

  def train_tech_stats(self):
    stats = ["awr", "rb", "pb", "car", "rtr", "cat"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.upgrade_att(self.awr)
      elif up == "rb":
        self.rb = self.upgrade_att(self.rb)
      elif up == "pb":
        self.pb = self.upgrade_att(self.pb)
      elif up == "car":
        self.car = self.upgrade_att(self.car)
      elif up == "rtr":
        self.rtr = self.upgrade_att(self.rtr)
      elif up == "cat":
        self.cat = self.upgrade_att(self.cat)

  def regress_tech(self):
    stats = ["awr", "rb", "pb", "car", "rtr", "cat"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.regress_att(self.awr)
      elif up == "rb":
        self.rb = self.regress_att(self.rb)
      elif up == "pb":
        self.pb = self.regress_att(self.pb)
      elif up == "car":
        self.car = self.regress_att(self.car)
      elif up == "rtr":
        self.rtr = self.regress_att(self.rtr)
      elif up == "cat":
        self.cat = self.regress_att(self.cat)
  
  def all_attr(self):
    super().all_attr()
    self.attr.append(self.car)
    self.attr.append(self.rtr)
    self.attr.append(self.cat)
    self.ratings = [self.attr_names, self.attr]
  def cal_ovr(self):
    blocking = 6
    rec = 7
    strength = 10
    speed = 8
    acc = 6
    rtr = 5
    cat = 10
    ###
    car = 1
    self.phy_ovr = ((self.strength * strength) + (self.spd * speed) + (self.acc * acc))/(strength + speed + acc)
    pb = 3
    rb = 5
    self.blocking_ovr = (self.rb * rb + self.pb * pb)/ (rb + pb)
    self.rec_ovr = (self.rtr * rec + self.cat * cat)/ (rtr + cat)
    self.tech_ovr = (self.blocking_ovr*blocking + self.rec_ovr*blocking)/(blocking + rec)
    phy = 10
    tech = 9
    mor = 0.01
    awr = 2
    men = 0.1
    self.mental_ovr = ((self.awr*awr) + (self.morale * mor))/(awr+mor)
    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy+tech+men))
    self.all_attr()

    
  def update_stats(self, team_rushing_yards, sacks_allowed, passing_snaps, rushing_snaps, yards, tds, targets, catches):
      self.all_time_sacks += sacks_allowed
      self.rushing_yards += team_rushing_yards
      self.passing_snaps += passing_snaps
      self.passing_snaps_szn += passing_snaps
      self.rushing_snaps_szn += rushing_snaps
      self.rushing_snaps += rushing_snaps
      self.rushing_yards_szn += team_rushing_yards
      self.avg_rush_szn = self.rushing_yards_szn/self.rushing_snaps_szn
      self.avg_rush = self.rushing_yards.self.rushing_snaps
      self.rec_yards_szn += yards
      self.rec_tds_szn += tds
      self.catches_szn += catches
      self.targets_szn += targets 
      self.games_szn += 1
  
class Defense(Player):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, rookie, inj, idx, age)
    self.tkl = tkl
    self.pr = p_rush
    self.rd = run_d
    self.mc = mc
    self.zc = zc
    self.attr = []
    self.tackles_szn = 0
    self.picks_szn = 0
    self.pick_six_szn = 0
    self.sacks_szn = 0
    self.f_fum_szn = 0
    self.fum_rec_szn = 0
    self.f_td_szn = 0
    self.sfty_szn = 0
    self.tfl_szn = 0
    self.tackles = 0
    self.picks = 0
    self.pick_six = 0
    self.sacks = 0
    self.f_fum = 0
    self.fum_rec = 0
    self.f_td = 0
    self.sfty = 0
    self.tfl = 0
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "Tkl", "Pr", "Rd", "Mc", "Zc"]
    self.ratings = []

    self.cov = 0
    self.blitz = 0
    self.DROY = 0
    self.DPOY = 0

  def DROY_winner(self):
    self.OROY = True
  def DPOY_winner(self):
    self.OPOY += 1

  def train_tech_stats(self):
    stats = ["awr", "tkl", "pr", "rd", "mc", "zc"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.upgrade_att(self.awr)
      elif up == "tkl":
        self.tkl = self.upgrade_att(self.tkl)
      elif up == "pr":
        self.pr = self.upgrade_att(self.pr)
      elif up == "rd":
        self.rd = self.upgrade_att(self.rd)
      elif up == "mc":
        self.mc = self.upgrade_att(self.mc)
      elif up == "zc":
        self.zc = self.upgrade_att(self.zc)

  def regress_tech(self):
    stats = ["awr", "tkl", "pr", "rd", "mc", "zc"]
    for i in range(3):
      up = random.choice(stats)
      if up == "awr":
        self.awr = self.regress_att(self.awr)
      elif up == "tkl":
        self.tkl = self.regress_att(self.tkl)
      elif up == "pr":
        self.pr = self.regress_att(self.pr)
      elif up == "rd":
        self.rd = self.regress_att(self.rd)
      elif up == "mc":
        self.mc = self.regress_att(self.mc)
      elif up == "zc":
        self.zc =self.regress_att(self.zc)
  def update_stats(self, tkls, ints, pick_six, sacks, f_fum, fum_rec, f_td, sfty, tfl):
    self.tackles_szn += tkls
    self.picks_szn += ints
    self.sacks_szn += sacks
    self.f_fum_szn += f_fum
    self.fum_rec_szn += fum_rec
    self.f_td_szn += f_td
    self.sfty_szn += sfty
    self.tfl_szn += tfl
    self.games_szn += 1

  def update_stats_year(self):
    self.tackles += self.tackles_szn
    self.picks += self.picks_szn
    self.sacks += self.sacks_szn
    self.f_fum += self.f_fum_szn
    self.fum_rec += self.fum_rec_szn
    self.f_td += self.f_td_szn
    self.sfty += self.sfty_szn
    self.tfl += self.tfl_szn
    self.games += self.games_szn
    self.tackles_szn = 0
    self.picks_szn = 0
    self.pick_six_szn = 0
    self.sacks_szn = 0
    self.f_fum_szn = 0
    self.fum_rec_szn = 0
    self.f_td_szn = 0
    self.sfty_szn = 0
    self.tfl_szn = 0
    

  def all_attr(self):
    self.attr = []
    self.ratings = []
    self.attr.append(self.spd)
    self.attr.append(self.acc)
    self.attr.append(self.strength)
    self.attr.append(self.awr)
    self.attr.append(self.tkl)
    self.attr.append(self.pr)
    self.attr.append(self.rd)
    self.attr.append(self.mc)
    self.attr.append(self.zc)
    self.ratings = [self.attr_names, self.attr]

class DE(Defense):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age)
    self.pos_sal_avg = 11 * (10**6)
    self.retirement_age = 36
  def cal_ovr(self):
    speed = 7
    blitz = 10
    phy = 9
    acc = 7
    tkl = 7
    strength = 9
    pr = 10
    rd = 7
    mc = 1
    zc = 9
    awr = 2
    mor = 0.01
    men = 1
    cov = 0.5
    tech = 9
    self.phy_ovr = (self.spd*speed + self.acc*acc + self.strength*strength)/ (speed + acc + strength)
    self.cov_ovr = (self.mc*mc + self.zc*zc)/(mc + zc)
    
    self.blitz_ovr = (self.pr*pr + self.rd*rd)/(pr + rd)
    
    self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr + mor)
    
    self.tech_ovr = ((self.cov_ovr * cov) + (self.blitz_ovr * blitz) + self.tkl * tkl)/(cov+blitz + tkl)
    
    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy+ tech + men))

    self.all_attr()

class DT(Defense):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age)
    self.pos_sal_avg = 8 * (10**6)
    self.retirement_age = 38
  def cal_ovr(self):
    speed = 3
    blitz = 10
    tkl = 7
    phy = 10
    acc = 7
    strength = 10
    pr = 6
    rd = 10
    mc = 1
    zc = 6
    awr = 2
    mor = 0.01
    men = 1
    cov = 0.01
    tech = 7
    self.phy_ovr = (self.spd*speed + self.acc*acc + self.strength*strength)/ (speed + acc + strength)
    self.cov_ovr = (self.mc*mc + self.zc*zc)/(mc + zc)

    self.blitz_ovr = (self.pr*pr + self.rd*rd)/(pr + rd)

    self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr + mor)

    self.tech_ovr = ((self.cov_ovr * cov) + (self.blitz_ovr * blitz) + self.tkl * tkl)/(cov+blitz + tkl)

    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy +tech + men))
    self.all_attr()

class ILB(Defense):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age)
    self.pos_sal_avg = 7.5 * (10**6)
    self.retirement_age = 36
  def cal_ovr(self):
    speed = 8
    blitz = 6
    phy = 9
    acc = 7
    strength = 9
    pr = 5
    tkl = 10
    rd = 8
    mc = 7
    zc = 8
    awr = 10
    mor = 0.01
    men = 10
    cov = 8
    tech = 9
    self.phy_ovr = (self.spd*speed + self.acc*acc + self.strength*strength)/ (speed + acc + strength)
    self.cov_ovr = (self.mc*mc + self.zc*zc)/(mc + zc)

    self.blitz_ovr = (self.pr*pr + self.rd*rd)/(pr + rd)

    self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr + mor)

    self.tech_ovr = ((self.cov_ovr * cov) + (self.blitz_ovr * blitz) + self.tkl * tkl)/(cov+blitz + tkl)

    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy +tech + men))
    self.all_attr()

class OLB(Defense):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc,inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age)
    self.pos_sal_avg = 12 * (10**6)
    self.retirement_age = 37
  def cal_ovr(self):
    speed = 8
    blitz = 8
    phy = 9
    acc = 7
    strength = 9
    pr = 8
    rd = 6
    mc = 7
    zc = 8
    awr = 10
    mor = 0.01
    tkl = 10
    men = 5
    cov = 6.5
    tech = 9
    self.phy_ovr = (self.spd*speed + self.acc*acc + self.strength*strength)/ (speed + acc + strength)
    self.cov_ovr = (self.mc*mc + self.zc*zc)/(mc + zc)

    self.blitz_ovr = (self.pr*pr + self.rd*rd)/(pr + rd)

    self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr + mor)
    
    self.tech_ovr = ((self.cov_ovr * cov) + (self.blitz_ovr * blitz) + self.tkl * tkl)/(cov+blitz + tkl)

    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy + tech + men))
    self.all_attr()

class CB(Defense):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age)
    self.pos_sal_avg = 9 * (10**6)
    self.retirement_age = 33
  def cal_ovr(self):
    speed = 10
    blitz = 3
    phy = 10
    acc = 7
    strength = 6
    pr = 4
    rd = 5
    mc = 10
    zc = 9
    awr = 6
    mor = 0.01
    men = 5
    tkl = 6
    cov = 10
    tech = 10
    self.phy_ovr = (self.spd*speed + self.acc*acc + self.strength*strength)/ (speed + acc + strength)
    self.cov_ovr = (self.mc*mc + self.zc*zc)/(mc + zc)

    self.blitz_ovr = (self.pr*pr + self.rd*rd)/(pr + rd)

    self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr + mor)

    self.tech_ovr = ((self.cov_ovr * cov) + (self.blitz_ovr * blitz) + self.tkl * tkl)/(cov+blitz + tkl)

    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy+ tech + men))
    self.all_attr()

class S(Defense):
  def __init__(self, pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc,inj, rookie, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, tkl, p_rush, run_d, mc, zc, rookie, inj, idx, age)
    self.pos_sal_avg = 5.5 * (10**6)
    self.retirement_age = 35
  def cal_ovr(self):
    speed = 6
    blitz = 4
    phy = 6
    acc = 6
    strength = 7
    pr = 4
    rd = 5
    mc = 10
    zc = 9
    awr = 8
    mor = 0.01
    men = 8
    cov = 10
    tkl = 8
    tech = 7
    self.phy_ovr = (self.spd*speed + self.acc*acc + self.strength*strength)/ (speed + acc + strength)
    self.cov_ovr = (self.mc*mc + self.zc*zc)/(mc + zc)

    self.blitz_ovr = (self.pr*pr + self.rd*rd)/(pr + rd)

    self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr + mor)

    self.tech_ovr = ((self.cov_ovr * cov) + (self.blitz_ovr * blitz) + self.tkl * tkl)/(cov+blitz + tkl)

    self.ovr = round((self.phy_ovr*phy + self.tech_ovr*tech + self.mental_ovr*men)/(phy + tech + men))
    self.all_attr()
class ST(Player):
  def __init__(self, pos, name, spd, acc, str, awr, inj, rookie, kp, ka, idx, age):
    super().__init__(pos, name, spd, acc, str, awr, inj, rookie, idx, age)
    self.retirement_age = 45
    self.ka = ka
    self.kp = kp
    self.attr_names = ["Spd", "Acc", "Str", "Awr", "Kp", "Ka"]
    self.pos_sal_avg = 1.75 * (10**6)
  def all_attr(self):
    self.attr = []
    self.attr.append(self.spd)
    self.attr.append(self.acc)
    self.attr.append(self.strength)
    self.attr.append(self.awr)
    self.attr.append(self.kp)
    self.attr.append(self.ka)
    self.ratings = [self.attr_names, self.attr]
  def cal_ovr(self):
    if self.pos == "K":
      ka = 2
      kp = 1
      tech = 10
      men = 5
      awr = 7
      mor = 0.01
      self.tech_ovr = (self.ka*ka + self.kp*kp)/(ka+kp)
      self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr+mor)
      self.ovr = round((self.tech_ovr*tech + self.mental_ovr*men)/(tech+men))
    else:
      ka = 1
      kp = 2
      tech = 10
      men = 5
      awr = 7
      mor = 0.01
      self.tech_ovr = (self.ka*ka + self.kp*kp)/(ka+kp)
      self.mental_ovr = (self.awr*awr + self.morale*mor)/(awr+mor)
      self.ovr = round((self.tech_ovr*tech + self.mental_ovr*men)/(tech+men))
    self.phy_ovr =  (self.spd*10 + self.acc*7 + self.strength*6)/(10+7+6)
    self.all_attr()

  def train_tech_stats(self):
    stats = ["awr","kp", "ka"]
    for i in range(3):
      up = random.choice(stats)
      if up == "kp":
        self.kp = self.upgrade_att(self.kp)
      elif up == "ka":
        self.ka = self.upgrade_att(self.ka)
      elif up == "awr":
        self.awr = self.upgrade_att(self.awr)

  def regress_tech(self):
    stats = ["awr", "kp", "ka"]
    for i in range(3):
      up = random.choice(stats)
      if up == "kp":
        self.kp = self.regress_att(self.kp)
      elif up == "ka":
        self.ka = self.regress_att(self.ka)
      elif up == "awr":
        self.awr = self.regress_att(self.awr)