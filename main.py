import argparse
import cv2 as cv
import mediapipe as mp
from exercise import typeofexcercises
from utility import *

#argparse: a library for parsing command-line arguments
def get_video_capture(video_source):
    if video_source:
        return cv.VideoCapture("workout/" + video_source)
    else:
        return cv.VideoCapture(0)  # webcam

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--exercise_type", type=str, help='Type of activity to do', required=True)
    ap.add_argument("-vs", "--video_source", type=str, help='Type of activity to do', required=False)
    args = vars(ap.parse_args())

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = get_video_capture(args["video_source"])
    cap.set(3, 800)  # width
    cap.set(4, 480)  # height

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        counter = 0
        status = False
        while cap.isOpened():
            ret, frame = cap.read()

            frame = cv.resize(frame, (1200, 800), interpolation=cv.INTER_AREA)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame.flags.writeable = False

            results = pose.process(frame)

            frame.flags.writeable = True
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                counter, status = typeofexcercises(landmarks).calculate_exercise(args["exercise_type"], counter, status)
            except (ValueError, AttributeError):
                pass

            frame = score_table(args["exercise_type"], frame, counter, status)

            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2)
            )

            # Add any other necessary processing here

            cv.imshow("Exercise Pose Estimation", frame)
            if cv.waitKey(1) & 0xFF == ord('e'):
                break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
