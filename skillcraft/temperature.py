# Function to convert from Celsius to Fahrenheit and Kelvin
def celsius_to_fahrenheit_kelvin(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Function to convert from Fahrenheit to Celsius and Kelvin
def fahrenheit_to_celsius_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert from Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Main function to handle user input and conversions
def main():
    print("Temperature Converter")
    print("Choose an option to convert:")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit, kelvin = celsius_to_fahrenheit_kelvin(celsius)
        print(f"{celsius} Celsius = {fahrenheit:.3f} Fahrenheit, {kelvin:.3f} Kelvin")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius, kelvin = fahrenheit_to_celsius_kelvin(fahrenheit)
        print(f"{fahrenheit} Fahrenheit = {celsius:.3f} Celsius, {kelvin:.3f} Kelvin")

    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius, fahrenheit = kelvin_to_celsius_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin = {celsius:.3f} Celsius, {fahrenheit:.3f} Fahrenheit")

    else:
        print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
