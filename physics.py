import numpy as np


def compute_trajectory(v0, angle_deg, y0=0, g=9.81, dt=0.01):
    """
    Computes projectile motion trajectory.

    Parameters:
        v0        : initial speed (m/s)
        angle_deg : launch angle (degrees)
        y0        : launch height above landing point (m). Default 0 = flat ground.
        g         : gravitational acceleration (m/s^2)
        dt        : time step for the simulation (s)

    Returns:
        x_t, y_t, t : numpy arrays of horizontal position, vertical position, and time
    """
    if v0 <= 0:
        raise ValueError("Initial velocity must be positive.")

    if angle_deg < 0 or angle_deg > 90:
        raise ValueError("Launch angle must be between 0 and 90 degrees.")

    if y0 < 0:
        raise ValueError("Initial height cannot be negative.")

    theta = np.radians(angle_deg)

    # Time of flight (derived from setting y(t) = 0, solving via quadratic formula)
    t_flight = (
        v0 * np.sin(theta)
        + np.sqrt((v0 * np.sin(theta))**2 + 2 * g * y0)
        ) / g

    t = np.arange(0, t_flight, dt)

    x_t = v0 * np.cos(theta) * t
    y_t = y0 + v0 * np.sin(theta) * t - 0.5 * g * t**2
    vx = v0 * np.cos(theta)
    vy = v0* np.sin(theta) - g*t
    a_x = np.zeros_like(t)
    a_y = - g * np.ones_like(t)
    velocity = np.sqrt(vx**2 + vy**2)
    if angle_deg == 0 and y0 == 0:
        return (
        np.array([0]),
        np.array([0]),
        np.array([0]),
        np.array([0]),
        np.array([0]),
        np.array([0])
    )
    return x_t, y_t, t, velocity, a_x, a_y





def compute_trajectory_with_drag(v0, angle_deg, mass, drag_cf, area, y0, g = 9.81, dt= 0.01, rho = 1.225):
    """
    Computes projectile motion trajectory with drag.

    Parameters:
        v0        : initial speed (m/s)
        angle_deg : launch angle (degrees)
        y0        : launch height above landing point (m). Default 0 = flat ground.
        g         : gravitational acceleration (m/s^2)
        dt        : time step for the simulation (s)
        mass      : mass of the projectile
        drag_cf   : estimated drag coefficient of the projectile
        area      : projectile estimated area
    """

    if v0 <= 0:
        raise ValueError("Initial velocity must be positive.")

    if angle_deg < 0 or angle_deg > 90:
        raise ValueError("Launch angle must be between 0 and 90 degrees.")

    if mass <= 0:
        raise ValueError("Mass must be positive.")

    if area <= 0:
        raise ValueError("Area must be positive.")

    if drag_cf < 0:
        raise ValueError("Drag coefficient cannot be negative.")

    if y0 < 0:
        raise ValueError("Initial height cannot be negative.")





    theta = np.radians(angle_deg)

    vx = v0*np.cos(theta)
    vy = v0 * np.sin(theta)
    x = 0
    y = y0

    x_positions = [x]
    y_positions = [y]
    times = [0]
    velocity = [np.sqrt(vx**2 + vy**2)]
    accelerations_x = [0]
    accelerations_y = [-g]
    t = 0


    while y >= 0:
        speed = np.sqrt(vx**2 + vy**2)
        drag_force = 0.5 * rho * area * drag_cf * speed ** 2

        if speed == 0:
            ay = -g
            ax = 0
        else:
            ax = -(drag_force / mass) * (vx/speed)
            ay = -g - (drag_force/mass) * (vy/speed)

        vx += ax*dt 
        vy += ay*dt
        x += vx*dt
        y += vy*dt
        t += dt
        speed = np.sqrt(vx**2+vy**2)
        x_positions.append(x)
        y_positions.append(y)
        times.append(t)
        velocity.append(speed)
        accelerations_x.append(ax)
        accelerations_y.append(ay)


    return (
        np.array(x_positions),
        np.array(y_positions),
        np.array(times),
        np.array(velocity),
        np.array(accelerations_x),
        np.array(accelerations_y))


    