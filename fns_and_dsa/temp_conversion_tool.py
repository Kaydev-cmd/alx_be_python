FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input("Enter the temperature to convert: "))
temperature_unit = input("Is the temperature in Celsius or Fahrenheit? (C/F) ").strip().upper()

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  
if temperature_unit == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp:.2f}°F")
    
elif temperature_unit == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp:.2f}°C")
    
else: 
  print("Invalid temperature. Please enter a numeric value.")
  
