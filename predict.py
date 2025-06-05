import json

def predict(to_predict, theta0, theta1):
    try:
        km = float(to_predict)
        if km < 0:
            raise Exception("Input cannot be negative.")
        prediction = theta0 + (theta1 * km)
        return max(0, prediction)
    except ValueError as e:
        print(f"Erreur : {str(e)}")
        return None

if __name__ == "__main__":
    with open("./values.json", "r") as file:
            values = json.load(file)
    theta0 = values['theta0']
    theta1 = values['theta1']
    to_predict = input("Mileage : ")
    prediction = predict(to_predict, theta0, theta1)
    print(f"Prediction : {prediction}")