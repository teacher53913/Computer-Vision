import cv2
#load the image
image=cv2.imread("image.png")
#convert the image to grayscale
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Resize the grayscale to fit a dimension
resized_image=cv2.resize(gray_image,(224,224))
#display the image
cv2.imshow("Processed image",resized_image)
#wait for a keypress
cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg',resized_image)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image was not saved")
#close the window, print the size of the picture
