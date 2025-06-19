from sklearn.datasets import load_iris
import pandas as pd

def create_data():
    data = load_iris()
    x, y = data.data, data.target
    pd.DataFrame(x).to_csv('/mnt/d/MLOPS/dags/data.csv', index=False)
    pd.DataFrame(y).to_csv('/mnt/d/MLOPS/dags/target.csv', index=False)