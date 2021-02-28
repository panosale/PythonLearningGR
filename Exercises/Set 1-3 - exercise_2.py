print ( '----- Set 1-3 - excercise_2 -----' )
# 2. Γράψτε μερικές εντολές Python οι οποίες δεδομένης μιας θερμοκρασίας T
# τυπώνουν το μήνυμα Cold... αν η θερμοκρασία είναι μικρότερη από 10 βαθμούς,
# το μήνημα Hot... αν η θερμοκρασία είναι μεγαλύτερη από 35 βαθμούς
# και το μήνυμα Pleasant... διαφορετικά.
t = float ( input ( 'Give the temperature: ') )
if t < 10:
    print ( 'Cold...' )
elif t > 35:
    print ( 'Hot...' )
else:
    print ( 'Pleasant...' )
