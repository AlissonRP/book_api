from gettext import find
from flask import Flask
from flask_restful import Resource, reqparse


books = [
    {"id_book": "Neuromancer", "review": 4.5, "author": "Willian Gibson"},
    {"id_book": "The last Wish", "review": 5, "author": "Andrzej Sapkowski"},
]

class ModelBook:

    def __init__(self, id_book, name, review, author):
        self.id_book = id_book
        self.review = review
        self.author = author

    def json(self):
        return {
                "id_book": self.id_book,
                "id_review": self.review,
                "id_author": self.author
            }

class Books(Resource):

    def get(self):
        return {"book": books}

    def post(self):
        pass

    def delete(self):
        pass


class Book(Resource):
    args = reqparse.RequestParser()
    args.add_argument("name")
    args.add_argument("review")
    args.add_argument("author")

    def find_book(id_book):
        return [x if x["id_book"] == id_book \
      else {"message": "book not found"} for x in books]

    def get(self, id_book):
      return  Book.find_book(id_book)  #sequential search fuuuck

    def post(self, id_book):


        data = Book.args.parse_args()
        book_obj = ModelBook(id_book, **data)
        new_book = book_obj.json()
        books.append(new_book)
        return new_book, 200

    def put(self, id_book):
        data = Book.args.parse_args()
        new_book = {
            "id_book": id_book, **data
        }
        book = Book.find_book(id_book)
        if book:
            book.update(new_book)
            return new_book, 200

        book.append(new_book)
        return new_book, 201

    def delete(self, id_book):
        global books
        books = [book for book in books if book["id_book"] != id_book]
        return {"message": "Book deleted"}