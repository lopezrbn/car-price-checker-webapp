import os
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression


def train_model(manuf, mod):

    # Input data and creation of dataframe

    # Path of the csv file with the data for the supplied car model
    manuf = manuf.replace(" ", "-")
    mod = mod.replace(" ", "-")
    abs_path = os.path.dirname(__file__)
    rel_path = "data/csv"
    file_path = manuf + "_" + mod + ".csv"
    full_path = os.path.join(abs_path, rel_path, file_path)
    print(f"Reading {file_path}.")

    # Dataframe creation
    df = pd.read_csv(full_path, index_col=0)
    df = df.drop_duplicates()
    target = "price"
    num_cols = ["year", "month", "km", "power_hp", "no_doors"]
    non_relevant = ["manufacturer", "model", "version", "color", "seller", "link"]
    cat_cols = [col for col in df.columns if col not in num_cols + non_relevant + [target]]

    # Columns adaptation and creation of new features
    df["month"].fillna(0, inplace=True)
    df["km"] = df["km"].str.replace(".", "").str.replace(" km", "")
    df.loc[df["km"]=="NUEVO", "km"] = 0
    df["power_hp"] = df["power_hp"].str.replace(" CV", "")
    df["no_doors"] = df["no_doors"].str.replace(" puertas", "")
    df["age"] = 2023 - df["year"]
    num_cols.append("age")
    df = df.astype({"month":"int", "year":"int", "km": int, "power_hp": int, "no_doors": int, "price": int})

    # Filtering of outliers
    prev_size = df.shape[0]
    for col in num_cols:
        mean_ = df[col].mean()
        std_ = df[col].std()
        lower_limit = mean_ - 3 * std_
        upper_limit = mean_ + 3 * std_
        outliers_indices = df[col][(df[col] < lower_limit) | (df[col] > upper_limit)].index.tolist()
        df.drop(outliers_indices, inplace=True)
    post_size = df.shape[0]
    print("Outliers filtered. {} rows deleted ({:.2f}%).".format(prev_size-post_size, (1-post_size/prev_size)*100))

    # Creation of X and y
    X = df[num_cols + cat_cols].copy()
    y = df[target].copy()

    # Pipelines

    pipe_num = Pipeline(
        steps=[
            ("standardization", MinMaxScaler())
        ]
    )
    pipe_cat = Pipeline(
        steps=[
            ("oh_encoder", OneHotEncoder(handle_unknown='ignore', sparse=False, drop="first", dtype=int))
        ]
    )
    col_transformer = ColumnTransformer(
        transformers=[
            ("num", pipe_num, num_cols),
            ("cat", pipe_cat, cat_cols)
        ],
        remainder="passthrough"
    )

    # Model
    model = LinearRegression()

    # Global pipe
    pipe_global = Pipeline(
        steps=[
            ("col_transformer", col_transformer),
            ("model", model)
        ]
    )

    # Fitting of the model
    pipe_global.fit(X, y)
    print(f"R^2: {pipe_global.score(X,y)}")

    return pipe_global


def make_prediction(manuf, model, X_pred):
    pipe = train_model(manuf, model)
    return pipe.predict(X_pred)[0]