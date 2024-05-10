from bodypart_angle import BodyPartAngle
from utility import *


class typeofexcercises(BodyPartAngle):

    def __init__(self, landmarks):
        super().__init__(landmarks)

    def pushup(self, counter, status):

        l_arm_angle = self.angle_of_the_left_arm()
        r_arm_angle = self.angle_of_the_right_arm()
        avg_arm_angle = (l_arm_angle + r_arm_angle) / 2

        if status:
            if avg_arm_angle < 70:
                status = False
        else:

            if avg_arm_angle > 160:
                counter += 1
                status = True

        return [counter, status]

    def pullup(self, counter, status):
        nose = detect_body_part(self.landmarks, "NOSE")
        left_shoulder = detect_body_part(self.landmarks, "LEFT_SHOULDER")
        right_shoulder = detect_body_part(self.landmarks, "RIGHT_SHOULDER")
        avg_shoulder = (right_shoulder + left_shoulder) / 2

        if status:
            if nose[1] > avg_shoulder:
                status = False

        else:
            if nose[1] < avg_shoulder:
                counter += 1
                status = True

        return [counter, status]

    def squat(self, counter, status):

        l_leg_angle = self.angle_of_the_left_leg()
        r_leg_angle = self.angle_of_the_right_leg()
        avg_leg_angle = (l_leg_angle + r_leg_angle) / 2

        if status:

            if avg_leg_angle < 70:
                status = False

        else:

            if avg_leg_angle > 160:
                status = True
                counter += 1

        return [counter, status]

    def situp(self, counter, status):
        abdomen_angle = self.angle_of_the_abdomen()

        if status:
            if abdomen_angle > 150:

                status = False
        else:
            if abdomen_angle < 100:
                counter += 1
                status = True

        return [counter, status]

    def bicepcurl(self, counter, status):

        l_arm_angle = self.angle_of_the_left_arm()
        r_arm_angle = self.angle_of_the_right_arm()

        if status:
            if l_arm_angle > 160 and r_arm_angle > 160:
                status = False

        else:

            if l_arm_angle < 70 and r_arm_angle < 70:
                counter += 1
                status = True

        return [counter, status]

    def hammercurl(self, counter, status):

        l_arm_angle = self.angle_of_the_left_arm()
        r_arm_angle = self.angle_of_the_right_arm()

        if status:
            if l_arm_angle > 150 and r_arm_angle > 150:
                status = False

        else:

            if l_arm_angle < 80 and r_arm_angle < 80:
                counter += 1
                status = True

        return [counter, status]



    def calculate_exercise(self, exercise_type, counter, status):
        if exercise_type == "pushup":
            counter, status = typeofexcercises(self.landmarks).pushup(counter, status)
        elif exercise_type == "pullup":
            counter, status = typeofexcercises(self.landmarks).pullup(counter, status)
        elif exercise_type == "squat":
            counter, status = typeofexcercises(self.landmarks).squat(counter, status)
        elif exercise_type == "situp":
            counter, status = typeofexcercises(self.landmarks).situp(counter, status)
        elif exercise_type == "bicepcurl":
            counter, status = typeofexcercises(self.landmarks).bicepcurl(counter, status)
        elif exercise_type == "hammercurl":
            counter, status = typeofexcercises(self.landmarks).hammercurl(counter, status)

        return [counter, status]
