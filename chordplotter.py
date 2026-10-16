from typing import Type

import numpy as np
import matplotlib.pyplot as plt

import chord


def plot(chord: Type[chord.Chord]) -> None:

    # The Calculating Stuff
    
    # angles of points on circle
    theta_circle = np.linspace(0.0, 2.0*np.pi, 180)

    # angles of points on arc
    theta_arc = np.linspace(0.0, 
                            chord.anglerad, 
                            int(180 * (chord.anglerad/(2.0*np.pi))))

    # calculate coordinates of circle points
    circle_x = chord.radius * np.cos(theta_circle)
    circle_y = chord.radius * np.sin(theta_circle)

    # calculate coordinates of arc points
    arc_x = chord.radius * np.cos(theta_arc)
    arc_y = chord.radius * np.sin(theta_arc)

    # coordinates of outer end of second radius line
    xc = np.cos(chord.anglerad) * chord.radius
    yc = np.sin(chord.anglerad) * chord.radius

    # The Plotting Stuff

    fig, ax = plt.subplots(figsize=(6,6))

    # circle
    ax.plot(circle_x,
            circle_y,
            label=f"radius {chord.radius:0.2f}",
            linewidth=0.5,
            color='#FF0080')
    
    # arc
    ax.plot(arc_x,
            arc_y,
            label=f"arc length {chord.arclength:0.2f}",
            color='#8000FF')

    # radius lines
    plt.plot((0,chord.radius), 
             (0, 0),
             label=f"angle {chord.anglerad:0.2f}rad",
             color='#FF8000')

    plt.plot((0,xc), 
             (0, yc), 
             color='#FF8000')

    # chord
    plt.plot((chord.radius,xc), 
             (0, yc), 
             label=f"chord length {chord.chordlength:0.2f}",
             color='#00C000')

    # axes must be same scale
    plt.gca().set_aspect('equal')

    # legend at top of fig, NOT in ax
    fig.legend(ncols=2, loc="upper center")

    plt.grid()

    plt.show()