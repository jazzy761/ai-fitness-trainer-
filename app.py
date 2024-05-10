import argparse
import sys

import cv2 as cv
import mediapipe as mp
from exercise import typeofexcercises
from utility import *
import streamlit as st

def get_video_capture(video_source):
    if video_source:
        return cv.VideoCapture("workout/" + video_source)
    else:
        return cv.VideoCapture(0)  # webcam

def main(exercise):
    global exercise_type
    exercise_type = exercise

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    st.title("AI Trainer ")
    st.write("Select a video file or use the webcam")

    cap = None

    if st.button("Upload a video"):
        uploaded_file = st.file_uploader("", type="mp4")
        if uploaded_file is not None:
            cap = get_video_capture(uploaded_file.name)
    elif st.button("Use Webcam"):
        cap = get_video_capture(None)

    if cap is not None:
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
                    counter, status = typeofexcercises(landmarks).calculate_exercise(exercise_type, counter, status)
                except (ValueError, AttributeError):
                    pass

                frame = score_table(exercise_type, frame, counter, status)

                mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2)
                )

                # Add any other necessary processing here

                cv.imshow("AI Trainer", frame)
                if cv.waitKey(1) & 0xFF == ord('e'):
                    break

        cap.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    exercise = "hammercurl"  # Set the default exercise type
    if len(sys.argv) > 1:
        exercise = sys.argv[1]
    main(exercise)


#streamlit run app.py <excercisename>