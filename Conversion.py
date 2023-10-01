print ("Entering Temperature in:")
print ("1: Celsius")
print ("2: Fahrenheit")

choice = int(input())

print ("Enter temperature")
temperature = int(input())

def fahrenheit_to_celsius(temperature):
  return round(((temperature - 32) / 1.8), 1)

def celsius_to_fahrenheit(temperature):
  return round(((temperature * 1.8) + 32), 1)

if choice == 1:
  result = celsius_to_fahrenheit(temperature)
  print ("The resulting temperature is", result, "degree Fahrenheit")
elif choice == 2:
  result = fahrenheit_to_celsius(temperature)
  print ("The resulting temperature is", result, "degree Celsius")
