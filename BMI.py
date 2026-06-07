
# BMI CALCULATOR PROJECT

try:

    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (meter): "))

    bmi = weight / (height ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")

    elif bmi < 25:
        print("Normal Weight")

    elif bmi < 30:
        print("Overweight")

    else:
        print("Obese")

except ValueError:
    print("Please Enter Valid Numbers")