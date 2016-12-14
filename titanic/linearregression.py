import pandas
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
import numpy as np
from sklearn.linear_model.logistic import LogisticRegression
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
import re
import operator
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import GradientBoostingClassifier


titanic = pandas.read_csv('C:\\Users\\sdahnke\\Dropbox\\Kaggle\\TitanicMachineLearningFromDisaster\\train.csv')

# print(titanic.head(5))
# print(titanic.describe())

# print(titanic["Age"])

titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

# convert Sex to numeric value
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

# print(titanic["Embarked"].unique())
# convert Embarked to num value and fill NaN values with "S" = 0
titanic["Embarked"] = titanic["Embarked"].fillna("S")

titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

# print(titanic.head(5))

# columns to predict the target
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# init algorithm class
alg = LinearRegression()

# generate cross validation folds for the titanic dataset.  It return the row indices corresponding to train and test.
# set random_state to ensure we get the same splits every time we run this.
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    # predictors we're using the train the algorithm.  Note how we only take the rows in the train folds.
    train_predictors = (titanic[predictors].iloc[train, :])
    # target we're using to train the algorithm
    train_target = titanic["Survived"].iloc[train]
    # training the algorithm using the predictors and target
    alg.fit(train_predictors, train_target)
    # now make predictions on the test fold
    test_predictions = alg.predict(titanic[predictors].iloc[test, :])
    predictions.append(test_predictions)

# predictions are in three separate numpy arrays and concatenate them into one
# concatenate them on axis 0, as they only have one axis
predictions = np.concatenate(predictions, axis=0)

# map predictions to outcomes (only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0

# calc accuracy
accuracy = sum(predictions[predictions == titanic["Survived"]]) / len(predictions)

# init algorithm
alg = LogisticRegression(random_state=1)
# compute the accuracy score for all the cross validation folds.  (much simpler than what we did before!)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
# take the mean of the scores (because we have one for each fold)
print(scores.mean())