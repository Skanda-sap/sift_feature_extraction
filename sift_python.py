
import cv2

#read images
img1 = cv2.imread("/home/skanda/coding/features/sift/images/book.jpg")
img2 = cv2.imread("/home/skanda/coding/features/sift/images/table.jpg")

#convert images to grayscale
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#create a SIFT object
sift = cv2.SIFT_create()

#detect SIFT features in both images
keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

#create feature matcher
bruteForceMatcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

#match descriptor of both images
matches = bruteForceMatcher.match(descriptors_1, descriptors_2)

#sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

#draw first 50 matches
matchedImage = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)

#display the images
cv2.imshow('image', matchedImage)
#save image
cv2.imwrite("/home/skanda/coding/features/sift/images/matchedImage.jpg",matchedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()