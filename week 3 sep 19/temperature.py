#Activity 8: temperature
temperature = float(input("Enter the temperature in degrees Celsius: "))

if temperature <= 0:
    state = "solid"
elif temperature <= 100:
    state = "liquid"
else:
    state = "gas"

print(f"At {temperature} degrees Celsius, the substance is in a {state} state.")
