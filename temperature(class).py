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

# Example usage
temperature = Temperature(70)
temperature.convert("fahrenheit")  # Convert Celsius to Fahrenheit
temperature.convert("celsius")  # Convert Fahrenheit back to Celsius

# Additional usage with different initial scale
temperature = Temperature(60, "fahrenheit")
temperature.convert("celsius")