import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation




line_style = dict( marker=".",
        ms=5,
        markerfacecolor='skyblue',
        markeredgecolor='red',
        linestyle='solid',
        linewidth=5,)
def plot_trajectory(x_t, y_t):
        plt.figure()
        plt.plot(x_t,y_t, color='#afc431', **line_style)
        plt.title('Horizontal distance(m) vs Vertical distance(m)')
        plt.xlabel('Horizontal Distance (m)')
        plt.ylabel('Vertical Distance (m)')
        plt.grid(True)

def plot_axis_vs_time(t, x_t, y_t):

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))

        axes[0].plot(t, x_t)
        axes[0].set_xlabel("Time (s)")
        axes[0].set_ylabel("x position (m)")
        axes[0].set_title("Horizontal position over time")
        axes[0].grid(True)

        axes[1].plot(t, y_t)
        axes[1].set_xlabel("Time (s)")
        axes[1].set_ylabel("y position (m)")
        axes[1].set_title("Vertical position over time")
        axes[1].grid(True)

        plt.tight_layout()

def plot_trajectory_comparison(x_nodrag, y_nodrag,x_wdrag,y_wdrag):

        plt.figure()
        plt.plot(x_nodrag, y_nodrag, label = 'No Drag')
        plt.plot(x_wdrag, y_wdrag, label = 'Drag')
        plt.title('Trajectory Comparison with & without drag')
        plt.xlabel('Horizontal Distance (m)')
        plt.ylabel('Vertical Distance (m)')
        plt.legend()
        plt.grid(True)


def optimization_plots(angles, ranges):
        plt.figure()
        plt.plot(angles, ranges)
        plt.xlabel("Launch Angle (degrees)")
        plt.ylabel("Range (m)")
        plt.title("Projectile Range vs Launch Angle")
        peak_index = np.argmax(ranges)

        optimal_angle = angles[peak_index]
        max_range = ranges[peak_index]

        plt.scatter(optimal_angle, max_range, color = "#941818")

        plt.legend([
                f"Maximum Range: {max_range:.2f} m at {optimal_angle}°"])
        plt.annotate(
                f"({optimal_angle:.0f}°, {max_range:.2f} m)",
                (optimal_angle, max_range),
                xytext=(-40, -40),
                textcoords="offset points",
                fontsize=10,
                arrowprops=dict(arrowstyle="->")
)
        plt.grid(True)



def plot_velocity(time, velocity):
        plt.figure()
        plt.plot(time, velocity)
        plt.xlabel('Time (s)')
        plt.ylabel('Speed (m/s)')
        plt.title('Velocity Graph')   
        plt.grid(True)    

def acceleration_vs_time(t, acceleration_x, acceleration_y):
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))


        axes[0].plot(t, acceleration_x)
        axes[0].set_title("Horizontal Acceleration")
        axes[0].set_xlabel("Time (s)")
        axes[0].set_ylabel("Acceleration (m/s²)")
        axes[0].grid(True)

        axes[1].plot(t, acceleration_y)
        axes[1].set_title("Vertical Acceleration")
        axes[1].set_xlabel("Time (s)")
        axes[1].set_ylabel("Acceleration (m/s²)")
        axes[1].grid(True)

        plt.tight_layout()

def animate_trajectory(x_t, y_t):
    fig, ax = plt.subplots()
    ax.set_xlim(0, np.max(x_t) * 1.1)
    ax.set_ylim(0, np.max(y_t) * 1.1)
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Distance (m)")

    point, = ax.plot([], [], 'ro', markersize=10)   # the ball
    trail, = ax.plot([], [], '-', color='#378ADD')  # the trailing line

    def update(frame):
        point.set_data([x_t[frame]], [y_t[frame]])
        trail.set_data(x_t[:frame+1], y_t[:frame+1])
        return point, trail

    ani = FuncAnimation(fig, update, frames=len(x_t), interval=10)
    return ani

