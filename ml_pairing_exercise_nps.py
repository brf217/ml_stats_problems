import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('nps_data.csv')

#check nulls and summary
df.isnull().sum()
summary = df.describe()

#almost all nan
df.drop('previous_NPS', axis = 1, inplace = True)

#new feature on license change
df['license_delta'] = df['current_licenses'] - df['previous_licenses']

#drop constant value - see summary
df.drop('minutes_kanban1', axis = 1, inplace = True)

#train test split the df - declare x and y
from sklearn.model_selection import train_test_split

X = df.drop('NPS', axis = 1)
y = df['NPS']

#train test split using default test_size
X_train, X_test, y_train, y_test = train_test_split(X,y)

#scale data given different scales (minutes, licenses, etc)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

#scale X_train
X_train_scl = scaler.fit_transform(X_train)
X_test_scl = scaler.fit_transform(X_test)

#import a model and fit on training data
from sklearn.ensemble import RandomForestClassifier as rfc
rfc = rfc(n_estimators = 100)
rfc.fit(X_train_scl, y_train)
preds = rfc.predict(X_test_scl)

#test accuracy and classification
from sklearn.metrics import classification_report as cr
print(cr(preds, y_test))

#check importances of predictors and plot for easy viewing
features = rfc.feature_importances_
feature_df = pd.DataFrame(X_train.columns, features).reset_index()
feature_df.columns = ['importance', 'feature']
feature_df.sort_values('importance', ascending = 0, inplace = True)
feature_df.plot('feature','importance', kind = 'bar' )

#automated feature selection technique that retains interpretability
from sklearn.feature_selection import RFE
rfe = RFE(rfc, 5)
fit = rfe.fit(X_train_scl, y_train)
fit.ranking_
rfe_selections = pd.DataFrame(X_train.columns, fit.ranking_,).reset_index()
rfe_selections.columns = ['ranking', 'feature']
rfe_selections.sort_values('ranking', inplace = True)

#see accuracy on dimension reduction - RFE with one feature almost as predictive as whole model
rfe_preds = rfe.predict(X_test_scl)
print(cr(rfe_preds, y_test))













