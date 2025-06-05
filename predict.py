import json

def predict(to_predict, theta0, theta1):
    try:
        km = float(to_predict)
        if km < 0:
            raise Exception("Input cannot be negative.")
        prediction = theta0 + (theta1 * km)
        if prediction <= 0:
            prediction = 0
        return prediction
    
    except ValueError:
        print("L'input n'est pas un nombre.")

if __name__ == "__main__":
    with open("./values.json", "r") as file:
            values = json.load(file)
    theta0 = values['theta0']
    theta1 = values['theta1']
    to_predict = input("Mileage : ")
    prediction = predict(to_predict, theta0, theta1)
    print(f"Prediction : {prediction}")