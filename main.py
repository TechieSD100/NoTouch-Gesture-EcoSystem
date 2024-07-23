from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Run Local Python File</h1>
    <form action="/run" method="post">
        <input type="text" name="filename" placeholder="Enter filename" required>
        <button type="submit">Run</button>
    </form>
    '''

@app.route('/run', methods=['POST'])
def run_file():
    filename = request.form['filename']
    try:
        result = subprocess.run(['python', filename], capture_output=True, text=True)
        output = result.stdout + result.stderr
        return f"<h2>Output:</h2><pre>{output}</pre>"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
