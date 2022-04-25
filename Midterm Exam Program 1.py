#Program 1: Modify the program below by adding two conversion methods - Fahrenheit to Celsius and Kelvin to Celsius (50 points)

def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32
 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15
 class FahrenheitToCelsius(TemperatureConversion):
  def conversion(self):
   return (self._temp - 32) * 5/9
 class KelvinToCelsius(TemperatureConversion):
  def conversion(self):
   return self._temp - 273.15

 temperature = float(input("Enter the temperature: "))
 convert = CelsiusToKelvin(temperature)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(temperature)
 print(str(convert.conversion()) + " Fahrenheit")
 convert = FahrenheitToCelsius(temperature)
 print(str(convert.conversion()) + " Celsius")
 convert = KelvinToCelsius(temperature)
 print(str(convert.conversion()) + " Celsius")

main()
