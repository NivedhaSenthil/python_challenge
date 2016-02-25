from PIL import Image

input_image = Image.open("oxygen.png")
output = ""
count = 0
while count < 629:
    output += chr(input_image.getpixel((count,47))[0])
    count += 7

output = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(map(chr,output))
