from flask import Flask
from flask_restful import  Resource, Api

app = Flask(__name__)
api = Api(app)


class Books(Resource):
    def get(self):
        return {"book": "teste"}
    def post(self):
        pass
    
    def delete(self):
        pass



api.add_resource(Books, "/books")

if __name__ == "__main__":
    app.run(debug=True)