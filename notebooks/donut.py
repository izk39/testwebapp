import os
import math
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def spin_donut():
    A, B = 0, 0  # Rotation angles
    while True:
        clear_console()

        # Constants for the dimensions and rendering
        width, height = 40, 20
        R1, R2 = 1, 2
        K2 = 15
        K1 = width * K2 * 3 / (8 * (R1 + R2))

        # Buffers for the frame
        output = [[' ' for _ in range(width)] for _ in range(height)]
        zbuffer = [[0 for _ in range(width)] for _ in range(height)]

        for theta in range(0, 628, 7):  # Angle around donut cross-section
            for phi in range(0, 628, 2):  # Angle around the torus center
                # Convert to radians
                theta_r = theta * 0.01
                phi_r = phi * 0.01

                # Coordinates of the donut in 3D
                cos_theta, sin_theta = math.cos(theta_r), math.sin(theta_r)
                cos_phi, sin_phi = math.cos(phi_r), math.sin(phi_r)
                h = cos_theta + R2
                z = 1 / (sin_phi * h * math.sin(A) + cos_theta * math.cos(A) + 5)

                # Project 3D to 2D
                x = int(width / 2 + K1 * z * (cos_phi * h * math.cos(B) - h * sin_phi * math.sin(B)))
                y = int(height / 2 + K1 * z * (cos_phi * h * math.sin(B) + h * sin_phi * math.cos(B)))
                luminance = int(8 * (sin_phi * cos_theta * math.sin(A) - cos_phi * sin_theta * math.cos(A)))

                if 0 <= x < width and 0 <= y < height and z > zbuffer[y][x]:
                    zbuffer[y][x] = z
                    output[y][x] = ".,-~:;=!*#$@"[max(0, min(8, luminance))]

        # Render the frame
        print('\n'.join(''.join(row) for row in output))

        # Update the angles for the spin
        A += 0.04
        B += 0.02

        time.sleep(0.03)

# Run the spinning donut
try:
    spin_donut()
except KeyboardInterrupt:
    print("\nAnimation stopped.")