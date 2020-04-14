print('----- Set 1-2 - excercise_5 -----')
# Ask for a letter and check if this is a vowel or not
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # Φωνήεντα
print ( 'Vowels are the:', vowels )
letter = str( input ( 'Give a letter: ' ) )
if len(letter)>1:
    print ( '"' + letter + '" is bigger than one letter, so only the 1st character "' + letter[0] + '" will be checked.' )
if letter[0] in vowels:
    print ( letter[0], 'is a vowel.' )
else:
    print ( letter[0], 'is not a vowel.' )


