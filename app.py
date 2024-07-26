from flask import Flask, render_template, send_file, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

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
