#  code to calculate temperature units from user input
class Temperature:
    def __init__(self, value, scale="celsius"):
        self.value = value
        self.scale = scale.lower()  # Ensure consistent case for scale

    def convert(self, target_scale):
        if self.scale == target_scale:
            print(f"The temperature is already in {target_scale.capitalize()} ({self.value:.2f}°{target_scale.upper()})")
            return

        conversion_factor = 1.8 if self.scale == "celsius" else 1 / 1.8
        converted_value = (self.value - 32) * conversion_factor if self.scale == "fahrenheit" else self.value * conversion_factor + 32
        print(f"The converted temperature is {converted_value:.2f}°{target_scale.upper()}")

# Function to get user input for temperature value and scale
def get_user_input():
    while True:
        value = input("Enter the temperature value: ")
        try:
            value = float(value)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    scale = input("Enter the scale (celsius or fahrenheit): ").lower()
    while scale not in ['celsius', 'fahrenheit']:
        print("Invalid input. Please enter either 'celsius' or 'fahrenheit'.")
        scale = input("Enter the scale (celsius or fahrenheit): ").lower()

    return value, scale

# Example usage with user input
value, scale = get_user_input()
temperature = Temperature(value, scale)
target_scale = input("Enter the target scale for conversion (celsius or fahrenheit): ").lower()
temperature.convert(target_scale)
