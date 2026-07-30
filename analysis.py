import numpy as np
from physics import compute_trajectory, compute_trajectory_with_drag

def optimization_angle_no_drag(v0,y0):

    angles = np.arange(0,91)
    ranges = []

    for angle in angles:

        if angle == 0 and y0 == 0:
            ranges.append(0)
            continue

        x,y,t, velocity, acceleration_x, acceleration_y = compute_trajectory(v0, angle, y0)
        ranges.append(np.max(x))

    return angles, np.array(ranges)


def optimization_angle_with_drag(v0,y0,mass,drag_cf, area, angle_step = 1):

    angles = np.arange(0,91, angle_step)
    ranges = []

    for angle in angles:
        if angle == 0 and y0 == 0:
            ranges.append(0)
            continue

        x,y,t, velocity, acceleration_x, acceleration_y = compute_trajectory_with_drag(
            v0,
            angle,
            mass,
            drag_cf,
            area,
            y0)
        ranges.append(np.max(x))

    return angles, np.array(ranges)









