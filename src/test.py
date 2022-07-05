import pandas as pd
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

filename = "../models/saved_model"

df = pd.read_csv("../data/test_data.csv"")


RF_model = pickle.load(open(filename, 'rb'))
y_pred = RF_model.predict(df[['sepal_length', 'sepal_width', 'petal_length', 'peta_width']])
accuracy_score(df['label'], y_pred)


