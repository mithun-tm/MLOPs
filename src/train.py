import pandas as pd
import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

filename = "models/saved_model"

df = pd.read_csv("data/train_data.csv")


RF_model = RandomForestClassifier(n_estimators=5, max_depth = 3)
RF_model.fit(df[['sepal_length', 'sepal_width', 'petal_length', 'peta_width']], df['label'])
y_pred = RF_model.predict(df[['sepal_length', 'sepal_width', 'petal_length', 'peta_width']])
acc = accuracy_score(df['label'], y_pred)

print("Accuracy : ", acc)
pickle.dump(RF_model, open(filename, 'wb'))

