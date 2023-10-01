print ("Entering Temperature in:")
print ("1: Celsius")
print ("2: Fahrenheit")

choice = int(input())

print ("Enter temperature")
temperature = int(input())

def celsius_to_fahrenheit(temperature):
  return ((temperature - 32) / 1.8)

def fahrenheit_to_celsius(temperature):
  return ((temperature * 1.8) + 32)

if choice == 1:
  celsius_to_fahrenheit(temperature)
elif choice == 2:
  fahrenheit_to_celsius(temperature)
