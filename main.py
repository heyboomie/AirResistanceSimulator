import math

# Constants
CD = 0.47  # Drag coefficient for sphere
P = 1.225  # Air density at 15°C (kg/m^3)
PI = math.pi
G = 9.80665
HALF = 0.5

# Input
r_cm = float(input("Radius of the object in cm: "))
r = r_cm / 100  # Convert to meters
A = PI * r * r  # Cross-sectional area

vi = float(input("Initial velocity in m/s: "))
vr = vi
theta_deg = float(input("Initial launch angle in degrees: "))
thetai = math.radians(theta_deg)

hi = float(input("Initial height (m): "))
hr = hi
mass = float(input("Mass of the object (kg): "))
riemann = int(input("Number of subdivisions (e.g., 2 = 0.5s steps): "))

# Initialize position and velocity arrays with initial values
dxarray = [0]
dyarray = [hi]
vxarray = [vr * math.cos(thetai)]
vyarray = [vr * math.sin(thetai)]


# Initialize variables
dr = 0
t = 0
thetar = thetai

while hr > 0:
    # Decompose velocity
    vx = vr * math.cos(thetar)
    vy = vr * math.sin(thetar)
    
    # Distance updates
    dt = 1 / riemann
    dr += vx * dt
    hr += vy * dt
    dxarray.append(dr)
    dyarray.append(hr)
    vxarray.append(vx)
    vyarray.append(vy)
    # Drag force
    drag = HALF * P * vr**2 * CD * A
    dragx = drag * math.cos(thetar)
    dragy = drag * math.sin(thetar)

    # Velocity update
    vx -= (dragx / mass) * dt
    vy -= ((dragy / mass) * dt + G * dt)

    # Recompute total velocity and angle
    thetar = math.atan2(vy, vx)
    vr = math.sqrt(vx**2 + vy**2)

    # Time update
    t += dt

print(f"Final height: {hr:.2f} m. Final distance: {dr:.2f} m. Total flight time: {t:.2f} s.")
print(dxarray)
print(dyarray)
print(vxarray)
print(vyarray)

