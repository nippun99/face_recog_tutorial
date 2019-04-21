import cv2
img = cv2.imread('scn.jpg')
px = img[55,55]
img[55,55] = [255,255,255]
px = img[55,55]
print(px)
roi = img[100:150,100:150]
print(roi)
img[100:150,100:150] = [255,255,255]
cv2.rectangle(img, (100, 100), (150,150 ), (255, 0, 0), 2)
cv2.circle(img, (97,97),44, (0,255,0), thickness=1, lineType=8)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
