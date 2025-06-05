from train import train
from utils import mean_squared_error
import pandas as pd

def tune(mileages, prices):
    results = []
    learning_rate = [0.5, 0.40, 0.35, 0.30, 0.15, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    for it in range(500, 10000, 500):
        for lr in learning_rate:
            theta0, theta1 = train(mileages, prices, lr, it)
            mse = mean_squared_error(mileages, prices, theta0, theta1)
            results.append({
                "learning_rate": lr,
                "iterations": it,
                "mse": mse
            })
            print(f"learning rate : {lr} and iterations {it}\n---> MSE : {mse}\n--------------------\n")
    best_result = min(results, key=lambda x: x["mse"])
    print(f"Best Option -> lr : {best_result['learning_rate']} with {best_result['iterations']} iterations\nMSE = {best_result['mse']}\n")

if __name__ == "__main__":
    df = pd.read_csv("./data/data.csv")
    mileages = df['km'].to_list()
    prices = df['price'].to_list()
    tune(mileages, prices)