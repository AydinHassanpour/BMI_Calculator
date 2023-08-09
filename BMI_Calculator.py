class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight  # Weight in kilograms
        self.height = height  # Height in meters

    def calculate_bmi(self):
        """
        Calculate BMI based on weight and height
        :return: Calculated BMI
        """
        bmi = self.weight / (self.height ** 2)
        return bmi

# Request user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Create an instance of the BMICalculator class using user inputs
calculator = BMICalculator(weight, height)

# Calculate BMI using the calculate_bmi method
bmi = calculator.calculate_bmi()

# Display the calculated BMI to the user
print("Your BMI is:", bmi)
