import xgboost as xgb
from xgboost import XGBClassifier

X, y = telco_churn.data, telco_churn.target

xgb = XGBoostClassifier()
xgb.fit(X,y)