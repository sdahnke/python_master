import numpy as np
import pandas
from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression

stat_file = pandas.read_csv('C:\\Users\\sdahnke\\Dropbox\\Privat\\predictive_modelling\\nfl_data\\weather_20131231.csv')

# replace % in humidity
stat_file["humidity"] = stat_file["humidity"].str.replace('%', '')

# replace 'NaN' values
stat_file["temperature"] = stat_file["temperature"].fillna(stat_file["temperature"].median())
stat_file["wind_chill"] = stat_file["wind_chill"].fillna(stat_file["wind_chill"].median())
stat_file["humidity"] = stat_file["humidity"].fillna(stat_file["humidity"].median())
stat_file["wind_mph"] = stat_file["wind_mph"].fillna(stat_file["wind_mph"].median())

# add column home_win
stat_file.loc[stat_file["home_score"] > stat_file["away_score"], "home_win"] = 1
stat_file.loc[stat_file["home_score"] <= stat_file["away_score"], "home_win"] = 0


# replace team names with dummy_ids
string_data = ["home_team", "away_team"]
stat_frame = pandas.get_dummies(stat_file, columns=string_data)
header_frame = pandas.get_dummies(stat_file, columns=string_data)

# delete columns
header_frame.drop(stat_frame.columns[[0, 1, 2, 7, 8, 9]], axis=1, inplace=True)

# columns to predict the target
predictors = list(header_frame.columns.values)

# init algorithm class
alg = LinearRegression()

# generate cross validation folds for the stat_file dataset.  It return the row indices corresponding to train and test.
# set random_state to ensure we get the same splits every time we run this.
kf = KFold(stat_file.shape[0], n_folds=1000, random_state=5)

predictions = []
for train, test in kf:
    # predictors we're using the train the algorithm.  Note how we only take the rows in the train folds.
    train_predictors = (stat_frame[predictors].iloc[train, :])
    # target we're using to train the algorithm
    train_target = stat_frame["home_win"].iloc[train]
    # training the algorithm using the predictors and target
    alg.fit(train_predictors, train_target)
    # now make predictions on the test fold
    test_predictions = alg.predict(stat_frame[predictors].iloc[test, :])
    predictions.append(test_predictions)

# predictions are in three separate numpy arrays and concatenate them into one
# concatenate them on axis 0, as they only have one axis
predictions = np.concatenate(predictions, axis=0)

# map predictions to outcomes (only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <= .5] = 0

# calc accuracy
accuracy = sum(predictions[predictions == stat_frame["home_win"]]) / len(predictions)

print("Die Genauigkeit der Linearen Regression entspricht : " + str(round(accuracy * 100, 3)) + " %")