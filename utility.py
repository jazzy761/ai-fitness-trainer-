import cv2 as cv
import mediapipe as mp
import numpy as np
import pandas as pd

mp_pose = mp.solutions.pose


def calc_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)  #Taking the points a, b, c and converting them to numpy arrays

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
              np.arctan2(a[1] - b[1], a[0] - b[0])  #calculating the radian angle between pints ab, bc, cb etc
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


def detect_body_part(landmarks, body_part_name): #this function detects the body parts
    return [
        landmarks[mp_pose.PoseLandmark[body_part_name].value].x,  #the function .PoseLandmarks is containing a dictionary , this dictionary is conatining mapping betwwen names of body part and thier index in list
        landmarks[mp_pose.PoseLandmark[body_part_name].value].y,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].visibility # this function has 2 options 0 , where a body part is partially visible or not at all , and 1 where body part is fully visibable
    ]


def detect_body_parts(landmarks):
    body_parts = pd.DataFrame(columns=["body_parts", "x", "y"])

    for i, landmark in enumerate(mp_pose.PoseLandmark):
        landmark = str(landmark).split(".")[1]
        cord = detect_body_part(landmarks, landmark)
        body_parts.loc[i] = landmark, cord[0], cord[1]

    return body_parts

def score_table(exercise, frames, counter, status): #using basic cv function we make a score table
    cv.putText(frames, "Activity : " + exercise.replace("-", " "),
               (10, 65), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 128, 0), 2,
               cv.LINE_AA)
    cv.putText(frames, "Counter : " + str(counter), (10, 100),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 128, 0), 2, cv.LINE_AA)
    cv.putText(frames, "Status : " + str(status), (10, 135),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 128, 0), 2, cv.LINE_AA)
    return frames
# the score level , tells your posture if correct or not , if correct counter goes up