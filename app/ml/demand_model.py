import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error


class DemandModel:
    def __init__(self):
        self.model = None

    def train(self, df: pd.DataFrame):
        X = df[["genre", "year", "price", "rating"]]
        Y = np.log1p(df["review_count"])

        preprocessor = ColumnTransformer(
            transformers=[
                ("genre", OneHotEncoder(handle_unknown="ignore"), ["genre"]),
                ("num", "passthrough", ["year", "price", "rating"]),
            ]
        )

        self.model = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("regressor", LinearRegression()),
            ]
        )

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)

        return [round(mse, 2), round(mae, 2)]

    def predict(self, book_features: dict):
        df = pd.DataFrame([book_features])
        return int(np.expm1(self.model.predict(df)[0]))