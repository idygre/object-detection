import cv2

# Define first frame
first_frame = None

# capture video via webcam
video_capture = cv2.VideoCapture(0)

# read the video, assign to frame while true
while True:
    check, frame = video_capture.read()

    # convert frame to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply a Gaussian Blur to gray image
    gray = cv2.GaussianBlur(gray, (20, 20), 0)

    # convert first frame to gray if it's the first and continue
    if first_frame == None:
        first_frame = gray
        continue

    # delta frame (compare first frame with current):
    # apply absolute difference to the first frame and gray current frame
    delta_frame = cv2.absdiff(first_frame, gray)

    # threshold: apply threshold tuple to the abs diff object at 30 and make it white(255)
    thresh = cv2.threshold(delta_frame, 30, 255)[1]

# show the gray image
    cv2.imshow("Gray", gray)
# show the abs diff delta frame
    cv2.imshow("delta abs diff", delta_frame)

# *****     When running, on webcam show background first        *****
