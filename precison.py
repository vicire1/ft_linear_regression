from predict import predict
import json
import pandas as pd
import math

def mean_squared_error(x, y, theta0, theta1):
    square_diff = 0
    data_len = len(x)
    for i in range(data_len):
        y_pred = predict(x[i], theta0, theta1)
        square_diff += ((y_pred - y[i]) ** 2)
    return square_diff / data_len

if __name__ == "__main__":
    with open("./values.json", "r") as file:
            values = json.load(file)
    theta0 = values['theta0']
    theta1 = values['theta1']

    df = pd.read_csv("./data/data.csv")
    mileages = df['km'].to_list()
    prices = df['price'].to_list()

    mse = mean_squared_error(mileages, prices, theta0, theta1)
    rmse = math.sqrt(mse)
    print(f"The root mean squared error if this model is {rmse} euros.")