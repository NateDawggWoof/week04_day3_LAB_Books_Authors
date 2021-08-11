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
@books_blueprint.route('/books/<id>/delete', methods = ['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect('/books')

##### EXTENSION #####


# NEW
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repo.select_all()
    return render_template('books/new.html', all_authors = authors)


# CREATE
@books_blueprint.route('/books', methods = ['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, genre,publisher, author)
    book_repo.save(book)
    return redirect('/books')


# SHOW
@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repo.select(id)
    return render_template('books/show.html', book = book)


##### ADVANCED EXTENSION #####


# EDIT
@books_blueprint.route('/books/<id>/edit')
def edit_book(id):
    book = book_repo.select(id)
    authors =author_repo.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)

# UPDATE
@books_blueprint.route('/books/<id>', methods = ['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book = Book(title, genre,publisher, author, id)
    book_repo.update(book)
    return redirect('/books')
