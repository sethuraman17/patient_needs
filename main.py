import cv2
import time

cap = cv2.VideoCapture(0)

count = 0

while True:
    success, frame = cap.read()
    count = count+1
    name = './images/'+'restroom'+'/'+'restroom'+str(count)+'.jpg'
    cv2.imwrite(name, frame)
    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)
    time.sleep(2)
    if count > 30 or k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
