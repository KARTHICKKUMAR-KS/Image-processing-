import cv2

path = "D:/Build club project/Image processing/th - Copy.jpg"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite('D:/Build club project/Image processing/th - Copy.jpg',image_gray)

cv2.waitKey()
cv2.destroyAllWindows()

