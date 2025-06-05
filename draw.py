import matplotlib.pyplot as plt
import pandas as pd
import json

def draw_graph(mileages, prices, theta0, theta1):
    y_pred = [theta0 + theta1 * x for x in mileages]

    plt.scatter(mileages, prices, color="blue", label="data")
    plt.plot(mileages, y_pred, color="red", label="linear regression")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("./data/data.csv")
    mileages = df['km'].to_list()
    prices = df['price'].to_list()
    with open("./values.json", "r") as file:
        values = json.load(file)
    theta0 = values['theta0']
    theta1 = values['theta1']
    draw_graph(mileages, prices, theta0, theta1)