print('----- Set 1-2 - excercise_7 -----')
# Find the distance from the Axis center of a given point (x & y coordinates)
import math
x = int ( input ( 'Give the x point: ' ) )
y = int ( input ( 'Give the y point: ' ) )
distance = math.sqrt ( ( x ** 2 ) + ( y ** 2 ) )
print ( 'You gave' , x , 'and' , y ,
        'and the distance of these coordinates from the center of the axis is' , distance)

