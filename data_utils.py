# 📁 data_utils.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_prepare_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"Şikayet": "text", "Müdürlük": "label"})
    label_encoder = LabelEncoder()
    df["labels"] = label_encoder.fit_transform(df["label"])
    return df, label_encoder