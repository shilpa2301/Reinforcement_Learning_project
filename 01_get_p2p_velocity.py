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


import pandas as pd
import os

file_path = os.path.join('Data', 'First_Set_for_imitation_Learning', 'data_8_clockwise', 'vehicle_waypoint.csv')
track_file = pd.read_csv(file_path)
print(track_file.columns)

velocities = calculate_velocity(track_file)
omegas = calculate_omega(track_file)

print("Velocity: ")
for i, velocity in enumerate(velocities):
    if i < 20:
        print(velocity)

print("Omega: ")
for i, omega in enumerate(omegas):
    if i < 20:
        print(omega)

