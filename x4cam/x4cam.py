import cv2
from timecontext import Timer
import numpy as np


def gstreamer_pipeline(
    sensor_id=0,
    sensor_mode=3,
    capture_width=1280,
    capture_height=720,
    display_width=480,
    display_height=270,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d sensor-mode=%d ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            sensor_mode,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def show_camera():
    # Modify the flip_method parameter
    print(gstreamer_pipeline(flip_method=0))
    left_cap = cv2.VideoCapture(
        gstreamer_pipeline(flip_method=0,display_width=480,display_height=270,framerate=30), cv2.CAP_GSTREAMER)
    right_cap = cv2.VideoCapture(gstreamer_pipeline(
        flip_method=0, sensor_id=1,display_width=480,display_height=270,framerate=30), cv2.CAP_GSTREAMER)
    top_cap = cv2.VideoCapture(gstreamer_pipeline(
        flip_method=0, sensor_id=2,display_width=480,display_height=270,framerate=30), cv2.CAP_GSTREAMER)
    sub_cap = cv2.VideoCapture(gstreamer_pipeline(
        flip_method=0, sensor_id=3,display_width=480,display_height=270,framerate=30), cv2.CAP_GSTREAMER)
    if left_cap.isOpened():
        cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        # Window
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            with Timer() as context_time:
                ret_val, left_image = left_cap.read()
                ret_val, right_image = right_cap.read()
                ret_val, top_image = top_cap.read()
                ret_val, sub_image = sub_cap.read()
                # print(context_time.elapsed)
                # Images are stacked horizontally
                camera_images = np.hstack((left_image, right_image, top_image, sub_image))
                cv2.imshow("CSI Cameras", camera_images)
                # cv2.imshow("CSI Camera", left_image)
                # print(context_time.elapsed)

                keyCode = cv2.waitKey(20) & 0xFF
            # print(context_time.elapsed)
            # print("---")
            # ESC key to stop the program
            if keyCode == 27:
                break
        left_cap.release()
        right_cap.release()
        top_cap.release()
        sub_cap.release()
        cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":
    show_camera()
