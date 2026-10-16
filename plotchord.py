import math

import chord
import chordplotter as cp


def main():

    c = chord.Chord(anglerad=4.5,
                    radius=32,
                    chordlength=0,
                    arclength=0)
    
    c.chordlength = 2.0 * c.radius * math.sin(c.anglerad/2.0)
    c.arclength = c.radius * c.anglerad

    cp.plot(c)


if __name__ == "__main__":

    main()