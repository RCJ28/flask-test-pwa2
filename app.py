from flask import Flask, render_template, send_file, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    file_path = './content.txt'
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
        else:
            content = "Unable to find file"
    except Exception as e:
        content = "Unable to find file"

    return render_template("index.html", content=content)

@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/add', methods=['POST'])
def add():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
    except ValueError:
        result = "Invalid input. Please enter numbers only."
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
