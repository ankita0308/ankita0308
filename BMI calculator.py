def calculate_bmi(weight, height):
    # Calculate BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight (in kilograms): "))
    height = float(input("Enter your height (in meters): "))

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"Your BMI is {bmi:.2f}")
    print(f"Interpretation: {interpretation}")

if __name__ == "__main__":
    main()
