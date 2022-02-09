from pandas import read_csv

def FPLdata():
    fpl_data = read_csv("https://raw.githubusercontent.com/andrewl776/fplmodels/master/data/players_by_gameweek_csv.csv")
    fpl_data = fpl_data.dropna(axis = 0, subset=["next_gw_points"])
    return(fpl_data)

