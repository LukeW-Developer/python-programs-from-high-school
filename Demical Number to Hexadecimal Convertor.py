# HEX Subroutine
def HEX(x):
    val = hex(x)[2:] # Removes 0x at the beginning so we get an answer like 8F rather than 0x8F
    val = "0"+val if len(val)<2 else val # Make sure that it is 2 digits
    print(val.upper())

# Start of the Program (Input and sets the range)
x = int(input("Decimal Number: "))
check = range(0, 256)

# Making sure its between 0-255 and a actual whole number
if x < 0:
    print("Please enter a number thats above 0")
elif x > 255:
    print("Please choose a number thats below 256")
elif x in check:
    HEX(x)
else:
    print("Error. Please make sure that the number you entered was a whole number")
