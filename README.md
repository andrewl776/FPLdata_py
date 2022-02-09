# Introduction

This data contains a large variety of information on players and their
  current attributes on Fantasy Premier League
  <https://fantasy.premierleague.com/>. In particular, it contains a
  `next_gw_points` (next gameweek points) value for each player
  given their attributes in the current week. Rows represent player-gameweeks,
  i.e. for each player there is a row for each gameweek. This
  makes the data suitable for modelling a player's next gameweek points, given
  attributes such as form, total points, and cost at the current gameweek.
  This data can therefore be used to create Fantasy Premier League bots that
  may use a machine learning algorithm and a linear programming solver
  (for example) to return the best possible transfers and team to pick for
  each gameweek, thereby fully automating the decision making process in
  Fantasy Premier League. This function simply supplies the required data
  for such a task.
