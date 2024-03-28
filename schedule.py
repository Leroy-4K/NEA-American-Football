## generates divisional games using modulo
def gen_div_games(nfl, i):
  return [
      [nfl.afc_north[3], nfl.afc_north[i%3]],
      [nfl.afc_north[(i+1)%3], nfl.afc_north[(i+2)%3]],

      [nfl.afc_east[3], nfl.afc_east[i%3]],
      [nfl.afc_east[(i+1)%3], nfl.afc_east[(i+2)%3]],

      [nfl.afc_south[3], nfl.afc_south[i%3]],
      [nfl.afc_south[(i+1)%3], nfl.afc_south[(i+2)%3]], 
    
      [nfl.afc_west[3], nfl.afc_west[i%3]],
      [nfl.afc_west[(i+1)%3], nfl.afc_west[(i+2)%3]],

      [nfl.nfc_north[3], nfl.nfc_north[i%3]],
      [nfl.nfc_north[(i+1)%3], nfl.nfc_north[(i+2)%3]], 
  
      [nfl.nfc_east[3], nfl.nfc_east[i%3]],
      [nfl.nfc_east[(i+1)%3], nfl.nfc_east[(i+2)%3]], 
    
      [nfl.nfc_south[3], nfl.nfc_south[i%3]],
      [nfl.nfc_south[(i+1)%3], nfl.nfc_south[(i+2)%3]],
  
      [nfl.nfc_west[3], nfl.nfc_west[i%3]],
      [nfl.nfc_west[(i+1)%3], nfl.nfc_west[(i+2)%3]]

    ]

## generate the rest by passing the divisions in different orders
def gen_conf_div_games(divA, divB, divC, divD, divE, divF, divG, divH, i):

  l = [
    [divA[0], divB[i % 4]],
    [divA[1], divB[(i + 1) % 4]],
    [divA[2], divB[(i + 2) % 4]],
    [divA[3], divB[(i + 3) % 4]], 

    [divC[0], divD[i % 4]],
    [divC[1], divD[(i + 1) % 4]],
    [divC[2], divD[(i + 2) % 4]],
    [divC[3], divD[(i + 3) % 4]], 

    [divE[0], divF[i % 4]],
    [divE[1], divF[(i + 1) % 4]],
    [divE[2], divF[(i + 2) % 4]],
    [divE[3], divF[(i + 3) % 4]], 

    [divG[0], divH[i % 4]],
    [divG[1], divH[(i + 1) % 4]],
    [divG[2], divH[(i + 2) % 4]],
    [divG[3], divH[(i + 3) % 4]] 
    ]
  return l

## can switch the home and away team
def switch_home_away(array):
  temp = array[0]
  array[0] = array[1]
  array[1] = temp
  return array
## can switch the home and away team for the entire week
def switch_home_away_for_week(array):
  for j in range(len(array)):
    temp = array[0]
    array[0] = array[1]
    array[1] = temp
  return array

## generates the nfl schedule based on the year, since the way games are generated depends on two cycles
def generate_sch(year, nfl):

  conf = (year - 2023 ) % 3
  iconf = (year - 2023 ) % 4

  nfl.week1 = gen_div_games(nfl, 0)
  nfl.week2 = gen_div_games(nfl, 1)
  nfl.week3 = gen_div_games(nfl, 2)
  nfl.week4 = switch_home_away_for_week(nfl.week1)
  nfl.week5 = switch_home_away_for_week(nfl.week2)
  nfl.week6 = switch_home_away_for_week(nfl.week3)


  if conf == 0:
    # nfc south  vs nfc north: afc south vs afc north
    nfl.week7 = gen_conf_div_games(nfl.afc_north, nfl.afc_south, nfl.afc_east, nfl.afc_west, nfl.nfc_west, nfl.nfc_east, nfl.nfc_north, nfl.nfc_south, 0)
    nfl.week8 = gen_conf_div_games(nfl.afc_north, nfl.afc_south, nfl.afc_east, nfl.afc_west, nfl.nfc_west, nfl.nfc_east, nfl.nfc_north, nfl.nfc_south, 1)
    nfl.week9 = gen_conf_div_games(nfl.afc_north, nfl.afc_south, nfl.afc_east, nfl.afc_west, nfl.nfc_west, nfl.nfc_east, nfl.nfc_north, nfl.nfc_south, 2)
    nfl.week10 = gen_conf_div_games(nfl.afc_north, nfl.afc_south, nfl.afc_east, nfl.afc_west, nfl.nfc_west, nfl.nfc_east, nfl.nfc_north, nfl.nfc_south, 3)
    

    # Other teams same pos in conf
    nfl.week15 = gen_conf_div_games(nfl.afc_north, nfl.afc_west, nfl.afc_east, nfl.afc_south, nfl.nfc_west, nfl.nfc_north, nfl.nfc_east, nfl.nfc_south, 0)
    nfl.week16 = gen_conf_div_games(nfl.afc_north, nfl.afc_east, nfl.afc_west, nfl.afc_south, nfl.nfc_west, nfl.nfc_south, nfl.nfc_east, nfl.nfc_north, 0)
  elif conf == 1:
    # souths vs wests
    nfl.week7 = gen_conf_div_games(nfl.afc_west, nfl.afc_south, nfl.afc_east, nfl.afc_north, nfl.nfc_west, nfl.nfc_south, nfl.nfc_east, nfl.nfc_north, 0)
    nfl.week8 = gen_conf_div_games(nfl.afc_west, nfl.afc_south, nfl.afc_east, nfl.afc_north, nfl.nfc_west, nfl.nfc_south, nfl.nfc_east, nfl.nfc_north, 1)
    nfl.week9 = gen_conf_div_games(nfl.afc_west, nfl.afc_south, nfl.afc_east, nfl.afc_north, nfl.nfc_west, nfl.nfc_south, nfl.nfc_east, nfl.nfc_north, 2)
    nfl.week10 = gen_conf_div_games(nfl.afc_west, nfl.afc_south, nfl.afc_east, nfl.afc_north, nfl.nfc_west, nfl.nfc_south, nfl.nfc_east, nfl.nfc_north, 3)

    # other teams same conf same pos
    nfl.week15 = gen_conf_div_games(nfl.afc_west, nfl.afc_east, nfl.afc_south, nfl.afc_north, nfl.nfc_west, nfl.nfc_east, nfl.nfc_south, nfl.nfc_north, 0)
    nfl.week16 = gen_conf_div_games(nfl.afc_west, nfl.afc_north, nfl.afc_south, nfl.afc_east, nfl.nfc_west, nfl.nfc_north, nfl.nfc_east, nfl.nfc_south, 0)

  else:
    # souths vs easts 

    nfl.week7 = gen_conf_div_games(nfl.afc_east, nfl.afc_south, nfl.afc_west, nfl.afc_north, nfl.nfc_east, nfl.nfc_south, nfl.nfc_west, nfl.nfc_north, 0)
    nfl.week8 = gen_conf_div_games(nfl.afc_east, nfl.afc_south, nfl.afc_west, nfl.afc_north, nfl.nfc_east, nfl.nfc_south, nfl.nfc_west, nfl.nfc_north, 1)
    nfl.week9 = gen_conf_div_games(nfl.afc_east, nfl.afc_south, nfl.afc_west, nfl.afc_north, nfl.nfc_east, nfl.nfc_south, nfl.nfc_west, nfl.nfc_north, 2)
    nfl.week10 = gen_conf_div_games(nfl.afc_east, nfl.afc_south, nfl.afc_west, nfl.afc_north, nfl.nfc_east, nfl.nfc_south, nfl.nfc_west, nfl.nfc_north, 3)
    

    ################

    nfl.week15 = gen_conf_div_games(nfl.afc_east, nfl.afc_west, nfl.afc_south, nfl.afc_north, nfl.nfc_east, nfl.nfc_west, nfl.nfc_south, nfl.nfc_north, 0)
    nfl.week16 = gen_conf_div_games(nfl.afc_east, nfl.afc_north, nfl.afc_west, nfl.afc_south, nfl.nfc_east, nfl.nfc_north, nfl.nfc_west, nfl.nfc_south, 0)

  if iconf == 0:
    # ns vs as, nw vs an, aw vs nn, ne vs ae
    nfl.week11 = gen_conf_div_games(nfl.nfc_south, nfl.afc_south, nfl.afc_west, nfl.nfc_north, nfl.afc_east, nfl.nfc_east, nfl.nfc_west, nfl.afc_north, 0)
    nfl.week12 = gen_conf_div_games(nfl.nfc_south, nfl.afc_south, nfl.afc_west, nfl.nfc_north, nfl.afc_east, nfl.nfc_east, nfl.nfc_west, nfl.afc_north, 1)
    nfl.week13 = gen_conf_div_games(nfl.nfc_south, nfl.afc_south, nfl.afc_west, nfl.nfc_north, nfl.afc_east, nfl.nfc_east, nfl.nfc_west, nfl.afc_north, 2)
    nfl.week14 = gen_conf_div_games(nfl.nfc_south, nfl.afc_south, nfl.afc_west, nfl.nfc_north, nfl.afc_east, nfl.nfc_east, nfl.nfc_west, nfl.afc_north, 3)
    
  ## 17th ns : east, north, south, west
  ## 17th as: west, east ,south, north
  ## 17th nw: south, north, north, east
  # pos based matchups 
    nfl.week17 = gen_conf_div_games(nfl.nfc_south, nfl.afc_east, nfl.afc_west, nfl.nfc_east, nfl.afc_south, nfl.nfc_west, nfl.afc_north, nfl.nfc_north, 0)
     ## 17th for iconf = 1,2,else
  elif iconf == 1:
    # ns vs aw, nw vs ae, as vs nn, ne vs an
    nfl.week11 = gen_conf_div_games(nfl.nfc_north, nfl.afc_south, nfl.afc_west, nfl.nfc_south, nfl.afc_east, nfl.nfc_west, nfl.nfc_east, nfl.afc_north, 0)
    nfl.week12 = gen_conf_div_games(nfl.nfc_north, nfl.afc_south, nfl.afc_west, nfl.nfc_south, nfl.afc_east, nfl.nfc_west, nfl.nfc_east, nfl.afc_north, 1)
    nfl.week13 = gen_conf_div_games(nfl.nfc_north, nfl.afc_south, nfl.afc_west, nfl.nfc_south, nfl.afc_east, nfl.nfc_west, nfl.nfc_east, nfl.afc_north, 2)
    nfl.week14 = gen_conf_div_games(nfl.nfc_north, nfl.afc_south, nfl.afc_west, nfl.nfc_south, nfl.afc_east, nfl.nfc_west, nfl.nfc_east, nfl.afc_north, 3)
    
    
  ## 17th ns : east, north, south, west
  ## 17th as: west, east ,south, north
  ## 17th nw: south, west, north, east
    nfl.week17 = gen_conf_div_games(nfl.afc_north, nfl.nfc_south, nfl.afc_west, nfl.nfc_west, nfl.afc_south, nfl.nfc_east, nfl.afc_east, nfl.nfc_north, 0)
  elif iconf == 2:
    # ns vs ae, "as vs nw", aw vs ne, nn vs an
    nfl.week11 = gen_conf_div_games(nfl.nfc_west, nfl.afc_south, nfl.afc_east, nfl.nfc_south, nfl.afc_west, nfl.nfc_east, nfl.nfc_north, nfl.afc_north, 0)
    nfl.week12 = gen_conf_div_games(nfl.nfc_west, nfl.afc_south, nfl.afc_east, nfl.nfc_south, nfl.afc_west, nfl.nfc_east, nfl.nfc_north, nfl.afc_north, 1)
    nfl.week13 = gen_conf_div_games(nfl.nfc_west, nfl.afc_south, nfl.afc_east, nfl.nfc_south, nfl.afc_west, nfl.nfc_east, nfl.nfc_north, nfl.afc_north, 2)
    nfl.week14 = gen_conf_div_games(nfl.nfc_west, nfl.afc_south, nfl.afc_east, nfl.nfc_south, nfl.afc_west, nfl.nfc_east, nfl.nfc_north, nfl.afc_north, 3)
    

  ## 17th ns : east, north, south, west
  ## 17th as: west, east ,south, north
  ## 17th nw: south, west, north, east
    nfl.week17 = gen_conf_div_games(nfl.afc_north, nfl.nfc_west, nfl.afc_west, nfl.nfc_north, nfl.afc_south, nfl.nfc_south, nfl.afc_east, nfl.nfc_east, 0)

  else:
    # ns vs an: as vs ne: "nw vs aw": nn vs ae

    nfl.week11 = gen_conf_div_games(nfl.nfc_south, nfl.afc_north, nfl.afc_south, nfl.nfc_east, nfl.nfc_west, nfl.afc_west, nfl.nfc_north, nfl.afc_east, 0)
    nfl.week12 = gen_conf_div_games(nfl.nfc_south, nfl.afc_north, nfl.afc_south, nfl.nfc_east, nfl.nfc_west, nfl.afc_west, nfl.nfc_north, nfl.afc_east, 1)
    nfl.week13 = gen_conf_div_games(nfl.nfc_south, nfl.afc_north, nfl.afc_south, nfl.nfc_east, nfl.nfc_west, nfl.afc_west, nfl.nfc_north, nfl.afc_east, 2)
    nfl.week14 = gen_conf_div_games(nfl.nfc_south, nfl.afc_north, nfl.afc_south, nfl.nfc_east, nfl.nfc_west, nfl.afc_west, nfl.nfc_north, nfl.afc_east, 3)
    
  ## 17th ns : east, north, south, west
  ## 17th as: west, east ,south, north
  ## 17th nw: south, west, north, east
    nfl.week17 = gen_conf_div_games(nfl.afc_north, nfl.nfc_east, nfl.afc_west, nfl.nfc_south, nfl.afc_south, nfl.nfc_north, nfl.afc_east, nfl.nfc_west, 0)
  nfl.week18 = []
  #switch games about tooo
  
  nfl.sch = [nfl.week1, nfl.week2, nfl.week3, nfl.week4, nfl.week5, nfl.week6, nfl.week7, nfl.week8, nfl.week9, nfl.week10, nfl.week11, nfl.week12, nfl.week13, nfl.week14, nfl.week15, nfl.week16, nfl.week17, nfl.week18]  
