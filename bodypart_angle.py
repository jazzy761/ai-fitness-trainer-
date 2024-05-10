from utility import *


class BodyPartAngle:

    def __init__(self , landmarks):
        self.landmarks = landmarks

    def angle_of_the_left_arm(self):
        l_shoulder = detect_body_part(self.landmarks, "LEFT_SHOULDER")
        l_elbow = detect_body_part(self.landmarks, "LEFT_ELBOW")
        l_wrist = detect_body_part(self.landmarks, "LEFT_WRIST")
        return calc_angle(l_shoulder, l_elbow, l_wrist)

    def angle_of_the_right_arm(self):
        r_shoulder = detect_body_part(self.landmarks, "RIGHT_SHOULDER")
        r_elbow = detect_body_part(self.landmarks, "RIGHT_ELBOW")
        r_wrist = detect_body_part(self.landmarks, "RIGHT_WRIST")
        return calc_angle(r_shoulder, r_elbow, r_wrist)

    def angle_of_the_left_leg(self):
        l_hip = detect_body_part(self.landmarks, "LEFT_HIP")
        l_knee = detect_body_part(self.landmarks, "LEFT_KNEE")
        l_ankle = detect_body_part(self.landmarks, "LEFT_ANKLE")
        return calc_angle(l_hip, l_knee, l_ankle)

    def angle_of_the_right_leg(self):
        r_hip = detect_body_part(self.landmarks, "RIGHT_HIP")
        r_knee = detect_body_part(self.landmarks, "RIGHT_KNEE")
        r_ankle = detect_body_part(self.landmarks, "RIGHT_ANKLE")
        return calc_angle(r_hip, r_knee, r_ankle)

    def angle_of_the_neck(self):
        r_shoulder = detect_body_part(self.landmarks, "RIGHT_SHOULDER")
        l_shoulder = detect_body_part(self.landmarks, "LEFT_SHOULDER")
        r_mouth = detect_body_part(self.landmarks, "MOUTH_RIGHT")
        l_mouth = detect_body_part(self.landmarks, "MOUTH_LEFT")
        r_hip = detect_body_part(self.landmarks, "RIGHT_HIP")
        l_hip = detect_body_part(self.landmarks, "LEFT_HIP")

        shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
                        (r_shoulder[1] + l_shoulder[1]) / 2]
        mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2,
                     (r_mouth[1] + l_mouth[1]) / 2]
        hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

        return abs(180 - calc_angle(mouth_avg, shoulder_avg, hip_avg))

    def angle_of_the_abdomen(self):
        # calculate angle of the avg shoulder
        r_shoulder = detect_body_part(self.landmarks, "RIGHT_SHOULDER")
        l_shoulder = detect_body_part(self.landmarks, "LEFT_SHOULDER")
        shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
                        (r_shoulder[1] + l_shoulder[1]) / 2]

        # calculate angle of the avg hip
        r_hip = detect_body_part(self.landmarks, "RIGHT_HIP")
        l_hip = detect_body_part(self.landmarks, "LEFT_HIP")
        hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

        # calculate angle of the avg knee
        r_knee = detect_body_part(self.landmarks, "RIGHT_KNEE")
        l_knee = detect_body_part(self.landmarks, "LEFT_KNEE")
        knee_avg = [(r_knee[0] + l_knee[0]) / 2, (r_knee[1] + l_knee[1]) / 2]

        return calc_angle(shoulder_avg, hip_avg, knee_avg)

    













