from flask import Flask, render_template, request
from codeforces.analysis import CodeforcesAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/analyze/', methods=['POST'])
def analyze():
    username = request.form.get('username')
    analyzer = CodeforcesAnalyzer(username)
    return f"{analyzer.get_datablock().__dict__}"

@app.route('/dashboard')
def dashboard():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)