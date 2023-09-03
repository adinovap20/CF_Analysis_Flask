from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/analyze/', methods=['POST'])
def analyze():
    username = request.form.get('username')
    return username

@app.route('/dashboard')
def dashboard():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)