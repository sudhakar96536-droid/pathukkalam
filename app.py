from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/add-post', methods=['POST'])
def add_post():

    username = request.form.get('username')
    caption = request.form.get('caption')

    posts.insert(0, {
        'username': username,
        'caption': caption
    })

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
