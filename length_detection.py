import cv2


scale = cv2.imread('opencv_frame_2.png', cv2.IMREAD_COLOR)
scale_gray = cv2.cvtColor(scale, cv2.COLOR_BGR2GRAY)
# adjust the second value of the next line to tune the detection
ret, thresh = cv2.threshold(scale_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# filter noisy detection
contours = [c for c in contours if cv2.contourArea(c) > 100]
# sort from by (y, x)
contours.sort(key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))
# work on the segment
cv2.rectangle(scale, cv2.boundingRect(contours[-1]), (0,255,0), 2)
x,y,w,h = cv2.boundingRect(contours[-1])
print(x,y,w,h)
# x,y: (39 152) w,h: [304 21]