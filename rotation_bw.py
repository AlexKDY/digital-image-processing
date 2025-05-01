# Backward Transform
import cv2
import numpy as np

def backward_transform(img, angle):
    height, width = img.shape
    result = np.zeros((height, width), np.uint8)

    affine_inv = np.array([[np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0],
                           [-np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
                           [0, 0, 1]])

    for x in range(width):
        for y in range(height):

            p = affine_inv.dot(np.array([x, y, 1]))
            xp = int(p[0])
            yp = int(p[1])

            if 0 <= yp < height and 0 <= xp < width:
                result[y, x] = img[yp, xp]

    return result

in_image = cv2.imread('img/dgu_gray.png', 0)

out_image = backward_transform(in_image, 20)

cv2.imshow('Input Image', in_image)
cv2.imshow('Result Image', out_image)

cv2.imwrite('img/dgu_gray_rotate_bw.png', out_image) 
cv2.waitKey()
