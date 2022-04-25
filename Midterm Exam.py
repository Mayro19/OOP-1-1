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

from tkinter import *
window = Tk()

window.geometry("600x300+30+10")
window. title("Midterm in OOP")

lbl = Label(window, text="Enter your fullname: ", fg="red", font=("verdana", 10))
lbl.place(x=70,y=80)

txtfld = Entry(window, bd=3, font=("times new roman", 12))
txtfld.place(x=290, y=80)

txtfld2 = Entry(window, bd=3, font=("times new roman", 12))
txtfld2.place(x=290, y=150)

def clicked():
    value=txtfld.get()
    txtfld2.insert(END, str(value))

bttn= Button(window, text="Click to display your Fullname", fg="red", command=clicked)
bttn.place(x=70, y=150)


window.mainloop()