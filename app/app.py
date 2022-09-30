from flask import Flask, jsonify
from flask_restful import Api
from resources.book import  Books, Book

app = Flask(__name__)
api = Api(app)








api.add_resource(Books, "/books")
api.add_resource(Book, "/books/<string:id_book>")
if __name__ == "__main__":
    app.run(debug=True)
