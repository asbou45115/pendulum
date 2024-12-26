# Pendulum Simulation

![image](https://github.com/user-attachments/assets/45aad08c-9ff1-4f2c-adc2-0fcc2be89ccd)

This project is a pendulum simulation written in Python using the `pygame` library for graphical rendering and `tkinter` for the control interface. The simulation models one or more pendulums with adjustable parameters such as length, initial angle, gravity, and the number of pendulums. The pendulums swing with a realistic motion, and the user can observe their paths in the simulation window.

## Features

- Simulates the motion of pendulums using basic physics principles.
- User-friendly graphical interface using `tkinter` to adjust:
  - Pendulum length
  - Initial angle of the pendulum
  - Gravity
  - Number of pendulums
- Real-time updating of pendulum parameters through a control panel.
- Option to view the trail of the pendulum's bob as it swings.

## Installation

```bash
pip install -r requirements.txt
sudo apt-get install python3-tk (On Linux if tkinter module error)
```

## Usage

To run the simulation run 

```bash
python3 pendulum.py
```

