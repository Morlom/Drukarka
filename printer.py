from PIL import Image
import numpy
import easygui
import serial
import time

#initiate connection with arduino
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

#open image file and get it's size
path = easygui.fileopenbox()
img = Image.open(path)
width, height = img.size

#maximal size on longest edge in pixels
size = 50

#calculate size of image
if width > height:
    reswidth = size
    resheight = int((size*height)/width)
else:
    resheight = size
    reswidth = int((size*width)/height)

#print calculated image size
#print(reswidth)
#print(resheight)

#resize image
img = img.resize((reswidth, resheight), Image.ANTIALIAS)

#convert image to black and white
thresh = 200
fn = lambda x : 255 if x > thresh else 0
img = img.convert('L').point(fn, mode='1')

#save image to jpg
#img.save('resshape.jpg', format='JPEG')

#transfer to array
array = numpy.array(img, dtype=numpy.uint8)

#print array in console output

for i in range (0, resheight-1):
    for j in range (0, reswidth-1):
        print(array[i][j], end='')
    print('')


#save image to png
"""
im = Image.fromarray(array * 255)
im.show()
im.save('resshape.png', format='PNG')
"""


#send to arduino function
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(ts)

    #print data received by arduino
    data = arduino.readline()
    data = data.decode('utf-8')
    print(data)

#sleep time before next command
ts = 0.3

#main printing code  Y=1 Z=2 X=3 DL=4 DH=5
for i in range (0, resheight-1):
    if i == 0 or i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i%2 == 0:
        for j in range (0, reswidth-1):
            
            if array[i][j] == 0:
                write_read('1')
                time.sleep(ts)
                write_read('3')
                time.sleep(ts)
            else:
                time.sleep(ts)
                write_read('3')
                time.sleep(ts)
        if array[i][j] == 0:
            write_read('1')
            time.sleep(ts)
        write_read('2')
        time.sleep(ts)
        write_read('5')
        time.sleep(ts)
    else:
        for j in range (reswidth-1, 0, -1):
            if array[i][j] == 0:
                write_read('1')
                time.sleep(ts)
                write_read('3')
                time.sleep(ts)
            else:
                time.sleep(ts)
                write_read('3')
                time.sleep(ts)
        if array[i][j] == 0:
            write_read('1')
            time.sleep(ts)
        write_read('2')
        time.sleep(ts)
        write_read('4')
        time.sleep(ts)