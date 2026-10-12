import math

import chord


def main():

    c = chord.Chord(anglerad=math.radians(40),
                    radius=76,
                    chordlength=51.987061785501645,
                    arclength=53.058009260627614)
    
    print()

    print("CHORD LENGTH \n------------")

    # chordlength from radius and anglerad
    c.chordlength = 2.0 * c.radius * math.sin(c.anglerad/2.0)
    print(f"{c.chordlength}")

    # chordlength from radius and arclength
    c.chordlength = 2.0 * c.radius * math.sin(c.arclength / (2.0*c.radius))
    print(f"{c.chordlength}")

    print()

    print("ARC LENGTH\n----------")

    # arclength from radius and anglerad
    c.arclength = c.radius * c.anglerad
    print(f"{c.arclength}")

    print()

    print("ANGLE\n-----")

    # anglerad from chordlength and radius
    c.anglerad = 2.0 * math.asin(c.chordlength / (2*c.radius))
    print(f"{c.anglerad}rad")
    print(f"{math.degrees(c.anglerad)}°")

    # anglerad from arclength and radius
    c.anglerad = c.arclength / c.radius
    print(f"{c.anglerad}rad")
    print(f"{math.degrees(c.anglerad)}°")

    print()

    print("RADIUS\n------")

    # radius from arclength and anglerad
    c.radius = c.arclength / c.anglerad
    print(f"{c.radius}")


if __name__ == "__main__":

    main()