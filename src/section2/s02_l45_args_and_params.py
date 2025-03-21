def calculate_mpg():
    car = {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460
    }
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg()