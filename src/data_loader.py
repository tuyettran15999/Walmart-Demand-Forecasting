from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw"

def load_data():
    train = pd.read_csv(DATA_PATH / "train.csv")
    features = pd.read_csv(DATA_PATH / "features.csv")
    stores = pd.read_csv(DATA_PATH / "stores.csv")

    return train, features, stores
