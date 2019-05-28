def temp_foo(celcius):
    fahrenheit = float(celcius) * 9/5 + 32
    return fahrenheit

celcius = input("Enter temperature in celcius: ")
print("Temperature in Fahrenheit: ",temp_foo(celcius))
