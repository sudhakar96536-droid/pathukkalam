from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "name": "Sudhakar",
        "username": "@sudhakar",
        "caption": "Welcome to Pathukkalam 🚀",
        "image": "https://picsum.photos/500/300",
        "profile": "https://i.pravatar.cc/150?img=10"
    },
    {
        "name": "Arun",
        "username": "@arun",
        "caption": "Modern PWA app running in Flask",
        "image": "https://picsum.photos/500/301",
        "profile": "https://i.pravatar.cc/150?img=11"
    },
    {
        "name": "Vijay",
        "username": "@vijay",
        "caption": "Installable Android-like web app",
        "image": "https://picsum.photos/500/302",
        "profile": "https://i.pravatar.cc/150?img=12"
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/explore')
def explore():
    return render_template('explore.html', posts=posts)

@app.route('/new-post')
def new_post():
    return render_template('new_post.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
