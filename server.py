from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninjas')
def display_ninjas():
	img = 'tmnt.png' 
	return render_template('ninjas.html', img='tmnt.png')

@app.route('/ninjas/<color>')
def display_color(color):
	if color == "blue":
		img = "leonardo.jpg"
	elif color == "orange":
		img = "michelangelo.jpg"
	elif color == "red":
		img = "raphael.jpg"
	elif color == "purple":
		img = "donatello.jpg"
	else:
		img = "notapril.jpg"

	return render_template('ninjas.html', img=img)

app.run(debug=True)