from flask import Flask, blueprints, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

books_blueprint = Blueprint("books", __name__)

##### MVP #####

# INDEX
@books_blueprint.route('/books')
def books():
    books = book_repo.select_all()
    return render_template('/books/index.html', all_books = books)



# DELETE


##### EXTENSION #####


# NEW


# CREATE


# SHOW



##### ADVANCED EXTENSION #####


# EDIT


# UPDATE


