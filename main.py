import matplotlib.pyplot as plt
import numpy as np

from physics import compute_trajectory, compute_trajectory_with_drag
from plot import plot_trajectory, plot_axis_vs_time, plot_trajectory_comparison,optimization_plots, plot_velocity, animate_trajectory, acceleration_vs_time
from results import print_all_results, results_analysis, print_optimal_angle_results, print_drag_comparison, velocity_parameters, acceleration_parameters
from analysis import optimization_angle_no_drag, optimization_angle_with_drag

# ---------- User input ----------

while True:
    try:
        v0 = float(input("Velocity: "))

    except ValueError:
        print('Not a valid velocity')
        continue
    if v0 <= 0:
        print('The Velocity must be positive')
        continue

    break


while True:
    try:
        angle = float(input('What do you want the angle to be: '))

    except ValueError:
        print('Not a valid angle')
        continue

    if not (0 <= angle <= 90):
       print('Angle must be in between 0 and 90 degrees')
       continue
    break
   


while True:
    try:    
        y0 = float(input('What do you want your height offset to be: '))

    except ValueError:
        print('That is not an acceptable offset')
        continue

    if y0 < 0: 
        print('Offset cannot be less than zero')
        continue
    break

use_drag = input('Will air resistance be included? (yes/no):').lower()


if use_drag in ('y', 'yes'):


    
    mass = float(input('Ball Mass (kg):'))
    drag_cf = float(input('What is the coefficient of drag for the projectile:'))
    area = float(input('What is the area in (m^2) of the projectile:'))
    x_position, y_position,times, velocity, acceleration_x, acceleration_y = compute_trajectory_with_drag(v0, angle, mass, drag_cf, area, y0)
    x_nodrag, y_nodrag, t_nodrag, velocity_no_drag, acceleration_x_nodrag, acceleration_y_nodrag = compute_trajectory(v0, angle, y0)
    plot_trajectory_comparison(x_nodrag, y_nodrag, x_position, y_position) 
    results = results_analysis(x_nodrag, y_nodrag, t_nodrag)
    results_drag = results_analysis(x_position, y_position, times)
    print_all_results(
    *results_drag,
    angle,
    drag=True)
    print_all_results(*results, angle, drag = False)
    angles, ranges = optimization_angle_no_drag(
    v0,
    y0
    )

    optimal_angle = angles[np.argmax(ranges)]
    max_range = np.max(ranges)

    print_optimal_angle_results(
    optimal_angle,
    max_range,
    drag=False
    )

    angles_drag, ranges_drag = optimization_angle_with_drag(
        v0,
        y0,
        mass,
        drag_cf,
        area
    )

    optimal_drag_angle = angles_drag[np.argmax(ranges_drag)]
    max_range_drag = np.max(ranges_drag)
    print_optimal_angle_results(optimal_drag_angle,
                                max_range_drag, 
                                drag= True)
    print_optimal_angle_results(
    optimal_drag_angle,
    max_range_drag,
    drag=True
    )
    print_drag_comparison(
    max_range,
    max_range_drag
    )
    print_drag_comparison(
    max_range,
    max_range_drag
    )
    optimization_plots(angles_drag, 
                       ranges_drag
                        )
    

else: 
    x_position, y_position, times, velocity, acceleration_x, acceleration_y = compute_trajectory(v0,angle, y0)
    results = results_analysis(x_position, y_position, times)
    print_all_results(
        *results,
        angle,
        drag= False)
    angles, ranges = optimization_angle_no_drag(v0, 
                                                y0)
    optimal_angle = angles[np.argmax(ranges)]
    max_range = np.max(ranges)

    print_optimal_angle_results(
        optimal_angle,
        max_range,
        drag=False
    )

    optimization_plots(
        angles, 
        ranges
    )
    print_optimal_angle_results(
    optimal_angle,
    max_range,
    drag=False
)
    
plot_trajectory(x_position, y_position)
plot_axis_vs_time(times, x_position,y_position) 
plot_velocity(times,velocity)
velocity_parameters(times, velocity)
acceleration_vs_time(times, acceleration_x, acceleration_y)
acceleration_parameters(times, acceleration_x, acceleration_y)
ani = animate_trajectory(x_position, y_position)
plt.show()

