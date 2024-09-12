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
        [scale * cos_a, -sin_a, tx],
        [sin_a, scale * cos_a, ty],
        [0, 0, 1]
    ]
)

inversed_M = np.linalg.inv(M)

new_img = np.zeros_like(img)

for new_y in range(new_img.shape[0]):
    for new_x in range(new_img.shape[1]):
        
        original_x, original_y, _ = np.matmul(inversed_M, [new_x, new_y, 1])
        original_x, original_y = int(original_x), int(original_y)

        if 0 <= original_x < img.shape[1] and 0 <= original_y < img.shape[0]:
            new_img[new_y, new_x] = img[original_y, original_x]

cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", new_img)
cv2.waitKey(0)
