# Import flask
from flask import Flask

# Initializing flask app
app = Flask(__name__)

# Student data
students = [
    {"Name": "pavan", "Age": 22, "Course": "Computer Science"},
    {"Name": "siva", "Age": 21, "Course": "Mathematics"},
    {"Name": "jaya", "Age": 23, "Course": "Business"}
]

# Route for seeing student data
@app.route('/students')
def student_data():

	# Returning an API for showing in ReactJS
	return {"students": students}

# Running app
if __name__ == '__main__':
	app.run(debug=True, port=5000)

