import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import xgboost as xgb
from sklearn.linear_model import LogisticRegression

# Split and train the data
from sklearn.model_selection import train_test_split

# I will construct a pipeline containing my chosen models
from sklearn.pipeline import Pipeline

# I need to score predicted versus actual values
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer, confusion_matrix, ConfusionMatrixDisplay

# I need to cross-validate and evaluate results
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
