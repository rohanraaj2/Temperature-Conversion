repeat = True

def temperature_input():
  print ("Entering Temperature in:")
  print ("1: Celsius")
  print ("2: Fahrenheit")

  choice = input()

  if choice != '1' and choice != '2':
    print("Invalid Input. Please try again.")
    temperature_type()

  else:
    return int(choice)
  
def temperature_number():

  print ("Enter temperature")
  temperature = input()

  if temperature.isdigit() == False:
    print('Temperature must be a number')
    temperature_number()

  else:
    return int(temperature)

while repeat == True:

  temperature_type = temperature_input()
  temperature = temperature_number()
  def fahrenheit_to_celsius(temperature):
    return round(((temperature - 32) / 1.8), 1)

  def celsius_to_fahrenheit(temperature):
    return round(((temperature * 1.8) + 32), 1)

  if temperature_type == 1:
    result = celsius_to_fahrenheit(temperature)
    print ("The resulting temperature is", result, "degree Fahrenheit")
    
  elif temperature_type == 2:
    result = fahrenheit_to_celsius(temperature)
    print ("The resulting temperature is", result, "degree Celsius")

  print ("Convert again?")
  again = input()

  if again == '1':
    repeat = True
  elif again == '2':
    repeat = False
    print ("Thankyou for using this temperature converter!")
