# PythonLearningGR
P Y T H O N

Μ Α Θ Η Μ Α Τ Α   -   Α Σ Κ Η Σ Ε Ι Σ - Ε Ρ Γ Α Λ Ε Ι Α

* SITES & TITORIALS

https://docs.python.org/3/tutorial/

https://www.guru99.com/python-tutorials.html

https://realpython.com/ (needs to be member)


* ΒΙΒΛΙΑ

https://www.ebooks4greeks.gr/category/free-ebooks/%CF%80%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CE%BA%CE%B7%CF%83/%CE%B3%CE%BB%CF%89%CF%83%CF%83%CE%B5%CF%83-%CF%80%CF%81%CE%BF%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B9%CF%83%CE%BC%CE%BF%CF%85/%CE%B2%CE%B9%CE%B2%CE%BB%CE%B9%CE%B1-python


* ΑΣΚΗΣΕΙΣ

Set 1 - http://users.tem.uoc.gr/~komineas/Teaching/MEM104_2016/exercises/index.html - N/A ?

Set 2 - http://users.tem.uoc.gr/~komineas/Teaching/MEM104_2017/Exercises/index.html - N/A ?

Set 3 - http://rousogiannis.blogspot.com/2016/01/python.html - DOWNLOADED IN "Exercises\Rousogiannis" FOLDER.

Set 4 - http://users.sch.gr/karatolos/?page_id=411 - DOWNLOADED IN "Exercises\Karatolos" FOLDER.

Set 5 - http://ecourse.uoi.gr/mod/forum/discuss.php?d=9924 - Οδηγεί στον παρακάτω σύνδεσμο:

Set 6 - https://www.w3resource.com/python-exercises/ - ΜΟΝΟ ONLINE.


* ΑΡΘΡΑ

12 Python Tips and Tricks For Writing Better Code - Towards Data Science: https://towardsdatascience.com/12-python-tips-and-tricks-for-writing-better-code-b57e7eea580b

When and Why to Use := Over = in Python: https://towardsdatascience.com/when-and-why-to-use-over-in-python-b91168875453

3 Python Tricks to Read, Create, and Run Multiple Files Automatically: https://towardsdatascience.com/3-python-tricks-to-read-create-and-run-multiple-files-automatically-5221ebaad2ba

Test your Python skills with these 10 projects: https://thenextweb.com/syndication/2020/09/30/test-your-python-skills-with-these-10-projects/amp/

Programming language Python is a big hit for machine learning. But now it needs to change: https://www.zdnet.com/google-amp/article/programming-language-python-is-a-big-hit-for-machine-learning-but-now-it-needs-to-change/

Top 12 Python Developer Skills You Must Need to Know: https://towardsdatascience.com/top-12-python-developer-skills-you-must-need-to-know-9e2b6c7fc6c

Methods in Python – A Key Concept of Object Oriented Programming: https://www.analyticsvidhya.com/blog/2020/11/basic-concepts-object-oriented-programming-types-methods-python/

Understand Loops in Python with One Article: https://towardsdatascience.com/understand-loops-in-python-with-one-article-bace2ddba789


* ΒΟΗΘΗΤΙΚΑ - ΧΡΗΣΙΜΑ ΠΑΚΕΤΑ (γίνονται εγκατάσταση από Command Prompt)

pylint - Εργαλείο εύρεσης λαθών σε προγράμματα Python

https://pypi.org/project/pylint/

https://github.com/PyCQA/pylint/

        pip install pylint

Jupyterlab

        pip install jupyterlab


* ΧΡΗΣΙΜΕΣ ΕΝΤΟΛΕΣ

* * Από Command Prompt:

        pip list -> Εμφανίζει λίστα όλων των εγκατεστημένων πακέτων στην Python.

* * Από Python:

        dir(κάποια μεταβλητή ή κλάση) -> Εμαφνίζει όλες τις ιδιότητες (attributes) της μεταβλητής/κλάσης.
        

* ΣΗΜΕΙΩΣΕΙΣ

***** ΠΡΟΒΛΗΜΑΤΑ *****

Για να ελέγξουμε αν αναγνωρίζονται τα μέλη κάποιων βιβλιοθηκών εκτελούμε το "check_if_import_cv2_works_fine.py".
Αν το VCS εμφανίσει μήνυμα "Module 'XXX' has no 'yyyyyyyy' member" κάνουμε τα παρακάτω:
1.    On VScode: CTRL + Shift + P
2.    Choose "Preferences: Open Settings (JSON)"
3.    Add this line into JSON file:
4.    "python.linting.pylintArgs": ["--generate-members"]

Οι οδηγίες βρίσκονται εδώ: https://github.com/PyCQA/pylint/issues/2426 και εδώ: https://answers.opencv.org/question/200869/e1101module-cv2-has-no-imread-member/
