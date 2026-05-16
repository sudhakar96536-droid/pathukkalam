from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "name": "Sudhakar",
        "username": "@sudhakar",
        "caption": "Welcome to Pathukkalam 🚀",
        "image": "https://picsum.photos/500/300"
    },
    {
        "name": "Arun",
        "username": "@arun",
        "caption": "Modern PWA app running in Flask",
        "image": "https://picsum.photos/500/301"
    },
    {
        "name": "Vijay",
        "username": "@vijay",
        "caption": "Installable Android-like web app",
        "image": "https://picsum.photos/500/302"
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/explore')
def explore():
    return render_template('explore.html', posts=posts)

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

if __name__ == '__main__':
    app.run(debug=True)
