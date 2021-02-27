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

Build your programming skills with these e-courses, from Python to SwiftUI: https://amp.cnn.com/cnn/2020/12/23/cnn-underscored/learn-to-code-bundle-review/index.html

A Full-Length Machine Learning Course in Python for Free: https://towardsdatascience.com/a-full-length-machine-learning-course-in-python-for-free-f2732954f35f

3 Useful Projects to learn Python Classes: https://towardsdatascience.com/3-useful-projects-to-learn-python-classes-cf0076c36297

Learn Python by Building 12 Projects in This 3-Hour Course: https://www.freecodecamp.org/news/learn-how-to-build-12-python-projects-in-one-course/amp/

Three Functions to Know in Python: https://towardsdatascience.com/three-functions-to-know-in-python-4f2d27a4d05

Learn Python by coding a simple game: https://opensource.com/article/20/12/learn-python

10 Surprisingly Useful Base Python Functions: https://towardsdatascience.com/10-surprisingly-useful-base-python-functions-822d86972a23

Python Code Performance Measurement – Measure the right metric to optimize better!: https://www.analyticsvidhya.com/blog/2021/01/python-code-performance-measurement-measure-the-right-metric-to-optimize-better/

Functional Programming in Python: When and How to Use It – Real Python: https://realpython.com/python-functional-programming/

Python in Visual Studio Code – January 2021 Release | Python: https://devblogs.microsoft.com/python/python-in-visual-studio-code-january-2021-release/

Understanding Feature Importance and How to Implement it in Python: https://towardsdatascience.com/understanding-feature-importance-and-how-to-implement-it-in-python-ff0287b20285

11 Python Built-in Functions You Should Know: https://towardsdatascience.com/11-python-built-in-functions-you-should-know-877a2c2139db



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

        dir(κάποια μεταβλητή ή κλάση) -> Εμφανίζει όλες τις ιδιότητες (attributes) της μεταβλητής/κλάσης.
        

* ΣΗΜΕΙΩΣΕΙΣ

***** ΠΡΟΒΛΗΜΑΤΑ *****

Για να ελέγξουμε αν αναγνωρίζονται τα μέλη κάποιων βιβλιοθηκών εκτελούμε το "check_if_import_cv2_works_fine.py".
Αν το VCS εμφανίσει μήνυμα "Module 'XXX' has no 'yyyyyyyy' member" κάνουμε τα παρακάτω:
1.    On VScode: CTRL + Shift + P
2.    Choose "Preferences: Open Settings (JSON)"
3.    Add this line into JSON file:
4.    "python.linting.pylintArgs": ["--generate-members"]

Οι οδηγίες βρίσκονται εδώ: https://github.com/PyCQA/pylint/issues/2426 και εδώ: https://answers.opencv.org/question/200869/e1101module-cv2-has-no-imread-member/
