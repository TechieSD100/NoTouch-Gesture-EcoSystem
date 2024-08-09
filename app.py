from flask import Flask, render_template, redirect, url_for
import subprocess


app = Flask(__name__)

# Store process objects
processes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script1')
def run_script1():
    process = subprocess.Popen(['start', 'cmd', '/k', 'cd AIVirtualMouse && python AIVirtualMouseProject.py'], shell=True)
    processes['script1'] = process.pid
    return redirect(url_for('index'))

@app.route('/run_script2')
def run_script2():
    process = subprocess.Popen(['start', 'cmd', '/k', 'cd Gesture_Presentation && python presentation.py'], shell=True)
    processes['script2'] = process.pid
    return redirect(url_for('index'))

@app.route('/run_script3')
def run_script3():
    process = subprocess.Popen(['start', 'cmd', '/k', 'cd Pong_Game && python ponggame.py'], shell=True)
    processes['script3'] = process.pid
    return redirect(url_for('index'))

@app.route('/run_script4')
def run_script4():
    process = subprocess.Popen(['start', 'cmd', '/k', 'cd Kids_Education && python kidsedu.py'], shell=True)
    processes['script4'] = process.pid
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
