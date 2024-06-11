import xgboost as xgb
from sklearn.datasets import load_iris
import pickle

class IrisModel:
    def __init__(self):
        self.model = None

    def load_model(self, path: str):
        with open(path, 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, data):
        if not self.model:
            raise ValueError("Model is not loaded")
        dmatrix = xgb.DMatrix(data)
        return self.model.predict(dmatrix)

def train_and_save_model(path: str):
    iris = load_iris()
    X, y = iris.data, iris.target
    dmatrix = xgb.DMatrix(X, label=y)
    params = {
        'objective': 'multi:softmax',
        'num_class': 3
    }
    model = xgb.train(params, dmatrix)
    with open(path, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    train_and_save_model('xgb_iris_model.pkl')

