import math
import matplotlib.pyplot as plt
import numpy as np




# ******************************
# * Constants and Variables   *
# ******************************

# Text variables declared as global
text_vo = None
text_Ve = None
text_ae = None
text_fr = None
text_n = None
text_inductance = None

# Constants
g = 9.81
μo = 4 * math.pi * 10**-7
ilim = 0.46  # 0.58




# **************
# * User Input *
# **************

# Necessary initializations
mp = float(input("What is the mass of the projectile? [kg] "))
me = float(input("What is the mass of the piston? [kg] "))
d = float(input("What is the diameter of the coil? [m] "))
dist = float(input("What is the launch distance? [m] "))
comp = float(input("What is the length of your coil? [m] "))
ang = float(input("What is the launch angle? [°] "))
cam = float(input("How many layers do you want in the coil? [integer] "))




# ****************
# * Calculations *
# ****************

# exit velocity to reach the desired distance
vo = math.sqrt((dist * g) / math.sin(2 * math.radians(ang)))
print("The initial velocity of the projectile is: ", vo, "m/s")
# final velocity of the piston after acceleration provided by the magnetic force
Ve = mp * vo / me
print("The final velocity of the piston is: ", Ve, "m/s")
# acceleration of the piston
ae = Ve**2 / (comp)
print("The acceleration developed by the piston is: ", ae, "m/s²")
# resultant force on the piston
fr = me * ae
print("The resultant force on the piston is: ", fr, "N")

LaunchEnergy = fr * dist
print("The launch energy is: ", LaunchEnergy, "N")

# The launch energy is equal to that of the coil
Inductance = (2 * LaunchEnergy) / (ilim**2)
print("The coil inductance is: ", Inductance, "H")

# Calculating the number of turns in the coil:
microH = Inductance * 1000000
dmm = d * 1000
wire_diameter = 0.4547  # wire diameter (mm)
n = math.sqrt((26.4 * (6 * dmm + 9 * comp + 10 * cam * wire_diameter) * microH) / (0.8 * (dmm**2)))
print("The number of turns in the coil is: ", n)



# ********************
# * Display the results *
# ********************

# Calculating the projectile trajectory
print('cos')
print(np.cos(np.radians(ang)))

vox = vo * np.cos(np.radians(ang))
voy = vo * np.sin(np.radians(ang))

total_time = (2 * voy) / g
time = np.linspace(0, total_time, 10)  # Adjust the number of points as needed

Hmax = (vo**2 * np.sin(np.radians(ang))**2) / (2 * g)
Amax = (vo**2 * np.sin(np.radians(2 * ang))) / (g)

# Coefficients of the quadratic equation
a = -Hmax / (Amax / 2)**2

# Define the parabola function
def parabola(x):
    return a * (x - Amax/2)**2 + Hmax

# Create a set of 20 equally spaced points for plotting
x_points = np.linspace(0, Amax, 40)

# Calculate the corresponding y values for the 20 points
y_points = parabola(x_points)

# Plotting the trajectory with texts and dots
plt.figure(figsize=(8, 6))
plt.scatter(x_points, y_points, color='blue')  # Adds points on the trajectory
plt.title('Projectile Motion')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')

# Adding texts to the image
plt.text(0.05, 0.9, f'The initial velocity of the projectile is: {vo:.5f} m/s', transform=plt.gca().transAxes)
plt.text(0.05, 0.85, f'The final velocity of the piston is: {Ve:.5f} m/s', transform=plt.gca().transAxes)
plt.text(0.05, 0.8, f'The acceleration developed by the piston is: {ae:.5f} m/s²', transform=plt.gca().transAxes)
plt.text(0.05, 0.75, f'The resultant force on the piston is: {fr:.5f} N', transform=plt.gca().transAxes)
plt.text(0.05, 0.7, f'The number of turns in the coil is: {n:.5f}', transform=plt.gca().transAxes)
plt.text(0.05, 0.65, f'The coil inductance is: {Inductance:.5f} H', transform=plt.gca().transAxes)

plt.legend()
plt.grid(True)
plt.show()