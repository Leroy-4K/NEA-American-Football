from set_up import *
### table and label size##
table_font_size = 20
div_label_size = 15
conf_label_size = 15
### function for updating the division table ###
def weekly_standings():
  global aw, ae, aas, an, nn, ne, nw, ns
  global table_afc_east, table_afc_west, table_afc_north, table_afc_south
  global table_nfc_east, table_nfc_west, table_nfc_north, table_nfc_south

  padding = 5
  global aw_row1, aw_row2, aw_row, aw_row4, aw_row5
  global nw_row1, nw_row2, nw_row3, nw_row4, nw_row5
  # each row represents one team. each table represents one division
  ae = menu_div_standings.add.label("AFC East", font_size=div_label_size)

  table_afc_east = menu_div_standings.add.table(font_size=table_font_size)
  table_afc_east.default_cell_padding = padding
  table_afc_east.default_cell_align = pygame_menu.locals.ALIGN_CENTER

  ae_row1 = table_afc_east.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  ae_row2 = table_afc_east.add_row([AFC_EAST.teams[0].name, AFC_EAST.teams[0].wins_szn, AFC_EAST.teams[0].losses_szn, AFC_EAST.teams[0].ties_szn, AFC_EAST.teams[0].win_pct, AFC_EAST.teams[0].pts_for_szn, AFC_EAST.teams[0].pts_against_szn, AFC_EAST.teams[0].pts_for_szn - AFC_EAST.teams[0].pts_against_szn, str(AFC_EAST.teams[0].div_wins_szn) + "-" + str(AFC_EAST.teams[0].div_losses_szn) + "-" + str(AFC_EAST.teams[0].div_ties_szn)])

  ae_row3 = table_afc_east.add_row([AFC_EAST.teams[1].name, AFC_EAST.teams[1].wins_szn, AFC_EAST.teams[1].losses_szn, AFC_EAST.teams[1].ties_szn, AFC_EAST.teams[1].win_pct, AFC_EAST.teams[1].pts_for_szn, AFC_EAST.teams[1].pts_against_szn, AFC_EAST.teams[1].pts_for_szn - AFC_EAST.teams[1].pts_against_szn, str(AFC_EAST.teams[1].div_wins_szn) + "-" + str(AFC_EAST.teams[1].div_losses_szn) + "-" + str(AFC_EAST.teams[1].div_ties_szn)])

  ae_row4 = table_afc_east.add_row([AFC_EAST.teams[2].name, AFC_EAST.teams[2].wins_szn, AFC_EAST.teams[2].losses_szn, AFC_EAST.teams[2].ties_szn, AFC_EAST.teams[2].win_pct, AFC_EAST.teams[2].pts_for_szn, AFC_EAST.teams[2].pts_against_szn, AFC_EAST.teams[2].pts_for_szn - AFC_EAST.teams[2].pts_against_szn, str(AFC_EAST.teams[2].div_wins_szn) + "-" + str(AFC_EAST.teams[2].div_losses_szn) + "-" + str(AFC_EAST.teams[2].div_ties_szn)])

  ae_row5 = table_afc_east.add_row([AFC_EAST.teams[3].name, AFC_EAST.teams[3].wins_szn, AFC_EAST.teams[3].losses_szn, AFC_EAST.teams[3].ties_szn, AFC_EAST.teams[3].win_pct, AFC_EAST.teams[3].pts_for_szn, AFC_EAST.teams[3].pts_against_szn, AFC_EAST.teams[3].pts_for_szn - AFC_EAST.teams[3].pts_against_szn, str(AFC_EAST.teams[3].div_wins_szn) + "-" + str(AFC_EAST.teams[3].div_losses_szn) + "-" + str(AFC_EAST.teams[3].div_ties_szn)])

  aw = menu_div_standings.add.label("AFC West", font_size=div_label_size)

  table_afc_west = menu_div_standings.add.table(font_size=table_font_size)
  table_afc_west.default_cell_padding = padding
  table_afc_west.default_cell_align = pygame_menu.locals.ALIGN_CENTER
  aw_row1 = table_afc_west.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  aw_row2 = table_afc_west.add_row([AFC_WEST.teams[0].name, AFC_WEST.teams[0].wins_szn, AFC_WEST.teams[0].losses_szn, AFC_WEST.teams[0].ties_szn, AFC_WEST.teams[0].win_pct, AFC_WEST.teams[0].pts_for_szn, AFC_WEST.teams[0].pts_against_szn, AFC_WEST.teams[0].pts_for_szn - AFC_WEST.teams[0].pts_against_szn, str(AFC_WEST.teams[0].div_wins_szn) + "-" + str(AFC_WEST.teams[0].div_losses_szn) + "-" + str(AFC_WEST.teams[0].div_ties_szn)])

  aw_row3 = table_afc_west.add_row([AFC_WEST.teams[1].name, AFC_WEST.teams[1].wins_szn, AFC_WEST.teams[1].losses_szn, AFC_WEST.teams[1].ties_szn, AFC_WEST.teams[1].win_pct, AFC_WEST.teams[1].pts_for_szn, AFC_WEST.teams[1].pts_against_szn, AFC_WEST.teams[1].pts_for_szn - AFC_WEST.teams[1].pts_against_szn, str(AFC_WEST.teams[1].div_wins_szn) + "-" + str(AFC_WEST.teams[1].div_losses_szn) + "-" + str(AFC_WEST.teams[1].div_ties_szn)])

  aw_row4 = table_afc_west.add_row([AFC_WEST.teams[2].name, AFC_WEST.teams[2].wins_szn, AFC_WEST.teams[2].losses_szn, AFC_WEST.teams[2].ties_szn, AFC_WEST.teams[2].win_pct, AFC_WEST.teams[2].pts_for_szn, AFC_WEST.teams[2].pts_against_szn, AFC_WEST.teams[2].pts_for_szn - AFC_WEST.teams[2].pts_against_szn, str(AFC_WEST.teams[2].div_wins_szn) + "-" + str(AFC_WEST.teams[2].div_losses_szn) + "-" + str(AFC_WEST.teams[2].div_ties_szn)])

  aw_row5 = table_afc_west.add_row([AFC_WEST.teams[3].name, AFC_WEST.teams[3].wins_szn, AFC_WEST.teams[3].losses_szn, AFC_WEST.teams[3].ties_szn, AFC_WEST.teams[3].win_pct, AFC_WEST.teams[3].pts_for_szn, AFC_WEST.teams[3].pts_against_szn, AFC_WEST.teams[3].pts_for_szn - AFC_WEST.teams[3].pts_against_szn, str(AFC_WEST.teams[3].div_wins_szn) + "-" + str(AFC_WEST.teams[3].div_losses_szn) + "-" + str(AFC_WEST.teams[3].div_ties_szn)])

  an = menu_div_standings.add.label("AFC North", font_size=div_label_size)
  table_afc_north = menu_div_standings.add.table(font_size=table_font_size)

  table_afc_north.default_cell_padding = padding
  table_afc_north.default_cell_align = pygame_menu.locals.ALIGN_CENTER

  an_row1 = table_afc_north.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  an_row2 = table_afc_north.add_row([AFC_NORTH.teams[0].name, AFC_NORTH.teams[0].wins_szn, AFC_NORTH.teams[0].losses_szn, AFC_NORTH.teams[0].ties_szn, AFC_NORTH.teams[0].win_pct, AFC_NORTH.teams[0].pts_for_szn, AFC_NORTH.teams[0].pts_against_szn, AFC_NORTH.teams[0].pts_for_szn - AFC_NORTH.teams[0].pts_against_szn, str(AFC_NORTH.teams[0].div_wins_szn) + "-" + str(AFC_NORTH.teams[0].div_losses_szn) + "-" + str(AFC_NORTH.teams[0].div_ties_szn)])

  an_row3 = table_afc_north.add_row([AFC_NORTH.teams[1].name, AFC_NORTH.teams[1].wins_szn, AFC_NORTH.teams[1].losses_szn, AFC_NORTH.teams[1].ties_szn, AFC_NORTH.teams[1].win_pct, AFC_NORTH.teams[1].pts_for_szn, AFC_NORTH.teams[1].pts_against_szn, AFC_NORTH.teams[1].pts_for_szn - AFC_NORTH.teams[1].pts_against_szn, str(AFC_NORTH.teams[1].div_wins_szn) + "-" + str(AFC_NORTH.teams[1].div_losses_szn) + "-" + str(AFC_NORTH.teams[1].div_ties_szn)])

  an_row4 = table_afc_north.add_row([AFC_NORTH.teams[2].name, AFC_NORTH.teams[2].wins_szn, AFC_NORTH.teams[2].losses_szn, AFC_NORTH.teams[2].ties_szn, AFC_NORTH.teams[2].win_pct, AFC_NORTH.teams[2].pts_for_szn, AFC_NORTH.teams[2].pts_against_szn, AFC_NORTH.teams[2].pts_for_szn - AFC_NORTH.teams[2].pts_against_szn, str(AFC_NORTH.teams[2].div_wins_szn) + "-" + str(AFC_NORTH.teams[2].div_losses_szn) + "-" + str(AFC_NORTH.teams[2].div_ties_szn)])

  an_row5 = table_afc_north.add_row([AFC_NORTH.teams[3].name, AFC_NORTH.teams[3].wins_szn, AFC_NORTH.teams[3].losses_szn, AFC_NORTH.teams[3].ties_szn, AFC_NORTH.teams[3].win_pct, AFC_NORTH.teams[3].pts_for_szn, AFC_NORTH.teams[3].pts_against_szn, AFC_NORTH.teams[3].pts_for_szn - AFC_NORTH.teams[3].pts_against_szn, str(AFC_NORTH.teams[3].div_wins_szn) + "-" + str(AFC_NORTH.teams[3].div_losses_szn) + "-" + str(AFC_NORTH.teams[3].div_ties_szn)])

  aas = menu_div_standings.add.label("AFC South", font_size=div_label_size)
  table_afc_south = menu_div_standings.add.table(font_size=table_font_size)
  table_afc_south.default_cell_padding = padding
  table_afc_south.default_cell_align = pygame_menu.locals.ALIGN_CENTER

  as_row1 = table_afc_south.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  as_row2 = table_afc_south.add_row([AFC_SOUTH.teams[0].name, AFC_SOUTH.teams[0].wins_szn, AFC_SOUTH.teams[0].losses_szn, AFC_SOUTH.teams[0].ties_szn, AFC_SOUTH.teams[0].win_pct, AFC_SOUTH.teams[0].pts_for_szn, AFC_SOUTH.teams[0].pts_against_szn, AFC_SOUTH.teams[0].pts_for_szn - AFC_SOUTH.teams[0].pts_against_szn, str(AFC_SOUTH.teams[0].div_wins_szn) + "-" + str(AFC_SOUTH.teams[0].div_losses_szn) + "-" + str(AFC_SOUTH.teams[0].div_ties_szn)])

  as_row3 = table_afc_south.add_row([AFC_SOUTH.teams[1].name, AFC_SOUTH.teams[1].wins_szn, AFC_SOUTH.teams[1].losses_szn, AFC_SOUTH.teams[1].ties_szn, AFC_SOUTH.teams[1].win_pct, AFC_SOUTH.teams[1].pts_for_szn, AFC_SOUTH.teams[1].pts_against_szn, AFC_SOUTH.teams[1].pts_for_szn - AFC_SOUTH.teams[1].pts_against_szn, str(AFC_SOUTH.teams[1].div_wins_szn) + "-" + str(AFC_SOUTH.teams[1].div_losses_szn) + "-" + str(AFC_SOUTH.teams[1].div_ties_szn)])

  as_row4 = table_afc_south.add_row([AFC_SOUTH.teams[2].name, AFC_SOUTH.teams[2].wins_szn, AFC_SOUTH.teams[2].losses_szn, AFC_SOUTH.teams[2].ties_szn, AFC_SOUTH.teams[2].win_pct, AFC_SOUTH.teams[2].pts_for_szn, AFC_SOUTH.teams[2].pts_against_szn, AFC_SOUTH.teams[2].pts_for_szn - AFC_SOUTH.teams[2].pts_against_szn, str(AFC_SOUTH.teams[2].div_wins_szn) + "-" + str(AFC_SOUTH.teams[2].div_losses_szn) + "-" + str(AFC_SOUTH.teams[2].div_ties_szn)])

  as_row5 = table_afc_south.add_row([AFC_SOUTH.teams[3].name, AFC_SOUTH.teams[3].wins_szn, AFC_SOUTH.teams[3].losses_szn, AFC_SOUTH.teams[3].ties_szn, AFC_SOUTH.teams[3].win_pct, AFC_SOUTH.teams[3].pts_for_szn, AFC_SOUTH.teams[3].pts_against_szn, AFC_SOUTH.teams[3].pts_for_szn - AFC_SOUTH.teams[3].pts_against_szn, str(AFC_SOUTH.teams[3].div_wins_szn) + "-" + str(AFC_SOUTH.teams[3].div_losses_szn) + "-" + str(AFC_SOUTH.teams[3].div_ties_szn)])


  ne = menu_div_standings.add.label("NFC East", font_size=div_label_size)

  table_nfc_east = menu_div_standings.add.table(font_size=table_font_size)
  table_nfc_east.default_cell_padding = padding
  table_nfc_east.default_cell_align = pygame_menu.locals.ALIGN_CENTER

  ne_row1 = table_nfc_east.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  ne_row2 = table_nfc_east.add_row([NFC_EAST.teams[0].name, NFC_EAST.teams[0].wins_szn, NFC_EAST.teams[0].losses_szn, NFC_EAST.teams[0].ties_szn, NFC_EAST.teams[0].win_pct, NFC_EAST.teams[0].pts_for_szn, NFC_EAST.teams[0].pts_against_szn, NFC_EAST.teams[0].pts_for_szn - NFC_EAST.teams[0].pts_against_szn, str(NFC_EAST.teams[0].div_wins_szn) + "-" + str(NFC_EAST.teams[0].div_losses_szn) + "-" + str(NFC_EAST.teams[0].div_ties_szn)])

  ne_row3 = table_nfc_east.add_row([NFC_EAST.teams[1].name, NFC_EAST.teams[1].wins_szn, NFC_EAST.teams[1].losses_szn, NFC_EAST.teams[1].ties_szn, NFC_EAST.teams[1].win_pct, NFC_EAST.teams[1].pts_for_szn, NFC_EAST.teams[1].pts_against_szn, NFC_EAST.teams[1].pts_for_szn - NFC_EAST.teams[1].pts_against_szn, str(NFC_EAST.teams[1].div_wins_szn) + "-" + str(NFC_EAST.teams[1].div_losses_szn) + "-" + str(NFC_EAST.teams[1].div_ties_szn)])

  ne_row4 = table_nfc_east.add_row([NFC_EAST.teams[2].name, NFC_EAST.teams[2].wins_szn, NFC_EAST.teams[2].losses_szn, NFC_EAST.teams[2].ties_szn, NFC_EAST.teams[2].win_pct, NFC_EAST.teams[2].pts_for_szn, NFC_EAST.teams[2].pts_against_szn, NFC_EAST.teams[2].pts_for_szn - NFC_EAST.teams[2].pts_against_szn,  str(NFC_EAST.teams[2].div_wins_szn) + "-" + str(NFC_EAST.teams[2].div_losses_szn) + "-" + str(NFC_EAST.teams[2].div_ties_szn)])

  ne_row5 = table_nfc_east.add_row([NFC_EAST.teams[3].name, NFC_EAST.teams[3].wins_szn, NFC_EAST.teams[3].losses_szn, NFC_EAST.teams[3].ties_szn, NFC_EAST.teams[3].win_pct, NFC_EAST.teams[3].pts_for_szn, NFC_EAST.teams[3].pts_against_szn, NFC_EAST.teams[3].pts_for_szn - NFC_EAST.teams[3].pts_against_szn, str(NFC_EAST.teams[3].div_wins_szn) + "-" + str(NFC_EAST.teams[3].div_losses_szn) + "-" + str(NFC_EAST.teams[3].div_ties_szn)])

  nw = menu_div_standings.add.label("NFC West", font_size=div_label_size)

  table_nfc_west = menu_div_standings.add.table(font_size=table_font_size)
  table_nfc_west.default_cell_padding = padding
  table_nfc_west.default_cell_align = pygame_menu.locals.ALIGN_CENTER


  nw_row1 = table_nfc_west.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  nw_row2 = table_nfc_west.add_row([NFC_WEST.teams[0].name, NFC_WEST.teams[0].wins_szn, NFC_WEST.teams[0].losses_szn, NFC_WEST.teams[0].ties_szn, NFC_WEST.teams[0].win_pct, NFC_WEST.teams[0].pts_for_szn, NFC_WEST.teams[0].pts_against_szn, NFC_WEST.teams[0].pts_for_szn - NFC_WEST.teams[0].pts_against_szn, str(NFC_WEST.teams[0].div_wins_szn) + "-" + str(NFC_WEST.teams[0].div_losses_szn) + "-" + str(NFC_WEST.teams[0].div_ties_szn)])

  nw_row3 = table_nfc_west.add_row([NFC_WEST.teams[1].name, NFC_WEST.teams[1].wins_szn, NFC_WEST.teams[1].losses_szn, NFC_WEST.teams[1].ties_szn, NFC_WEST.teams[1].win_pct, NFC_WEST.teams[1].pts_for_szn, NFC_WEST.teams[1].pts_against_szn, NFC_WEST.teams[1].pts_for_szn - NFC_WEST.teams[1].pts_against_szn, str(NFC_WEST.teams[1].div_wins_szn) + "-" + str(NFC_WEST.teams[1].div_losses_szn) + "-" + str(NFC_WEST.teams[1].div_ties_szn)])

  nw_row4 = table_nfc_west.add_row([NFC_WEST.teams[2].name, NFC_WEST.teams[2].wins_szn, NFC_WEST.teams[2].losses_szn, NFC_WEST.teams[2].ties_szn, NFC_WEST.teams[2].win_pct, NFC_WEST.teams[2].pts_for_szn, NFC_WEST.teams[2].pts_against_szn, NFC_WEST.teams[2].pts_for_szn - NFC_WEST.teams[2].pts_against_szn,  str(NFC_WEST.teams[2].div_wins_szn) + "-" + str(NFC_WEST.teams[2].div_losses_szn) + "-" + str(NFC_WEST.teams[2].div_ties_szn)])

  nw_row5 = table_nfc_west.add_row([NFC_WEST.teams[3].name, NFC_WEST.teams[3].wins_szn, NFC_WEST.teams[3].losses_szn, NFC_WEST.teams[3].ties_szn, NFC_WEST.teams[3].win_pct, NFC_WEST.teams[3].pts_for_szn, NFC_WEST.teams[3].pts_against_szn, NFC_WEST.teams[3].pts_for_szn - NFC_WEST.teams[3].pts_against_szn, str(NFC_WEST.teams[3].div_wins_szn) + "-" + str(NFC_WEST.teams[3].div_losses_szn) + "-" + str(NFC_WEST.teams[3].div_ties_szn)])

  nn = menu_div_standings.add.label("NFC North", font_size=div_label_size)
  table_nfc_north = menu_div_standings.add.table(font_size=table_font_size)
  table_nfc_north.default_cell_padding = padding
  table_nfc_north.default_cell_align = pygame_menu.locals.ALIGN_CENTER


  nn_row1 = table_nfc_north.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  nn_row2 = table_nfc_north.add_row([NFC_NORTH.teams[0].name, NFC_NORTH.teams[0].wins_szn, NFC_NORTH.teams[0].losses_szn, NFC_NORTH.teams[0].ties_szn, NFC_NORTH.teams[0].win_pct, NFC_NORTH.teams[0].pts_for_szn, NFC_NORTH.teams[0].pts_against_szn, NFC_NORTH.teams[0].pts_for_szn - NFC_NORTH.teams[0].pts_against_szn, str(NFC_NORTH.teams[0].div_wins_szn) + "-" + str(NFC_NORTH.teams[0].div_losses_szn) + "-" + str(NFC_NORTH.teams[0].div_ties_szn)])

  nn_row3 = table_nfc_north.add_row([NFC_NORTH.teams[1].name, NFC_NORTH.teams[1].wins_szn, NFC_NORTH.teams[1].losses_szn, NFC_NORTH.teams[1].ties_szn, NFC_NORTH.teams[1].win_pct, NFC_NORTH.teams[1].pts_for_szn, NFC_NORTH.teams[1].pts_against_szn, NFC_NORTH.teams[1].pts_for_szn - NFC_NORTH.teams[1].pts_against_szn, str(NFC_NORTH.teams[1].div_wins_szn) + "-" + str(NFC_NORTH.teams[1].div_losses_szn) + "-" + str(NFC_NORTH.teams[1].div_ties_szn)])

  nn_row4 = table_nfc_north.add_row([NFC_NORTH.teams[2].name, NFC_NORTH.teams[2].wins_szn, NFC_NORTH.teams[2].losses_szn, NFC_NORTH.teams[2].ties_szn, NFC_NORTH.teams[2].win_pct, NFC_NORTH.teams[2].pts_for_szn, NFC_NORTH.teams[2].pts_against_szn, NFC_NORTH.teams[2].pts_for_szn - NFC_NORTH.teams[2].pts_against_szn, str(NFC_NORTH.teams[2].div_wins_szn) + "-" + str(NFC_NORTH.teams[2].div_losses_szn) + "-" + str(NFC_NORTH.teams[2].div_ties_szn)])

  nn_row5 = table_nfc_north.add_row([NFC_NORTH.teams[3].name, NFC_NORTH.teams[3].wins_szn, NFC_NORTH.teams[3].losses_szn, NFC_NORTH.teams[3].ties_szn, NFC_NORTH.teams[3].win_pct, NFC_NORTH.teams[3].pts_for_szn, NFC_NORTH.teams[3].pts_against_szn, NFC_NORTH.teams[3].pts_for_szn - NFC_NORTH.teams[3].pts_against_szn, str(NFC_NORTH.teams[3].div_wins_szn) + "-" + str(NFC_NORTH.teams[3].div_losses_szn) + "-" + str(NFC_NORTH.teams[3].div_ties_szn)])

  ns = menu_div_standings.add.label("NFC South", font_size=div_label_size)
  table_nfc_south = menu_div_standings.add.table(font_size=table_font_size)
  table_nfc_south.default_cell_padding = padding
  table_nfc_south.default_cell_align = pygame_menu.locals.ALIGN_CENTER


  ns_row1 = table_nfc_south.add_row(['Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Div Rec'])
  ns_row2 = table_nfc_south.add_row([NFC_SOUTH.teams[0].name, NFC_SOUTH.teams[0].wins_szn, NFC_SOUTH.teams[0].losses_szn, NFC_SOUTH.teams[0].ties_szn, NFC_SOUTH.teams[0].win_pct, NFC_SOUTH.teams[0].pts_for_szn, NFC_SOUTH.teams[0].pts_against_szn, NFC_SOUTH.teams[0].pts_for_szn - NFC_SOUTH.teams[0].pts_against_szn, str(NFC_SOUTH.teams[0].div_wins_szn) + "-" + str(NFC_SOUTH.teams[0].div_losses_szn) + "-" + str(NFC_SOUTH.teams[0].div_ties_szn)])

  ns_row3 = table_nfc_south.add_row([NFC_SOUTH.teams[1].name, NFC_SOUTH.teams[1].wins_szn, NFC_SOUTH.teams[1].losses_szn, NFC_SOUTH.teams[1].ties_szn, NFC_SOUTH.teams[1].win_pct, NFC_SOUTH.teams[1].pts_for_szn, NFC_SOUTH.teams[1].pts_against_szn, NFC_SOUTH.teams[1].pts_for_szn - NFC_SOUTH.teams[1].pts_against_szn, str(NFC_SOUTH.teams[1].div_wins_szn) + "-" + str(NFC_SOUTH.teams[1].div_losses_szn) + "-" + str(NFC_SOUTH.teams[1].div_ties_szn)])

  ns_row4 = table_nfc_south.add_row([NFC_SOUTH.teams[2].name, NFC_SOUTH.teams[2].wins_szn, NFC_SOUTH.teams[2].losses_szn, NFC_SOUTH.teams[2].ties_szn, NFC_SOUTH.teams[2].win_pct, NFC_SOUTH.teams[2].pts_for_szn, NFC_SOUTH.teams[2].pts_against_szn, NFC_SOUTH.teams[2].pts_for_szn - NFC_SOUTH.teams[2].pts_against_szn, str(NFC_SOUTH.teams[2].div_wins_szn) + "-" + str(NFC_SOUTH.teams[2].div_losses_szn) + "-" + str(NFC_SOUTH.teams[2].div_ties_szn)])

  ns_row5 = table_nfc_south.add_row([NFC_SOUTH.teams[3].name, NFC_SOUTH.teams[3].wins_szn, NFC_SOUTH.teams[3].losses_szn, NFC_SOUTH.teams[3].ties_szn, NFC_SOUTH.teams[3].win_pct, NFC_SOUTH.teams[3].pts_for_szn, NFC_SOUTH.teams[3].pts_against_szn, NFC_SOUTH.teams[3].pts_for_szn - NFC_SOUTH.teams[3].pts_against_szn, str(NFC_SOUTH.teams[3].div_wins_szn) + "-" + str(NFC_SOUTH.teams[3].div_losses_szn) + "-" + str(NFC_SOUTH.teams[3].div_ties_szn)])

def update_div():
  AFC_SOUTH.standings()
  AFC_NORTH.standings()
  AFC_EAST.standings()
  AFC_WEST.standings()
  NFC_WEST.standings()
  NFC_NORTH.standings()
  NFC_SOUTH.standings()
  NFC_EAST.standings()

def update_conf():
  #updates conf standings in the classes
  AFC.c_standings()
  NFC.c_standings()
  
def nfc_conf_standings():
  padding = 5
  table_nfc = menu_nfc_standings.add.table(font_size=table_font_size)
  table_nfc.default_cell_padding = padding
  table_nfc.default_cell_align = pygame_menu.locals.ALIGN_CENTER
  NFC.c_standings()
  ### table for all nfc teams, using a loop be be concise ###
  
  table_nfc.add_row(['Rank', 'Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Conf Rec'])
  for i in range(len(NFC.rankings)):
    h = table_nfc.add_row([i+1, NFC.rankings[i].name, NFC.rankings[i].wins_szn, NFC.rankings[i].losses_szn, NFC.rankings[i].ties_szn, NFC.rankings[i].win_pct, NFC.rankings[i].pts_for_szn, NFC.rankings[i].pts_against_szn, NFC.rankings[i].pts_for_szn - NFC.rankings[i].pts_against_szn,  str(NFC.rankings[i].conf_wins_szn) + " - " + str(NFC.rankings[i].conf_losses_szn) + " - " + str(NFC.rankings[i].conf_ties_szn)])
      
def afc_conf_standings():
  # similar to nfc version
  padding = 5 
  table_afc = menu_afc_standings.add.table(font_size=table_font_size)
  table_afc.default_cell_padding = padding
  table_afc.default_cell_align = pygame_menu.locals.ALIGN_CENTER
  AFC.c_standings()
  ### for loop ###

  table_afc.add_row(["Rank", 'Team', 'W', 'L', 'T', 'Pct', 'Pts For', 'Pts Against', '+/-', 'Conf Rec'])
  for i in range(len(AFC.rankings)):
    h = table_afc.add_row([i+1, AFC.rankings[i].name, AFC.rankings[i].wins_szn, AFC.rankings[i].losses_szn, AFC.rankings[i].ties_szn, AFC.rankings[i].win_pct, AFC.rankings[i].pts_for_szn, AFC.rankings[i].pts_against_szn, AFC.rankings[i].pts_for_szn - AFC.rankings[i].pts_against_szn,  str(AFC.rankings[i].conf_wins_szn) + " - " + str(AFC.rankings[i].conf_losses_szn) + " - " + str(AFC.rankings[i].conf_ties_szn)])

### going to menus ###
def go_div_standings():
  menu_div_standings.clear(False)
  update_div()
  weekly_standings()
  menu_standings._open(menu_div_standings)

def go_to_afc_standings():
  menu_afc_standings.clear(False)
  update_conf()
  afc_conf_standings()
  menu_choose_conf._open(menu_afc_standings)

def go_to_nfc_standings():
  menu_nfc_standings.clear(False)
  update_conf()
  nfc_conf_standings()
  menu_choose_conf._open(menu_nfc_standings)

## adding the buttons###
menu_standings.add.button("Division Standings", go_div_standings)
menu_standings.add.button("Conference Standings", menu_conf, menu_standings)

menu_choose_conf.add.button("NFC", go_to_nfc_standings)
menu_choose_conf.add.button("AFC", go_to_afc_standings)
#### sets up the Falcons as the user team
user_team = nfl.nfc_south[3]
your_player_buttons = []
## Player face is unused
face =  pygame.image.load("playerfaces/football_player.svg")
generate_sch(year, nfl)
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10,15))