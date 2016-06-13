'''In this project, we'll use Bitwise operators to build a calculator that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

We'll add three methods to the project:

A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle'''

def rgb_hex():
  invalid_msg = "Invalid input, please try again later."
  red = int(raw_input("Please input the value of Red: "))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input("Please input the value of Green: "))
  if green < 0 or green > 255:
    print invalid_msg
    return
  blue = int(raw_input("Please input the value of Blue: "))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  print "The Hex value is: %s" % ((hex(val)[2:]).upper())

  
def hex_rgb():
    hex_val = raw_input("Please input the Hex value: ")
    if len(hex_val) != 6:
      print "Invalid input, please try again later."
      return
    else:
      hex_val = int(hex_val, 16)
      two_hex_digits = 2**8
      blue = hex_val % two_hex_digits
      hex_val >>= 8
      green = hex_val % two_hex_digits
      hex_val >>= 8
      red = hex_val % two_hex_digits
      print "The RGB value is: %d,%d,%d" %(red, green, blue)
    
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to exit: ").upper()
    if option == "1":
      print "RGB to Hex..."
      rgb_hex()
    elif option == "2":
      print "Hex to RGB"
      hex_rgb()
    elif option == "X":
      print "Exit..."
      break
    else:
      print "Error"

convert()