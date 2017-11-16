import webbrowser

# Class
class Book():
    """ This class provides Book information from the Golden Lion publisher. """
    
    # Constructor
    def __init__(self, book_title, book_summary, book_author, book_release_date, book_url):
        # instance variables - relative to the instances
        self.title = book_title
        self.summary = book_summary
        self.author = book_author
        self.release_date = book_release_date
        self.url = book_url
    # instance method
    def show_summary(self):
        webbrowser.open(self.url)
    # Class Variables (all instances share)
    PUBLISHER = ["Golden Lion"]