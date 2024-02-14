import cv2
path ="D:/Build club project/Image processing/th.jpg"
image = cv2.imread(path)
cv2.imshow("Output",image)
cv2.waitKey()
cv2.destroyAllWindows()