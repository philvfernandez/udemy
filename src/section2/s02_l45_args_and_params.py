

def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg({
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
})