import pandas as pd


def calculate_velocity(df):
    velocities = []

    for i in range(1, len(df)):
        x1, y1 = df.iloc[i - 1]['X'], df.iloc[i - 1]['Y']
        x2, y2 = df.iloc[i]['X'], df.iloc[i]['Y']

        # Calculate velocity between two points
        v = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
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

import pandas as pd
import os

print(os.getcwd())
dir_path = os.path.join('Data', 'First_Set_for_imitation_Learning', 'interpolated_8_clockwise')
result_path = os.path.join('Data', 'First_Set_for_imitation_Learning', 'results')
for file in os.listdir(dir_path):
    file_path = os.path.join(os.getcwd(), dir_path, file)
    print(file_path)
    track_file = pd.read_csv(file_path)
    print(track_file.columns)
    velocities = calculate_velocity(track_file)
    omegas = calculate_omega(track_file)

    print("Velocity: ")
    printlines(velocities, 0, 20)

    print("Omega: ")
    printlines(omegas, 0, 20)

    # write out the results here




