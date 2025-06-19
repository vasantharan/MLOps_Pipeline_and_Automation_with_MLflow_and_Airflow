import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def train_model():
    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    model = RandomForestClassifier(n_estimators=100)
    x = pd.read_csv('/mnt/d/MLOPS/dags/data.csv')
    y = pd.read_csv('/mnt/d/MLOPS/dags/target.csv').values.ravel()
    model.fit(x, y)
    with mlflow.start_run():
        mlflow.log_param('n_estimators', 100)
