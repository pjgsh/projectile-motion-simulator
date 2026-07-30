import numpy as np 
from physics import compute_trajectory, compute_trajectory_with_drag
from analysis import optimization_angle_no_drag, optimization_angle_with_drag

def results_analysis(x,y,t): 
    """
    Calculates key projectile performance metrics.

    Returns:
        max_distance : maximum horizontal distance
        max_height   : maximum vertical height
        peak_time    : time to reach maximum height
        total_time   : total flight time
    """

    if len(x) == 0: 
        raise ValueError('Trajectory Calculation returned no data')
    max_distance = np.max(x)
    max_height = np.max(y)
    
    
    peak_time = np.argmax(y)
    peaktime = t[peak_time]
    total_time = t[-1]
    if len(x) == 0:
        raise ValueError("Trajectory calculation returned no data.")
    
    return max_distance, max_height, peaktime, total_time



def print_all_results(max_distance, max_height, peak_time, total_time, angle, drag=False):
    """
    Prints projectile performance summary.
    """

    drag_status = "with drag" if drag else "without drag"

    print(f"\nProjectile Results ({drag_status})")
    print("--------------------------------")
    print(f"Launch angle: {angle}°")
    print(f"Maximum horizontal distance: {max_distance:.2f} m")
    print(f"Maximum height: {max_height:.2f} m")
    print(f"Time to peak height: {peak_time:.2f} s")
    print(f"Total flight time: {total_time:.2f} s")

def print_optimal_angle_results(optimal_angle, max_range, drag=False):

    if drag:
        print("\n--- Projectile Optimization With Drag ---")
    else:
        print("\n--- Projectile Optimization Without Drag ---")

    print(f"Optimal Launch Angle: {optimal_angle:.0f} degrees")
    print(f"Maximum Range: {max_range:.2f} m")



def print_drag_comparison(no_drag_range, drag_range):

    range_loss = ((no_drag_range - drag_range) / no_drag_range) * 100

    print("\n--- Drag Effect Analysis ---")
    print(f"No Drag Maximum Range: {no_drag_range:.2f} m")
    print(f"With Drag Maximum Range: {drag_range:.2f} m")
    print(f"Range Reduction Due to Drag: {range_loss:.2f}%")


def velocity_parameters(times, velocity):

    dir_change_t = np.argmin(velocity)
    dir_change = times[dir_change_t]
    high_speed = np.max(velocity)

    print("\n--- Velocity Analysis ---")
    print(f'The projetile reached a max speed of {high_speed:.2f} m/s')
    print(f'The projectile changed direction at {dir_change} seconds')


def acceleration_parameters(times, acceleration_x, acceleration_y):


    fastest_x_acceleration = np.max(np.abs(acceleration_x))
    fastest_y_acceleration = np.max(np.abs(acceleration_y))
    time_x_acceleration = np.argmax(np.abs(acceleration_x))
    time_x = times[time_x_acceleration]
    time_y_acceleration = np.argmax(np.max(acceleration_y))
    time_y = times[time_y_acceleration]

    print("\n--- Acceleration Analysis---")
    print(f'The projectile accelerated the fastest at {time_x:.2f} with {fastest_x_acceleration:.2f} in the horizontal direction')
    print(f'The projectile accelerated the fastest at {time_y:.2f} with {fastest_y_acceleration:.2f} in the vertical direction')


