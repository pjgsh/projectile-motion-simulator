import streamlit as st
import numpy as np
from physics import compute_trajectory, compute_trajectory_with_drag
import matplotlib.pyplot as plt

v0 = st.slider("Velocity (m/s)", 0, 50, 15)
angle = st.slider("Angle", 0,90,45)
y0 = st.slider('Height Offset (m)', 0 ,100,0)
use_drag = st.checkbox("Include Air Resistance?")
show_velocity = st.checkbox('View Velocity Plot?')
show_acceleration = st.checkbox('View Acceleration Plot?')

if use_drag:
    mass = st.slider('Mass (kg)', 0.01, 10.0, 0.43)
    drag_cf = st.slider('Drag Coefficient', 0.0, 1.0, 0.25)
    area = st.slider('Area (m^2)', 0.001, 0.5, 0.038)
    x_nodrag, y_nodrag, t_nodrag, v_nodrag, ax_nodrag, ay_nodrag = compute_trajectory(v0, angle, y0)
    x_t, y_t, times, velocity, a_x, a_y = compute_trajectory_with_drag(v0, angle, mass, drag_cf, area, y0)


    fig, ax = plt.subplots()
    ax.plot(x_nodrag, y_nodrag, label='No Drag')
    ax.plot(x_t, y_t, label='With Drag')
    ax.set_xlabel('Horizontal Distance (m)')
    ax.set_ylabel('Vertical Distance (m)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else: 
    x_t, y_t, times, velocity, a_x, a_y = compute_trajectory(v0, angle, y0)

st.write(f'Velocity : {v0}')
fig, ax = plt.subplots()
ax.plot(x_t, y_t)
ax.set_xlabel('Horizontal Distance (m)')
ax.set_ylabel('Vertical Distance (m')
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)
if show_velocity:
    fig, ax = plt.subplots()
    ax.plot(times, velocity)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Speed (m/s)")
    ax.grid(True)
    st.pyplot(fig)

if show_acceleration:
    fig, axes = plt.subplots(1, 2, figsize=(10,4))
    axes[0].plot(times, a_x)
    axes[1].plot(times, a_y)
    axes[0].set_xlabel('Time (s)')
    axes[0].set_ylabel('Acceleration (m/s²)')
    axes[1].set_xlabel('Time (s)')
    axes[1].set_ylabel('Acceleration (m/s²)')
    axes[0].set_title('Horizontal Acceleration')
    axes[1].set_title('Vertical Acceleration')
    plt.tight_layout()    
    st.pyplot(fig)

