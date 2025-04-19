# Wind Chill Calculator
# This program calculates the wind chill for wind speeds from 5 to 60 mph
# using user input in Celsius or Fahrenheit.
# Coding starts here...

# --- Functions ---

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def calculate_wind_chill(temperature_f, wind_speed_mph):
    """Calculate wind chill based on temperature in Fahrenheit and wind speed in mph."""
    wind_chill = 35.74 + (0.6215 * temperature_f) \
                 - 35.75 * (wind_speed_mph ** 0.16) \
                 + 0.4275 * temperature_f * (wind_speed_mph ** 0.16)
    return wind_chill

# --- Main Program ---

# Get temperature from user
try:
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if unit == "C":
        temperature_f = celsius_to_fahrenheit(temperature)
    elif unit == "F":
        temperature_f = temperature
    else:
        print("Invalid unit. Please enter 'F' or 'C'.")
        exit()

    # Loop through wind speeds and calculate wind chill
    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temperature_f, wind_speed)
        print(f"At temperature {temperature_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

except ValueError:
    print("Invalid input. Please enter a numeric value for the temperature.")
