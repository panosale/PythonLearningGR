print('----- Set 1-2 - excercise_6 -----')
# Function that finds the average of the three given numbers
def Avg ( num1, num2, num3 ):
    return int ( ( num1 + num2 + num3 ) / 3)
# Function that finds the minimum of the three given numbers
def Min ( num1, num2, num3 ):
    new_min = n1
    if n2 < new_min:
        new_min = n2
    if n3 < new_min:
        new_min = n3
    return new_min
# Function that finds the minimum of the three given numbers
def Max ( num1, num2, num3 ):
    new_max = n1
    if n2 > new_max:
        new_max = n2
    if n3 > new_max:
        new_max = n3
    return new_max
# Ask for 3 numbers
n1 = int ( input ( 'Give 1st number: ' ) )
n2 = int ( input ( 'Give 2nd number: ' ) )
n3 = int ( input ( 'Give 3rd number: ' ) )
print ( '**********' )
# Calls the Avg function with the 3 numbers
print ( 'The average of the given numbers is :', Avg ( n1, n2, n3 ))
# Calls the Min function with the 3 numbers
print ( 'The minimum of the given numbers is :', Min ( n1, n2, n3 ))
# Calls the Max function with the 3 numbers
print ( 'The maximum of the given numbers is :', Max ( n1, n2, n3 ))
