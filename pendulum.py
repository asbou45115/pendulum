import math
import pygame
import tkinter as tk
from tkinter import ttk
import threading
import random

pygame.init()

###################################################################
# Initial variables

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOUR = (0, 0, 0)
PENDULUM_COLOUR = (255, 255, 255)
TRAIL_COLOUR = (57, 255, 20)
PENDULUM_LENGTH = 200
INITIAL_ANGLE = math.pi / random.randrange(1, 9)
GRAVITY = 9.8
TIME_STEP = 0.1
###################################################################
# Initialises the GUI for the screen  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pendulum Simulation")
clock = pygame.time.Clock()

running = True

# array containing the positions the bob has been
trail_pos = []  

###################################################################
root = tk.Tk()
root.title("Pendulum Controls")

# Create slider variables
length_var = tk.DoubleVar(value = PENDULUM_LENGTH)
angle_var = tk.DoubleVar(value = math.degrees(INITIAL_ANGLE))
gravity_var = tk.DoubleVar(value = GRAVITY)

# Function to update the simulation parameters
def update_parameters(*args):
    global PENDULUM_LENGTH, INITIAL_ANGLE, GRAVITY
    PENDULUM_LENGTH = length_var.get()
    INITIAL_ANGLE = math.radians(angle_var.get())
    GRAVITY = gravity_var.get()
    length_label.config(text=f"Pendulum Length (pixels): {int(PENDULUM_LENGTH)}")
    angle_label.config(text=f"Initial Angle (degrees): {int(angle_var.get())}")
    gravity_label.config(text=f"Gravity (m/s^2): {gravity_var.get():.2f}")

length_label = ttk.Label(root, text=f"Pendulum Length (pixels): {int(PENDULUM_LENGTH)}")
length_slider = ttk.Scale(root, variable=length_var, from_=50, to=300, orient="horizontal")

angle_label = ttk.Label(root, text=f"Initial Angle (degrees): {int(angle_var.get())}")
angle_slider = ttk.Scale(root, variable=angle_var, from_=0, to=90, orient="horizontal")

gravity_label = ttk.Label(root, text=f"Gravity (m/s^2): {gravity_var.get():.2f}")
gravity_slider = ttk.Scale(root, variable=gravity_var, from_=1, to=20, orient="horizontal")

# Pack widgets into the Tkinter window
length_label.pack()
length_slider.pack()
angle_label.pack()
angle_slider.pack()
gravity_label.pack()
gravity_slider.pack()

length_var.trace("w", update_parameters)
angle_var.trace("w", update_parameters)
gravity_var.trace("w", update_parameters)

def run_simulation():
    global running, TIME_STEP
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BG_COLOUR)
        theta = INITIAL_ANGLE * math.cos(math.sqrt(GRAVITY / PENDULUM_LENGTH) * TIME_STEP)  
        
        pend_x = SCREEN_WIDTH // 2 + PENDULUM_LENGTH * math.sin(theta)
        pend_y = SCREEN_HEIGHT // 2 + PENDULUM_LENGTH * math.cos(theta)
    
        trail_pos.append((pend_x, pend_y))
        if len(trail_pos) > 100:
            trail_pos.pop(0)
        
        for i in range(1, len(trail_pos)):
            pygame.draw.aaline(screen, TRAIL_COLOUR, trail_pos[i - 1], trail_pos[i])  
        
        pygame.draw.line(screen, PENDULUM_COLOUR, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (pend_x, pend_y), 1)
        pygame.draw.circle(screen, PENDULUM_COLOUR, (pend_x, pend_y), 10)
        
        pygame.display.flip()
        clock.tick(60)
        TIME_STEP += 0.1
    
    pygame.quit()
    
simulation_thread = threading.Thread(target=run_simulation)
simulation_thread.start()

root.mainloop()