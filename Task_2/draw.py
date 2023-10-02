import numpy as np
import cv2

print(cv2.__version__)

image = np.full((500,500,3),255,dtype=np.uint8)

cv2.line(image,(0,250),(500,250),(28.6,32.5,100),4)

cv2.rectangle(image,(0,0),(500,500),(133,21,199),4)

cv2.circle(image,(250,250),(250),(226,43,138),4)

cv2.ellipse(image,(250,250),(250,100),(0),(0),(360),(128,128,0),4)

cv2.imshow("image",image)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
    