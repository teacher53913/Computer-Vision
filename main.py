import cv2
#load the image
image=cv2.imread("image.png")
#resize the window to fit the image
cv2.namedWindow('Loaded Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image',800,500)
#display the image in the window
cv2.imshow('Loaded Image',image)
cv2.waitKey(0)
#close the window
cv2.destroyAllWindows()
#display the image dimensions
print(f"Image Dimensions:{image.shape}")