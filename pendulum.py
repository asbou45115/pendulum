import math
import pygame
import tkinter as tk
from tkinter import ttk
import threading
import random

pygame.init()

###################################################################
# Initial variables

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 1000
BG_COLOUR = (0, 0, 0)
PENDULUM_COLOUR = (255, 255, 255)
TRAIL_COLOUR = (57, 255, 20)
PENDULUM_LENGTH = 200
INITIAL_ANGLE = math.pi / random.randrange(2, 9)
GRAVITY = 9.8
TIME_STEP = 0.1
NUM_PENDULUMS = 1
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
num_pend_var = tk.IntVar(value = NUM_PENDULUMS)
length_var = tk.DoubleVar(value = PENDULUM_LENGTH)
angle_var = tk.DoubleVar(value = math.degrees(INITIAL_ANGLE))
gravity_var = tk.DoubleVar(value = GRAVITY)

# Function to update the simulation parameters
def update_parameters(*args):
    global PENDULUM_LENGTH, INITIAL_ANGLE, GRAVITY, NUM_PENDULUMS
    PENDULUM_LENGTH = length_var.get()
    INITIAL_ANGLE = math.radians(angle_var.get())
    GRAVITY = gravity_var.get()
    NUM_PENDULUMS = num_pend_var.get()
    length_label.config(text=f"Pendulum Length (pixels): {int(PENDULUM_LENGTH)}")
    angle_label.config(text=f"Initial Angle (degrees): {int(angle_var.get())}")
    gravity_label.config(text=f"Gravity (m/s^2): {gravity_var.get():.2f}")
    num_pend_label.config(text=f"Number of Pendulums: {int(NUM_PENDULUMS)}")
    
num_pend_label = ttk.Label(root, text=f"Number of Pendulums: {int(NUM_PENDULUMS)}")
num_pend_slider = ttk.Scale(root, variable=num_pend_var, from_=1, to=8, orient="horizontal")

length_label = ttk.Label(root, text=f"Pendulum Length (pixels): {int(PENDULUM_LENGTH)}")
length_slider = ttk.Scale(root, variable=length_var, from_=50, to=300, orient="horizontal")

angle_label = ttk.Label(root, text=f"Initial Angle (degrees): {int(angle_var.get())}")
angle_slider = ttk.Scale(root, variable=angle_var, from_=0, to=90, orient="horizontal")

gravity_label = ttk.Label(root, text=f"Gravity (m/s^2): {gravity_var.get():.2f}")
gravity_slider = ttk.Scale(root, variable=gravity_var, from_=1, to=20, orient="horizontal")

# Pack widgets into the Tkinter window
num_pend_label.pack()
num_pend_slider.pack()
length_label.pack()
length_slider.pack()
angle_label.pack()
angle_slider.pack()
gravity_label.pack()
gravity_slider.pack()

# Updates the data on the sliders 
num_pend_var.trace("w", update_parameters)
length_var.trace("w", update_parameters)
angle_var.trace("w", update_parameters)
gravity_var.trace("w", update_parameters)

###################################################################
# Main loop function for the pendulum simulation
def run_simulation():
    global running, TIME_STEP
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BG_COLOUR)
        
        for i in range(0, NUM_PENDULUMS):
            pend_len = PENDULUM_LENGTH + (20 * i)
            theta = INITIAL_ANGLE * math.cos(math.sqrt(GRAVITY / pend_len) * TIME_STEP)  
            
            pend_x = SCREEN_WIDTH // 2 + pend_len * math.sin(theta)
            pend_y = SCREEN_HEIGHT // 2 + pend_len * math.cos(theta)
        
            if NUM_PENDULUMS == 1:
                trail_pos.append((pend_x, pend_y))
                if len(trail_pos) > 100:
                    trail_pos.pop(0)
                
                for j in range(1, len(trail_pos)):
                    pygame.draw.aaline(screen, TRAIL_COLOUR, trail_pos[j - 1], trail_pos[j])  
            
            pygame.draw.line(screen, PENDULUM_COLOUR, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (pend_x, pend_y), 1)
            pygame.draw.circle(screen, (255 - (i * 20), 255, 255 - (i * 20)), (pend_x, pend_y), 10)
            
        pygame.display.flip()
        clock.tick(60)
        TIME_STEP += 0.1
    
    pygame.quit()
    
simulation_thread = threading.Thread(target=run_simulation)
simulation_thread.start()

root.mainloop()