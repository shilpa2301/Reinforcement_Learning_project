import pandas as pd


class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.cumulative_error = 0

    def compute(self, set_point, current_position):
        # Compute 2D Euclidean error
        error = ((set_point[0] - current_position[0]) ** 2 + (set_point[1] - current_position[1]) ** 2) ** 0.5

        self.cumulative_error += error
        differential_error = error - self.prev_error

        # PID formula
        output = (self.kp * error) + (self.ki * self.cumulative_error) + (self.kd * differential_error)

        self.prev_error = error
        return output


def calculate_velocity(df, pid_controller):
    velocities = []

    for i in range(1, len(df)):
        current_position = (df.iloc[i - 1]['X'], df.iloc[i - 1]['Y'])
        set_point = (df.iloc[i]['X'], df.iloc[i]['Y'])
        v = pid_controller.compute(set_point, current_position)
        velocities.append(v)

    return velocities


def calculate_omega(df):
    omegas = []
    for i in range(1, len(df)):
        angle1 = df.iloc[i - 1]['Yaw']
        angle2 = df.iloc[i]['Yaw']

        # Calculate velocity between two points
        omega = angle2 - angle1
        omegas.append(omega)

    return omegas


def printlines(list, start_line, end_line):
    for i, item in enumerate(list):
        if end_line > i > start_line:
            print(item)


# Example usage
import pandas as pd
import os

print(os.getcwd())
dir_path = os.path.join('Data', 'First_Set_for_imitation_Learning', 'interpolated_8_clockwise')
result_path = os.path.join('Data', 'First_Set_for_imitation_Learning', 'results')

pid = PID(1, 0, 0)  # Just example values; tune them according to your needs

for file in os.listdir(dir_path):
    file_path = os.path.join(os.getcwd(), dir_path, file)
    print(file_path)
    track_file = pd.read_csv(file_path)
    print(track_file.columns)
    velocities = calculate_velocity(track_file, pid)
    omegas = calculate_omega(track_file)

    print("Velocity: ")
    printlines(velocities, 0, 20)

    print("Omega: ")
    printlines(omegas, 0, 20)

    # write out the results here
