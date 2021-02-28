print('----- Set 1-2 - excercise_3 -----')
# s = 'AppliedMathematics'
s = input('Give a string : ')
# *** Print initial string
print('Initial string        =', s)

# *** α) Print 1st 6 characters
print('α) 1st 6 characters      =', s[0:6])

# *** β) Print last 5 characters
print('β) Last 5 characters     =', s[-5:])

# *** γ) Print every 2nd character starting from pos 3
# **** Print only for the standard string "AppliedMathematics"
# print('Every 2nd character from "' + s2 + '" starting from pos 3 =',
#      s2[1] + s2[3] + s2[5] + s2[7] + s2[9] + s2[11] + s2[13] + s2[15])
# **** Print dynamically for every given string
s2 = s[2:]
s3 = ''
for i in range(1, len(s2), 2):
    s3 += s2[i]
print('γ) Every 2nd character from "' + s2 + '" (starting from pos 3 of the initial string) =', s3)

# *** δ) Print all characters starting from 2nd last towards 1st
s2 = s[0:len(s)-1]
s3 = ''
for i in range(len(s2)-1, -1, -1):
    s3 += s2[i]
print('δ) Given string starting from 2nd last towards 1st =', s3)

# *** ε) Print odd and even numbers separately
s_odd = ''
s_even = ''
for i in range(0, len(s), 2):
    s_odd += s[i]
for i in range(1, len(s), 2):
    s_even += s[i]
print('ε) Letters from odd places are "' + s_odd + '" and from even places are "' + s_even + '".')
