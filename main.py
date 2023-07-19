import numpy
import cv2
import math

def img_rot(src_image, deg):
    #convert from degress to radians
    rad = math.radians(deg)

    #store value of source image height and width
    src_h, src_w = src_image.shape[0], src_image.shape[1]
    mid_x_src, mid_y_src = src_w//2, src_h//2

    #calculate value of output image height and width
    out_h = round(abs(src_w*math.sin(rad)) + abs(src_h*math.cos(rad)))
    out_w = round(abs(src_w*math.cos(rad)) + abs(src_h*math.sin(rad)))
    
    #calculate mid point to use as origin
    mid_x_out, mid_y_out = out_w//2, out_h//2
    out_image = numpy.uint8(numpy.zeros((out_h, out_w, src_image.shape[2])))

    for i in range(src_h):
        for j in range(src_w):
            #transformation and rotation
            x = round((j-mid_x_src) * math.cos(rad) + (i-mid_y_src) * math.sin(rad))
            y = round(-(j-mid_x_src)*math.sin(rad) + (i-mid_y_src)*math.cos(rad))

            #transform back
            x += mid_x_out
            y += mid_y_out

            #check if in bound
            if 0 <= x < out_w and 0 <=y <out_h:
                out_image[y][x] = src_image[i][j]
    
    #this block of code is similar to the top block. it is used to fill out the hole when there is error from converting from float to int
    for i in range(out_h):
        for j in range(out_w):
            x = round((j-mid_x_out) * math.cos(rad)-(i-mid_y_out)*math.sin(rad))
            y = round((j-mid_x_out)* math.sin(rad) + (i-mid_y_out)* math.cos(rad))

            x += mid_x_src
            y += mid_y_src

            if 0 <= x < src_w and 0 <= y < src_h:
                out_image[i][j] = src_image[y][x]
                
    return out_image


#main
#you can put any image you want
src_image = cv2.imread("sunflower.jpg")
#in this case 120 is the angle of rotation
out_image = img_rot(src_image, 120)
#output new image
cv2.imwrite("new_sunflower2.jpg", out_image)
print("Success!")