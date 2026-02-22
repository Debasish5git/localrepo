unit = input("Is the temperature in Celcius or Fahrenheit(C/F)?: ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp*9/5)+32
    print(f"The temperature in Fahrenheit is {round(temp, 2)} F")
elif unit == "F":
    temp = (temp-32)*5/9
    print(f"The temperature in celcius is {round(temp, 2)} C")
else:
    print(f"The unit {unit} is invalid")