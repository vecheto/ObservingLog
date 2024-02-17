from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
import os
import csv
from datetime import datetime
from weasyprint import HTML

app = Flask(__name__)

UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def save_image_and_data(image, text):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    filename = f"{datetime.utcnow().strftime('%H%M%S')}.jpg"
    image_path = None
    
    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
    
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.utcnow().strftime("%d/%m/%y"),
                         datetime.utcnow().strftime("%H:%M:%S"),
                         text,
                         image_path if image_path else ""])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    text = request.form['textInput']
    image = request.files['imageInput']
    save_image_and_data(image, text)
    return redirect(url_for('data'))

@app.route('/data')
def data():
    with open('data.csv', 'r') as csvfile:
        data1 = [row for row in csv.reader(csvfile)]
    return render_template('data.html', data=data1)

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

if __name__ == '__main__':
    app.run(debug=True)
