import cv2 as cv
import numpy as np

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / (gamma+1e-06)
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv.LUT(image, table)

## Make an adjustable trackbar
gamma = 100
window_name = 'Gamma Correction'
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
cv.createTrackbar("gamma, (* 0.01)", window_name, gamma, 300, lambda x:x)
# define a video capture object
vid = cv.VideoCapture(1)

while (True):
    ret, frame = vid.read()
    ## Do Operations Here
    g = cv.getTrackbarPos("gamma, (* 0.01)", window_name) * 0.01
    adjusted = adjust_gamma(frame, gamma=g).astype('uint8')

    ## Add Some text
    cv.putText(adjusted, "g={}".format(g), (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

    cv.imshow(window_name, np.hstack([frame, adjusted]))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv.destroyAllWindows()