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


# Example usage
import pandas as pd
import os

file_path = os.path.join('Data', 'First_Set_for_imitation_Learning', 'data_8_clockwise', 'vehicle_waypoint.csv')
track_file = pd.read_csv(file_path)
print(track_file.columns)

pid = PID(1, 0, 0)  # Just example values; tune them according to your needs
velocities = calculate_velocity(track_file, pid)

for velocity in velocities:
    print(velocity)