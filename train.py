import pandas as pd
from utils import normalize
import json

def calculate_tmp_theta1(mileages, prices, theta0, theta1, coef):
    sum_of_err = 0.0
    for i in range(len(mileages)):
        sum_of_err += (theta0 + (theta1 * mileages[i]) - prices[i])
    return sum_of_err * coef

def calculate_tmp_theta2(mileages, prices, theta0, theta1, coef):
    sum_of_err = 0.0
    for i in range(len(mileages)):
        sum_of_err += ((theta0 + (theta1 * mileages[i]) - prices[i]) * mileages[i])
    return sum_of_err * coef

def denormalize_thetas(theta0, theta1, max_mileage, max_price):
    theta0 = theta0 * max_price
    theta1 = theta1 * (max_price / max_mileage)
    return theta0, theta1

def train(mileages, prices, learning_rate, number_of_iterations):
    mileages, max_mileage = normalize(mileages)
    prices, max_price = normalize(prices)
    coef = learning_rate / float(len(mileages))
    theta0 = 0.0
    theta1 = 0.0
    for i in range(number_of_iterations):
        tmp0 = calculate_tmp_theta1(mileages, prices, theta0, theta1, coef)
        tmp1 = calculate_tmp_theta2(mileages, prices, theta0, theta1, coef)
        theta0 -= tmp0
        theta1 -= tmp1
    theta0, theta1 = denormalize_thetas(theta0, theta1, max_mileage, max_price)
    return theta0, theta1

if __name__ == "__main__":
    df = pd.read_csv("./data/data.csv")
    mileages = df['km'].to_list()
    prices = df['price'].to_list()
    theta0, theta1 = train(mileages, prices, 0.01, 10000)
    values = {
        "theta0": theta0,
        "theta1": theta1
    }
    with open("values.json", "w") as outfile:
        json.dump(values, outfile)