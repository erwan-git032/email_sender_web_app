from flask import Flask, render_template, request, flash, redirect, url_for
from email_utils import send_email
import os

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods = ['POST'])
def send():
    to_email = request.form['to_email']
    subject = request.form['subject']
    message = request.form['message']
    file = request.files.get('attachment')

    attachment_path = None
    if file:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        attachment_path = f"uploads/{file.filename}"
        file.save(attachment_path)

    success, msg = send_email(to_email, subject, message, attachment_path)

    if attachment_path:
        os.remove(attachment_path)

    flash(msg, 'success' if success else 'error')

    return render_template('index.html', message = msg, success = success)


if __name__ == '__main__':
    app.run(debug=True)