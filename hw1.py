import numpy as np
import cv2

img = cv2.imread("img/cat.jpg")

scale = 0.5
angle = 15
tx = 20
ty = -60

angle_rad = np.deg2rad(angle)
cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)

M = np.array(
    [
        [scale * cos_a,     -sin_a,             tx],
        [sin_a,             scale * cos_a,      ty],
        [0,                 0,                  1],
    ]
)

new_img = np.zeros(img.shape, dtype=np.uint8)

for original_y in range(img.shape[0]):
    for orginal_x in range(img.shape[1]):
        
        new_x, new_y, _ = np.matmul(M, [orginal_x, original_y, 1])
        new_x, new_y = int(new_x), int(new_y)
        
        if 0 <= new_x < img.shape[1] and 0 <= new_y < img.shape[0]:
            new_img[new_y, new_x] = img[original_y, orginal_x]

inversed_M = np.linalg.inv(M)
recovered_img = np.zeros(new_img.shape, dtype=np.uint8)

for original_y in range(new_img.shape[0]):
    for original_x in range(new_img.shape[1]):
        
        new_x, new_y, _ = np.matmul(inversed_M, [orginal_x, original_y, 1])
        new_x, new_y = int(new_x), int(new_y)
        
        if 0 <= new_x < img.shape[1] and 0 <= new_y < img.shape[0]:
            recovered_img[new_y, new_x] = new_img[original_y, original_x]

cv2.imshow("original image", img)
cv2.imshow("transferd image", new_img)
cv2.imshow("rovered image", recovered_img)
cv2.waitKey(0)



