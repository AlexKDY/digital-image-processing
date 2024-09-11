import numpy as np
import cv2

# 원본 이미지를 불러옵니다.
img = cv2.imread("img/cat.jpg")

# 변환 매개변수 정의
scale = 0.5
angle = 15
tx = 20
ty = -60

# 각도를 라디안으로 변환하고 삼각함수 계산
angle_rad = np.deg2rad(angle)
cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)

# 변환 행렬 M (이미지 크기 조정, 회전, 평행 이동 포함)
M = np.array(
    [
        [scale * cos_a,     -sin_a,             tx],
        [sin_a,             scale * cos_a,      ty],
        [0,                 0,                  1],
    ]
)

# 변환된 이미지를 저장할 배열을 초기화합니다.
new_img = np.zeros(img.shape, dtype=np.uint8)

# 변환을 적용하여 새로운 이미지를 생성합니다.
for original_y in range(img.shape[0]):
    for orginal_x in range(img.shape[1]):
        # 원본 좌표에 변환 행렬을 적용하여 새로운 좌표 계산
        new_x, new_y, _ = np.matmul(M, [orginal_x, original_y, 1])
        new_x, new_y = int(new_x), int(new_y)

        # 계산된 좌표가 이미지 범위 내에 있는지 확인
        if 0 <= new_x < img.shape[1] and 0 <= new_y < img.shape[0]:
            # 변환된 이미지에 원래 픽셀 값을 저장
            new_img[new_y, new_x] = img[original_y, orginal_x]

# 역변환을 위한 코드
# 변환 행렬의 역행렬을 구합니다.
M_inv = np.linalg.inv(M)

# 역변환된 이미지를 저장할 배열을 초기화합니다.
recovered_img = np.zeros(new_img.shape, dtype=np.uint8)

# 변환된 이미지에서 역변환을 적용하여 원본 이미지를 복원합니다.
for new_y in range(new_img.shape[0]):
    for new_x in range(new_img.shape[1]):
        # 변환된 좌표에 역행렬을 적용하여 원래 좌표 계산
        original_x, original_y, _ = np.matmul(M_inv, [new_x, new_y, 1])
        original_x, original_y = int(original_x), int(original_y)

        # 원래 좌표가 이미지 범위 내에 있는지 확인
        if 0 <= original_x < new_img.shape[1] and 0 <= original_y < new_img.shape[0]:
            # 원래 이미지 좌표에 해당하는 픽셀 값을 복원된 이미지에 저장
            recovered_img[new_y, new_x] = new_img[original_y, original_x]

# 결과를 화면에 출력합니다.
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image", new_img)
cv2.imshow("Recovered Image", recovered_img)
cv2.waitKey(0)
