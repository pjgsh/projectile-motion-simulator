# 🚀 Projectile Motion Simulator

An interactive Python-based projectile motion simulator that models the trajectory of a projectile **with and without aerodynamic drag**. The project combines analytical physics, numerical methods, and data visualization to simulate realistic projectile motion and analyze flight performance.

The simulator can be used through either a **command-line interface (CLI)** or an interactive **Streamlit web application**.

---

## Features

### Projectile Simulation
- Simulate projectile motion without air resistance using analytical equations.
- Simulate projectile motion with quadratic aerodynamic drag using Euler's Method.
- Supports customizable:
  - Initial velocity
  - Launch angle
  - Initial launch height
  - Projectile mass
  - Drag coefficient
  - Cross-sectional area

---

### Flight Analysis

The simulator calculates:

- Maximum horizontal distance
- Maximum height
- Total flight time
- Time to reach maximum height
- Maximum projectile speed
- Direction change time
- Horizontal and vertical acceleration
- Optimal launch angle for maximum range
- Range reduction caused by aerodynamic drag

---

### Visualization

The simulator generates:

- Projectile trajectory
- Position vs. Time
- Velocity vs. Time
- Acceleration vs. Time
- Drag vs. No-Drag trajectory comparison
- Range vs. Launch Angle optimization graph

---

### Interactive Streamlit Interface

The project includes a Streamlit application that allows users to:

- Adjust parameters using sliders
- Toggle air resistance on or off
- Enter projectile properties
- Run simulations instantly
- View plots directly within the browser

---

## Physics Model

### Without Air Resistance

Projectile motion is solved analytically using the kinematic equations

$$ x(t) = v_0 \cos(\theta)t $$

$$ y(t) = y_0 + v_0 \sin(\theta)t - \frac{1}{2}gt^2 $$

where

- $v_0$ = initial velocity
- $\theta$ = launch angle
- $g$ = gravitational acceleration
---

### With Aerodynamic Drag

Drag force is modeled as

Drag force is modeled as

$$ F_D = \frac{1}{2}\rho C_D A v^2 $$

where

- $\rho$ = air density
- $C_D$ = drag coefficient
- $A$ = cross-sectional area
- $v$ = instantaneous speed

The equations of motion are solved numerically using **Euler Integration**.

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Streamlit

---

## Project Structure

```text
PROJECTILE_MOTION_SIMULATOR/

│── app.py                  # Streamlit interface
│── main.py                 # Command-line application
│── physics.py              # Physics calculations
│── analysis.py             # Optimization analysis
│── plot.py                 # Plot generation
│── results.py              # Performance metrics
│── README.md
│── LICENSE
│
└── images/
    ├── app_interface.png
    ├── trajectory.png
    ├── drag_comparison.png
    ├── optimization.png
    ├── velocity.png
    └── acceleration.png
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Projectile-Motion-Simulator.git
```

Navigate into the project directory

```bash
cd Projectile-Motion-Simulator
```

Install the required packages

```bash
pip install numpy matplotlib streamlit
```

---

## Running the Project

### Command-Line Version

```bash
python main.py
```

### Streamlit Interface

```bash
streamlit run app.py
```

---

## Example Input

### Without Air Resistance

```text
Velocity: 30 m/s
Launch Angle: 35°
Initial Height: 0 m
```

### With Air Resistance

```text
Velocity: 30 m/s
Launch Angle: 35°
Initial Height: 0 m

Mass: 0.145 kg
Drag Coefficient: 0.47
Cross-sectional Area: 0.0042 m²
```

---

# Sample Results

## Streamlit Interface

![Streamlit Interface](app_interface.png)

---

## Projectile Trajectory

![Trajectory](images\trajectory.png)

---

## Drag vs. No-Drag Comparison

![Drag Comparison](images\drag_comparison.png)

---

## Launch Angle Optimization

![Optimization](images\optimization.png)

---

## Velocity Analysis

![Velocity](images\velocity.png)

---

## Acceleration Analysis

![Acceleration](images\acceleration.png)

---

## Future Improvements

Possible future additions include:

- Wind modeling
- Variable air density with altitude
- Runge-Kutta (RK4) integration
- 3D projectile motion
- Animated projectile trajectories
- Projectile presets (baseball, golf ball, soccer ball, etc.)
- Export simulation results to CSV
- Interactive parameter sensitivity studies

---

## What I Learned

This project strengthened my understanding of:

- Classical mechanics
- Projectile motion
- Newton's Second Law
- Aerodynamic drag modeling
- Numerical integration (Euler Method)
- Scientific computing with NumPy
- Data visualization using Matplotlib
- Building interactive applications with Streamlit
- Writing modular, reusable Python code

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
