import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


studentsAr = [{'name': 'maya', "age": 17},
            {'name': 'Itay', "age": 7},
            {'name': 'amir', "age": 12},
            {'name': 'noam', "age": 4}]


# get all
# get one (id)
# post 
@app.route("/students/",defaults={"id":-1},methods=['GET','POST'])
@app.route("/students/<int:id>",methods=['GET','POST'])
def students(id):
    if request.method == 'POST':
        request_data = request.get_json()
        sName= request_data['name']
        sAge= request_data['age']
        studentsAr.append( {'name': sName, "age":int( sAge)})
    if id> -1:
        return json.dumps(studentsAr[id])
    return json.dumps(studentsAr)


app.run(debug=True)
