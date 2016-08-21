# quotes.py
# A program for recording quotes and displaying them on demand.

# Contains all the info for a Quote object.
class Quote:
    def __init__(self, quote, author, date):
        self.quote = quote
        self.author = author
        self.date = date

    def display(self):
        output = "\"{}\", {}, {}.".format(self.quote, self.author, self.date)
        print(output)

# Variables.
quote1 = "If you're constantly defending something everytime you do it\
, maybe you've done something fucking indefensible."
author1 = "Jim Sterling"
date1 = "October 2015"

quote2 = "Time began at Thursday, 1st January, 1970."
author2 = "UNIX time"
date2 = "01/01/1970"

quote3 = "A pointer is a variable that stores a memory location."
author3 = "Dan Gookin, Beginning Programming with C for Dummies"
date3 = "2014"

# Making the Quote object.
inspiration1 = Quote(quote1, author1, date1)
inspiration2 = Quote(quote2, author2, date2)
inspiration3 = Quote(quote3, author3, date3)

# Printing the Quote details.
inspiration1.display()
inspiration2.display()
inspiration3.display()
