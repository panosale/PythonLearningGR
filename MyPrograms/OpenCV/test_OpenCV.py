import cv2
# load it in GRAYSCALE color mode...
image1 = cv2.imread("""D:\My Documents\Programming\Python\OpenCV_tests\OpenCV_logo.png""", 0)
image2 = cv2.imread("""D:\My Documents\Programming\Python\OpenCV_tests\OpenCV_logo.png""", 0)
cv2.imshow('Analytics Vidhya Computer Vision', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
