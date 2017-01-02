import pandas

stat_file = pandas.read_csv('C:\\Users\\sdahnke\\Dropbox\\Privat\\predictive_modelling\\nfl_data\\weather_20131231.csv')

# Show start stat_file
# print(stat_file.head(2))
# print(stat_file.describe())

# replace 'NaN' values
stat_file["wind_chill"] = stat_file["wind_chill"].fillna(stat_file["wind_chill"].median())

# add column home_win
stat_file.loc[stat_file["home_score"] > stat_file["away_score"], "home_win"] = 1
stat_file.loc[stat_file["home_score"] <= stat_file["away_score"], "home_win"] = 0

print(stat_file.head(10))

# columns to predict the target
predictors = ["home_team", "away_team", "temperature", "wind_chill", "humidity", "wind_mph", "date"]
