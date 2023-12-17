def calculate_bmi(weight, height):
    # Weight in kilograms, height in meters
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your Body Mass Index (BMI) is: {bmi}")