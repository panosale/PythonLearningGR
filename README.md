# PythonLearningGR
Μαθήματα - ασκήσεις Python

SITES - TITORIALS

https://docs.python.org/3/tutorial/

https://www.guru99.com/python-tutorials.html

https://realpython.com/ (needs to be member)


ΑΣΚΗΣΕΙΣ

Set 1 - http://users.tem.uoc.gr/~komineas/Teaching/MEM104_2016/exercises/index.html

Set 2 - http://users.tem.uoc.gr/~komineas/Teaching/MEM104_2017/Exercises/index.html

Set 3 - http://rousogiannis.blogspot.com/2016/01/python.html

Set 4 - http://users.sch.gr/karatolos/?page_id=411

Set 5 - http://ecourse.uoi.gr/mod/forum/discuss.php?d=9924

Set 6 - https://www.w3resource.com/python-exercises/


ΒΙΒΛΙΑ

https://www.ebooks4greeks.gr/category/free-ebooks/%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%B7%CF%83/%CE%B3%CE%BB%CF%89%CF%83%CF%83%CE%B5%CF%83-%CF%80%CF%81%CE%BF%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%85/%CE%B2%CE%B9%CE%B2%CE%BB%CE%B9%CE%B1-python


ΒΟΗΘΗΤΙΚΑ - ΣΗΜΕΙΩΣΕΙΣ

12 Python Tips and Tricks For Writing Better Code - Towards Data Science

https://towardsdatascience.com/12-python-tips-and-tricks-for-writing-better-code-b57e7eea580b

pylint - Εργαλείο εύρεσης λαθών σε προγράμματα Python

https://pypi.org/project/pylint/

https://github.com/PyCQA/pylint/

Για να ελέγξουμε αν αναγνωρίζονται τα μέλη κάποιων βιβλιοθηκών εκτελούμε το "check_if_import_cv2_works_fine.py".
Αν το VCS εμφανίσει μήνυμα "Module 'XXX' has no 'yyyyyyyy' member" κάνουμε τα παρακάτω:
1.    On VScode: CTRL + Shift + P
2.    Choose "Preferences: Open Settings (JSON)"
3.    Add this line into JSON file:
4.    "python.linting.pylintArgs": ["--generate-members"]
5.    Done, it works for me
Οι οδηγίες βρίσκονται εδώ: https://github.com/PyCQA/pylint/issues/2426 και εδώ: https://answers.opencv.org/question/200869/e1101module-cv2-has-no-imread-member/
