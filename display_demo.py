import time

from display import epd4in2bc
from PIL import Image, ImageDraw

epd = epd4in2bc.EPD()

print("Init and clear")
epd.init()
epd.Clear()
time.sleep(1)

# Create a blank, white image for the black data
black_image = Image.new("1", (epd.width, epd.height), 255)

# Create a blank, white image for the red data
red_image = Image.new("1", (epd.width, epd.height), 255)

# Create drawing objects for each image
draw_black = ImageDraw.Draw(black_image)
draw_red = ImageDraw.Draw(red_image)

# Draw a black rectangle on the left half of the black_image
# The coordinates are (x_start, y_start, x_end, y_end)
# The rectangle goes from (0, 0) to (200, 300)
draw_black.rectangle((0, 0, epd.width // 2, epd.height), fill=0)

# Draw a black rectangle on the right half of the red_image
# The rectangle goes from (200, 0) to (400, 300)
draw_red.rectangle((epd.width // 2, 0, epd.width, epd.height), fill=0)

print("Rendering image...")
epd.display(epd.getbuffer(black_image), epd.getbuffer(red_image))

# print("Waiting 20 seconds...")
# time.sleep(20)

# print("Cleaning")
# epd.init()
# epd.Clear()

# print("Going to sleep")
# epd.sleep()
