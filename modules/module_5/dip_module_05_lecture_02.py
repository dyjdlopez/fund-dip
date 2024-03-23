import cv2 as cv

# define a video capture object
vid = cv.VideoCapture(1)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    ## Process
    # Display the resulting frame
    cv.imshow('frame', frame)

    # the 'q' button is set as the quitting button
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()