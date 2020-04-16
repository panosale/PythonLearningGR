import math
# theta = 0.5235987755982988
theta = float(input('Give theta (must be between 0 and π/2): '))
if theta > 0 and theta < math.pi/2:
    print('sin =', math.sin(theta))
    print('cos =', math.cos(theta))
    print('tan =', math.tan(theta))
else:
    print('theta is out of limits (0 to π/2).')
# Χρειάζεται έλεγχο γιατί τα αποτελέσματα δεν συμβαδίζουν με το παράδειγμα της άσκησης (theta = 0.5235987755982988)
