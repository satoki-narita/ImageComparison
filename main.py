import cv2

# 2つの画像を読み込み
img1 = cv2.imread('C:/Users/satoki.narita/Desktop/hikaku/test1.png')
img2 = cv2.imread('C:/Users/satoki.narita/Desktop/hikaku/test2.png')

# 画像の差分を取得
diff = cv2.absdiff(img1, img2)

# 差分画像を表示
cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()